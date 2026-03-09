#!/usr/bin/env python3
"""Google SRE 3권 다운로드 및 Markdown 변환 스크립트.

3권의 Google SRE 서적을 챕터별 Markdown 파일로 변환합니다:
  1. Site Reliability Engineering (sre-book)
  2. The Site Reliability Workbook (workbook)
  3. Building Secure & Reliable Systems (bsrs)

사용법:
  python3 scripts/download_sre_books.py --book all
  python3 scripts/download_sre_books.py --book sre-book --chapter introduction
  python3 scripts/download_sre_books.py --book workbook --resume
  python3 scripts/download_sre_books.py --verify
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ─── 설정 ─────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent / "docs"
REQUEST_DELAY = 2.0  # 요청 간 지연(초)
MAX_RETRIES = 3
RETRY_BACKOFF = 2.0
REQUEST_TIMEOUT = 30
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
)


# ─── 데이터 모델 ──────────────────────────────────────────────────────


@dataclass
class ChapterInfo:
    """챕터 메타데이터."""

    number: int  # 0 = 부록/기타
    slug: str
    title: str
    url_path: str
    part: str = ""
    authors: list[str] = field(default_factory=list)
    chapter_type: str = "chapter"  # chapter, appendix, foreword, preface, etc.


@dataclass
class BookConfig:
    """책별 설정."""

    key: str
    title: str
    base_url: str
    chapters: list[ChapterInfo]
    content_selector: str  # CSS selector for main content
    heading_offset: int = 0  # 헤딩 수준 조정값


# ─── 책 설정 정의 ─────────────────────────────────────────────────────


def build_sre_book_config() -> BookConfig:
    """Site Reliability Engineering 설정."""
    chapters = [
        # Part I - Introduction
        ChapterInfo(1, "introduction", "Introduction", "introduction/",
                     part="I - Introduction",
                     authors=["Benjamin Treynor Sloss"]),
        ChapterInfo(2, "production-environment",
                     "The Production Environment at Google, from the Viewpoint of an SRE",
                     "production-environment/",
                     part="I - Introduction",
                     authors=["JC van Winkel"]),
        # Part II - Principles
        ChapterInfo(3, "embracing-risk", "Embracing Risk", "embracing-risk/",
                     part="II - Principles",
                     authors=["Marc Alvidrez"]),
        ChapterInfo(4, "service-level-objectives", "Service Level Objectives",
                     "service-level-objectives/",
                     part="II - Principles",
                     authors=["Chris Jones", "John Wilkes", "Niall Murphy"]),
        ChapterInfo(5, "eliminating-toil", "Eliminating Toil", "eliminating-toil/",
                     part="II - Principles",
                     authors=["Vivek Rau"]),
        ChapterInfo(6, "monitoring-distributed-systems", "Monitoring Distributed Systems",
                     "monitoring-distributed-systems/",
                     part="II - Principles",
                     authors=["Rob Ewaschuk"]),
        ChapterInfo(7, "automation-at-google",
                     "The Evolution of Automation at Google",
                     "automation-at-google/",
                     part="II - Principles",
                     authors=["Niall Murphy", "John Looney", "Michael Kacirek"]),
        ChapterInfo(8, "release-engineering", "Release Engineering",
                     "release-engineering/",
                     part="II - Principles",
                     authors=["Dinah McNutt"]),
        ChapterInfo(9, "simplicity", "Simplicity", "simplicity/",
                     part="II - Principles",
                     authors=["Max Luebbe"]),
        # Part III - Practices
        ChapterInfo(10, "practical-alerting",
                     "Practical Alerting from Time-Series Data",
                     "practical-alerting/",
                     part="III - Practices",
                     authors=["Jamie Wilkinson"]),
        ChapterInfo(11, "being-on-call", "Being On-Call", "being-on-call/",
                     part="III - Practices",
                     authors=["Andrea Spadaccini"]),
        ChapterInfo(12, "effective-troubleshooting", "Effective Troubleshooting",
                     "effective-troubleshooting/",
                     part="III - Practices",
                     authors=["Chris Jones"]),
        ChapterInfo(13, "emergency-response", "Emergency Response",
                     "emergency-response/",
                     part="III - Practices",
                     authors=["Andrew Stribblehill"]),
        ChapterInfo(14, "managing-incidents", "Managing Incidents",
                     "managing-incidents/",
                     part="III - Practices",
                     authors=["Andrew Stribblehill"]),
        ChapterInfo(15, "postmortem-culture",
                     "Postmortem Culture: Learning from Failure",
                     "postmortem-culture/",
                     part="III - Practices",
                     authors=["John Googler"]),
        ChapterInfo(16, "tracking-outages", "Tracking Outages",
                     "tracking-outages/",
                     part="III - Practices",
                     authors=["Margo Fero"]),
        ChapterInfo(17, "testing-reliability", "Testing for Reliability",
                     "testing-reliability/",
                     part="III - Practices",
                     authors=["Alex Perry", "Max Luebbe"]),
        ChapterInfo(18, "software-engineering-in-sre", "Software Engineering in SRE",
                     "software-engineering-in-sre/",
                     part="III - Practices",
                     authors=["Dave Helstroom", "Trisha Weir", "Evan Leonard", "Kurt Schwehr"]),
        ChapterInfo(19, "load-balancing-frontend",
                     "Load Balancing at the Frontend",
                     "load-balancing-frontend/",
                     part="III - Practices",
                     authors=["Piotr Lewandowski"]),
        ChapterInfo(20, "load-balancing-datacenter",
                     "Load Balancing in the Datacenter",
                     "load-balancing-datacenter/",
                     part="III - Practices",
                     authors=["Alejandro Forero Cuervo"]),
        ChapterInfo(21, "handling-overload", "Handling Overload",
                     "handling-overload/",
                     part="III - Practices",
                     authors=["Alejandro Forero Cuervo"]),
        ChapterInfo(22, "addressing-cascading-failures",
                     "Addressing Cascading Failures",
                     "addressing-cascading-failures/",
                     part="III - Practices",
                     authors=["Mike Ulrich"]),
        ChapterInfo(23, "managing-critical-state",
                     "Managing Critical State: Distributed Consensus for Reliability",
                     "managing-critical-state/",
                     part="III - Practices",
                     authors=["Laura Nolan"]),
        ChapterInfo(24, "distributed-periodic-scheduling",
                     "Distributed Periodic Scheduling with Cron",
                     "distributed-periodic-scheduling/",
                     part="III - Practices",
                     authors=["Stepan Davidovic"]),
        ChapterInfo(25, "data-processing-pipelines", "Data Processing Pipelines",
                     "data-processing-pipelines/",
                     part="III - Practices",
                     authors=["Dan Dennison"]),
        ChapterInfo(26, "data-integrity",
                     "Data Integrity: What You Read Is What You Wrote",
                     "data-integrity/",
                     part="III - Practices",
                     authors=["Raymond Blum", "Rhandeev Singh"]),
        ChapterInfo(27, "reliable-product-launches",
                     "Reliable Product Launches at Scale",
                     "reliable-product-launches/",
                     part="III - Practices",
                     authors=["Laura Nolan"]),
        # Part IV - Management
        ChapterInfo(28, "accelerating-sre-on-call",
                     "Accelerating SREs to On-Call and Beyond",
                     "accelerating-sre-on-call/",
                     part="IV - Management",
                     authors=["Andrew Widdowson"]),
        ChapterInfo(29, "dealing-with-interrupts", "Dealing with Interrupts",
                     "dealing-with-interrupts/",
                     part="IV - Management",
                     authors=["Dave O'Connor"]),
        ChapterInfo(30, "operational-overload",
                     "Embedding an SRE to Recover from Operational Overload",
                     "operational-overload/",
                     part="IV - Management",
                     authors=["Randall Bosetti"]),
        ChapterInfo(31, "communication-and-collaboration",
                     "Communication and Collaboration in SRE",
                     "communication-and-collaboration/",
                     part="IV - Management",
                     authors=["Niall Murphy"]),
        ChapterInfo(32, "evolving-sre-engagement-model",
                     "The Evolving SRE Engagement Model",
                     "evolving-sre-engagement-model/",
                     part="IV - Management",
                     authors=["Acacio Cruz", "Henry L. F. Samuels"]),
        # Part V - Conclusions
        ChapterInfo(33, "lessons-learned",
                     "Lessons Learned from Other Industries",
                     "lessons-learned/",
                     part="V - Conclusions",
                     authors=["Jennifer Petoff"]),
        ChapterInfo(34, "conclusion", "Conclusion", "conclusion/",
                     part="V - Conclusions",
                     authors=["Benjamin Treynor Sloss"]),
        # 부록
        ChapterInfo(0, "availability-table", "Availability Table",
                     "availability-table/",
                     chapter_type="appendix"),
        ChapterInfo(0, "service-best-practices",
                     "A Collection of Best Practices for Production Services",
                     "service-best-practices/",
                     chapter_type="appendix"),
        ChapterInfo(0, "incident-document", "Example Incident State Document",
                     "incident-document/",
                     chapter_type="appendix"),
        ChapterInfo(0, "example-postmortem", "Example Postmortem",
                     "example-postmortem/",
                     chapter_type="appendix"),
        ChapterInfo(0, "launch-checklist", "Launch Coordination Checklist",
                     "launch-checklist/",
                     chapter_type="appendix"),
        ChapterInfo(0, "production-meeting",
                     "Example Production Meeting Minutes",
                     "production-meeting/",
                     chapter_type="appendix"),
    ]
    # 부록에 순서 번호 할당
    appendix_letters = "ABCDEF"
    appendix_idx = 0
    for ch in chapters:
        if ch.chapter_type == "appendix":
            ch.part = f"Appendix {appendix_letters[appendix_idx]}"
            appendix_idx += 1

    return BookConfig(
        key="sre-book",
        title="Site Reliability Engineering",
        base_url="https://sre.google/sre-book/",
        chapters=chapters,
        content_selector="sre-google",  # 특수 처리
    )


def build_workbook_config() -> BookConfig:
    """The Site Reliability Workbook 설정."""
    chapters = [
        # 서문
        ChapterInfo(0, "how-sre-relates", "How SRE Relates to DevOps",
                     "how-sre-relates/",
                     part="Introduction",
                     chapter_type="chapter"),
        # Part I - Foundations
        ChapterInfo(2, "implementing-slos", "Implementing SLOs",
                     "implementing-slos/",
                     part="I - Foundations"),
        ChapterInfo(3, "slo-engineering-case-studies", "SLO Engineering Case Studies",
                     "slo-engineering-case-studies/",
                     part="I - Foundations"),
        ChapterInfo(4, "monitoring", "Monitoring", "monitoring/",
                     part="I - Foundations"),
        ChapterInfo(5, "alerting-on-slos", "Alerting on SLOs",
                     "alerting-on-slos/",
                     part="I - Foundations"),
        ChapterInfo(6, "eliminating-toil", "Eliminating Toil",
                     "eliminating-toil/",
                     part="I - Foundations"),
        ChapterInfo(7, "simplicity", "Simplicity", "simplicity/",
                     part="I - Foundations"),
        # Part II - Practices
        ChapterInfo(8, "on-call", "On-Call", "on-call/",
                     part="II - Practices"),
        ChapterInfo(9, "incident-response", "Incident Response",
                     "incident-response/",
                     part="II - Practices"),
        ChapterInfo(10, "postmortem-culture",
                     "Postmortem Culture: Learning from Failure",
                     "postmortem-culture/",
                     part="II - Practices"),
        ChapterInfo(11, "managing-load", "Managing Load", "managing-load/",
                     part="II - Practices"),
        ChapterInfo(12, "non-abstract-design",
                     "Introducing Non-Abstract Large System Design",
                     "non-abstract-design/",
                     part="II - Practices"),
        ChapterInfo(13, "data-processing", "Data Processing Pipelines",
                     "data-processing/",
                     part="II - Practices"),
        ChapterInfo(14, "configuration-design",
                     "Configuration Design and Best Practices",
                     "configuration-design/",
                     part="II - Practices"),
        ChapterInfo(15, "configuration-specifics", "Configuration Specifics",
                     "configuration-specifics/",
                     part="II - Practices"),
        ChapterInfo(16, "canarying-releases", "Canarying Releases",
                     "canarying-releases/",
                     part="II - Practices"),
        # Part III - Processes
        ChapterInfo(17, "overload",
                     "Identifying and Recovering from Overload",
                     "overload/",
                     part="III - Processes"),
        ChapterInfo(18, "engagement-model", "SRE Engagement Model",
                     "engagement-model/",
                     part="III - Processes"),
        ChapterInfo(19, "reaching-beyond",
                     "SRE: Reaching Beyond Your Walls",
                     "reaching-beyond/",
                     part="III - Processes"),
        ChapterInfo(20, "team-lifecycles", "SRE Team Lifecycles",
                     "team-lifecycles/",
                     part="III - Processes"),
        ChapterInfo(21, "organizational-change",
                     "Organizational Change Management in SRE",
                     "organizational-change/",
                     part="III - Processes"),
        # 부록
        ChapterInfo(0, "conclusion", "Conclusion", "conclusion/",
                     chapter_type="conclusion"),
        ChapterInfo(0, "slo-document", "Example SLO Document",
                     "slo-document/",
                     chapter_type="appendix",
                     part="Appendix A"),
        ChapterInfo(0, "error-budget-policy", "Example Error Budget Policy",
                     "error-budget-policy/",
                     chapter_type="appendix",
                     part="Appendix B"),
        ChapterInfo(0, "postmortem-analysis",
                     "Results of Postmortem Analysis",
                     "postmortem-analysis/",
                     chapter_type="appendix",
                     part="Appendix C"),
    ]
    # ch01 번호 재설정
    chapters[0].number = 1
    return BookConfig(
        key="workbook",
        title="The Site Reliability Workbook",
        base_url="https://sre.google/workbook/",
        chapters=chapters,
        content_selector="workbook",  # 특수 처리
    )


def build_bsrs_config() -> BookConfig:
    """Building Secure & Reliable Systems 설정."""
    chapters = [
        # Part I
        ChapterInfo(1, "intersection-security-reliability",
                     "The Intersection of Security and Reliability",
                     "ch01.html",
                     part="I - Introductory Material"),
        ChapterInfo(2, "understanding-adversaries",
                     "Understanding Adversaries",
                     "ch02.html",
                     part="I - Introductory Material"),
        # Part II - Designing Systems
        ChapterInfo(3, "safe-proxies", "Case Study: Safe Proxies",
                     "ch03.html",
                     part="II - Designing Systems"),
        ChapterInfo(4, "design-tradeoffs", "Design Tradeoffs",
                     "ch04.html",
                     part="II - Designing Systems"),
        ChapterInfo(5, "design-least-privilege",
                     "Design for Least Privilege",
                     "ch05.html",
                     part="II - Designing Systems"),
        ChapterInfo(6, "design-understandability",
                     "Design for Understandability",
                     "ch06.html",
                     part="II - Designing Systems"),
        ChapterInfo(7, "design-changing-landscape",
                     "Design for a Changing Landscape",
                     "ch07.html",
                     part="II - Designing Systems"),
        ChapterInfo(8, "design-resilience", "Design for Resilience",
                     "ch08.html",
                     part="II - Designing Systems"),
        ChapterInfo(9, "design-recovery", "Design for Recovery",
                     "ch09.html",
                     part="II - Designing Systems"),
        ChapterInfo(10, "mitigating-dos",
                     "Mitigating Denial-of-Service Attacks",
                     "ch10.html",
                     part="II - Designing Systems"),
        # Part III - Implementing Systems
        ChapterInfo(11, "publicly-trusted-ca",
                     "Case Study: Designing, Implementing, and Maintaining a Publicly Trusted CA",
                     "ch11.html",
                     part="III - Implementing Systems"),
        ChapterInfo(12, "writing-code", "Writing Code",
                     "ch12.html",
                     part="III - Implementing Systems"),
        ChapterInfo(13, "testing-code", "Testing Code",
                     "ch13.html",
                     part="III - Implementing Systems"),
        ChapterInfo(14, "deploying-code", "Deploying Code",
                     "ch14.html",
                     part="III - Implementing Systems"),
        ChapterInfo(15, "investigating-systems", "Investigating Systems",
                     "ch15.html",
                     part="III - Implementing Systems"),
        # Part IV - Maintaining Systems
        ChapterInfo(16, "disaster-planning", "Disaster Planning",
                     "ch16.html",
                     part="IV - Maintaining Systems"),
        ChapterInfo(17, "crisis-management", "Crisis Management",
                     "ch17.html",
                     part="IV - Maintaining Systems"),
        ChapterInfo(18, "recovery-aftermath", "Recovery and Aftermath",
                     "ch18.html",
                     part="IV - Maintaining Systems"),
        # Part V - Organization and Culture
        ChapterInfo(19, "chrome-security",
                     "Case Study: Chrome Security Team",
                     "ch19.html",
                     part="V - Organization and Culture"),
        ChapterInfo(20, "roles-responsibilities",
                     "Understanding Roles and Responsibilities",
                     "ch20.html",
                     part="V - Organization and Culture"),
        ChapterInfo(21, "culture",
                     "Building a Culture of Security and Reliability",
                     "ch21.html",
                     part="V - Organization and Culture"),
        # 기타
        ChapterInfo(0, "conclusion", "Conclusion",
                     "ch22.html",
                     chapter_type="conclusion"),
        ChapterInfo(0, "disaster-risk-matrix",
                     "A Disaster Risk Assessment Matrix",
                     "appa.html",
                     chapter_type="appendix",
                     part="Appendix A"),
    ]
    return BookConfig(
        key="bsrs",
        title="Building Secure and Reliable Systems",
        base_url="https://google.github.io/building-secure-and-reliable-systems/raw/",
        chapters=chapters,
        content_selector="bsrs",  # 특수 처리
    )


ALL_BOOKS = {
    "sre-book": build_sre_book_config,
    "workbook": build_workbook_config,
    "bsrs": build_bsrs_config,
}


# ─── HTTP 클라이언트 ──────────────────────────────────────────────────


class HttpClient:
    """재시도 및 rate limiting이 포함된 HTTP 클라이언트."""

    def __init__(self, delay: float = REQUEST_DELAY):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.delay = delay
        self._last_request_time = 0.0

    def _wait(self):
        """요청 간 지연."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

    def get(self, url: str, binary: bool = False) -> Optional[bytes | str]:
        """URL에서 콘텐츠를 가져옵니다. 실패 시 None 반환."""
        for attempt in range(MAX_RETRIES):
            self._wait()
            try:
                r = self.session.get(url, timeout=REQUEST_TIMEOUT)
                self._last_request_time = time.time()

                if r.status_code == 429:
                    wait_time = RETRY_BACKOFF ** (attempt + 2)
                    print(f"  ⚠ Rate limited, {wait_time:.0f}초 대기...")
                    time.sleep(wait_time)
                    continue

                r.raise_for_status()
                if binary:
                    return r.content
                # UTF-8 강제 설정 (requests가 ISO-8859-1로 잘못 감지하는 경우 방지)
                r.encoding = "utf-8"
                return r.text

            except requests.RequestException as e:
                wait_time = RETRY_BACKOFF ** (attempt + 1)
                print(f"  ⚠ 요청 실패 (시도 {attempt + 1}/{MAX_RETRIES}): {e}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(wait_time)

        print(f"  ✗ 최종 실패: {url}")
        return None


# ─── 콘텐츠 추출기 ────────────────────────────────────────────────────


class ContentExtractor:
    """HTML에서 본문 콘텐츠를 추출합니다."""

    @staticmethod
    def extract_sre_google(html: str) -> Optional[Tag]:
        """SRE Book / Workbook에서 콘텐츠를 추출합니다.

        구조: div#content 안에 콘텐츠가 있음.
        SRE Book: div#content > section[data-type=chapter]
        Workbook: div#content 에 직접 h1, p 등이 있음
        """
        soup = BeautifulSoup(html, "html.parser")
        content_div = soup.find("div", id="content")
        if not content_div:
            return None

        # 불필요한 요소 제거
        for tag in content_div.find_all(["script", "style", "nav"]):
            tag.decompose()

        # overlay 내부의 nav/toc 제거
        overlay = soup.find("div", id="overlay-element")
        if overlay:
            overlay.decompose()

        # 네비게이션 링크 제거 (이전/다음 챕터)
        for nav_div in content_div.find_all("div", class_="nav-next"):
            nav_div.decompose()
        for nav_div in content_div.find_all("div", class_="nav-prev"):
            nav_div.decompose()

        return content_div

    @staticmethod
    def extract_bsrs(html: str) -> Optional[Tag]:
        """BSRS에서 콘텐츠를 추출합니다.

        구조: body[data-type=book] > section[data-type=chapter]
        """
        soup = BeautifulSoup(html, "html.parser")

        # chapter section 찾기
        chapter = soup.find("section", attrs={"data-type": "chapter"})
        if not chapter:
            # appendix 등은 다른 구조일 수 있음
            chapter = soup.find("section", attrs={"data-type": "appendix"})
        if not chapter:
            # body 전체에서 콘텐츠 추출
            chapter = soup.find("body")
        if not chapter:
            return None

        # indexterm 제거
        for idx in chapter.find_all("a", attrs={"data-type": "indexterm"}):
            idx.decompose()

        # 불필요한 요소 제거
        for tag in chapter.find_all(["script", "style"]):
            tag.decompose()

        # 챕터 번호 헤더 제거 (예: <h2>Chapter 1</h2> - body 직접 자식)
        body = soup.find("body")
        if body:
            for h2 in body.find_all("h2", recursive=False):
                text = h2.get_text().strip()
                if re.match(r"^Chapter \d+$", text) or text in ("Appendix A", "Conclusion"):
                    h2.decompose()

        return chapter

    @staticmethod
    def extract(book_key: str, html: str) -> Optional[Tag]:
        """책 타입에 따라 적절한 추출기를 선택합니다."""
        if book_key in ("sre-book", "workbook"):
            return ContentExtractor.extract_sre_google(html)
        elif book_key == "bsrs":
            return ContentExtractor.extract_bsrs(html)
        return None


# ─── HTML 전처리기 ────────────────────────────────────────────────────


class HtmlPreprocessor:
    """pandoc 변환 전에 HTML을 정리합니다."""

    @staticmethod
    def process(content: Tag, book_key: str) -> str:
        """콘텐츠 태그를 정리하여 HTML 문자열을 반환합니다."""
        content = HtmlPreprocessor._process_sidebars(content)
        content = HtmlPreprocessor._process_figures(content)
        content = HtmlPreprocessor._process_footnotes(content, book_key)
        content = HtmlPreprocessor._fix_heading_levels(content, book_key)
        content = HtmlPreprocessor._process_tables(content)
        content = HtmlPreprocessor._unwrap_tags(content)
        # 최상위 태그의 내부 HTML만 반환 (래퍼 태그 제외)
        return content.decode_contents()

    @staticmethod
    def _process_sidebars(content: Tag) -> Tag:
        """sidebar/aside를 blockquote로 변환합니다."""
        for aside in content.find_all("aside"):
            # sidebar 제목 추출
            title_tag = aside.find(["h1", "h2", "h3", "h4", "h5", "h6"])
            title_text = ""
            if title_tag:
                title_text = title_tag.get_text().strip()
                title_tag.decompose()

            # blockquote로 변환
            blockquote = content.find_all("aside")  # 참조용
            aside.name = "blockquote"
            if title_text:
                # 제목을 bold로 blockquote 앞에 삽입
                title_p = BeautifulSoup(
                    f'<p><strong>{title_text}</strong></p>',
                    "html.parser"
                )
                aside.insert(0, title_p)
        return content

    @staticmethod
    def _process_figures(content: Tag) -> Tag:
        """figure 태그를 이미지+캡션으로 변환합니다."""
        for figure in content.find_all("figure"):
            img = figure.find("img")
            figcaption = figure.find("figcaption")

            if img and figcaption:
                caption_text = figcaption.get_text().strip()
                # label span 제거하고 캡션 텍스트만 유지
                img["alt"] = caption_text

            # figcaption을 이탤릭 텍스트로 변환
            if figcaption:
                figcaption.name = "p"
                figcaption.string = f"*{figcaption.get_text().strip()}*"

        return content

    @staticmethod
    def _process_footnotes(content: Tag, book_key: str) -> Tag:
        """각주를 처리합니다."""
        if book_key in ("sre-book", "workbook"):
            # data-type="footnote" 처리
            for fn in content.find_all(attrs={"data-type": "footnote"}):
                # footnote ID 추출
                fn_id = fn.get("id", "")
                # 각주 내용을 [^N]: 형태로 변환하기 위해 마커 추가
                sup = fn.find("sup")
                if sup:
                    fn_num = sup.get_text().strip()
                    sup.decompose()
                    # 각주를 별도 단락으로
                    fn.name = "p"
                    fn_text = fn.get_text().strip()
                    fn.string = f"[^{fn_num}]: {fn_text}"

            # 각주 참조 마커 변환
            for marker in content.find_all("a", class_="jumptargets"):
                href = marker.get("href", "")
                if href.endswith("-marker"):
                    fn_num = marker.get_text().strip()
                    # sup 부모를 [^N]로 변환
                    parent_sup = marker.find_parent("sup")
                    if parent_sup:
                        parent_sup.replace_with(f"[^{fn_num}]")

        return content

    @staticmethod
    def _fix_heading_levels(content: Tag, book_key: str) -> Tag:
        """헤딩 수준을 재매핑합니다.

        SRE Book: section[data-type=chapter] 내부에서
          h2 (chapter title) -> h1
          h1 (sect1) -> h2
          h2 (sect2) -> h3

        Workbook: div#content 내부에서
          h1 -> h1 (유지)
          h2 -> h2 (유지)
          h5 -> h3 (재매핑)

        BSRS: section[data-type=chapter] 내부에서
          h1 (chapter title / sect1) -> h1/h2
          h2 (sect2) -> h3
        """
        if book_key == "sre-book":
            # sect2 h2 -> h3 먼저 (충돌 방지)
            for section in content.find_all("section", attrs={"data-type": "sect2"}):
                for h in section.find_all("h2", recursive=False):
                    h.name = "h3"

            # sect1 h1 -> h2
            for section in content.find_all("section", attrs={"data-type": "sect1"}):
                for h in section.find_all("h1", recursive=False):
                    h.name = "h2"

            # chapter title h2 -> h1
            chapter = content.find("section", attrs={"data-type": "chapter"})
            if chapter:
                title_h2 = chapter.find("h2", recursive=False)
                if title_h2:
                    title_h2.name = "h1"

        elif book_key == "workbook":
            # h5 -> h3
            for h5 in content.find_all("h5"):
                h5.name = "h3"

        elif book_key == "bsrs":
            # BSRS: content 자체가 section[data-type="chapter"]이므로 직접 탐색
            # sect2 h2 -> h3 먼저 (충돌 방지)
            for section in content.find_all("section", attrs={"data-type": "sect2"}):
                for h in section.find_all("h2", recursive=False):
                    h.name = "h3"

            # sect1 h1 -> h2
            for section in content.find_all("section", attrs={"data-type": "sect1"}):
                for h in section.find_all("h1", recursive=False):
                    h.name = "h2"

        return content

    @staticmethod
    def _process_tables(content: Tag) -> Tag:
        """테이블을 정리합니다."""
        # 불필요한 테이블 속성 제거
        for table in content.find_all("table"):
            for attr in ["width", "border", "cellpadding", "cellspacing", "style"]:
                if attr in table.attrs:
                    del table.attrs[attr]
        return content

    @staticmethod
    def _unwrap_tags(content: Tag) -> Tag:
        """pandoc이 처리하지 못하는 HTML 태그를 제거/언래핑합니다.

        div, section, span, figure 등의 래퍼 태그를 제거하고 내부 콘텐츠만 유지합니다.
        """
        # span 태그 언래핑 (keep-together 등)
        for span in content.find_all("span"):
            span.unwrap()

        # figure 태그 언래핑 (이미지 + 캡션)
        for figure in content.find_all("figure"):
            figure.unwrap()

        # section 태그 언래핑 (data-type 등)
        for section in content.find_all("section"):
            section.unwrap()

        # div 태그 언래핑 (content wrapper, nav 등)
        for div in content.find_all("div"):
            div.unwrap()

        # <a> 태그에서 불필요한 속성 제거 (pandoc이 raw HTML로 처리하는 것 방지)
        for a_tag in content.find_all("a"):
            for attr in ["rel", "target", "class", "data-type", "id",
                         "contenteditable", "data-primary"]:
                if attr in a_tag.attrs:
                    del a_tag.attrs[attr]

        # img 태그에서 불필요한 속성 제거
        for img in content.find_all("img"):
            allowed = {"src", "alt"}
            attrs_to_remove = [k for k in img.attrs if k not in allowed]
            for attr in attrs_to_remove:
                del img.attrs[attr]

        # sup > a.jumptargets 구조에서 남은 각주 참조를 텍스트로 변환
        for sup in content.find_all("sup"):
            a_tag = sup.find("a")
            if a_tag:
                fn_num = a_tag.get_text().strip()
                sup.replace_with(f"[^{fn_num}]")

        return content


# ─── Markdown 변환기 ──────────────────────────────────────────────────


class MarkdownConverter:
    """pandoc을 사용하여 HTML을 GFM Markdown으로 변환합니다."""

    @staticmethod
    def convert(html: str) -> Optional[str]:
        """HTML 문자열을 GFM Markdown으로 변환합니다."""
        try:
            result = subprocess.run(
                [
                    "pandoc",
                    "--from=html",
                    "--to=gfm",
                    "--wrap=none",
                    "--markdown-headings=atx",
                ],
                input=html,
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode != 0:
                print(f"  ⚠ pandoc 경고: {result.stderr[:200]}")
            return result.stdout
        except subprocess.TimeoutExpired:
            print("  ✗ pandoc 타임아웃")
            return None
        except FileNotFoundError:
            print("  ✗ pandoc을 찾을 수 없습니다. 설치해 주세요.")
            sys.exit(1)


# ─── Markdown 후처리기 ────────────────────────────────────────────────


class MarkdownPostprocessor:
    """변환된 Markdown을 정리합니다."""

    @staticmethod
    def process(md: str) -> str:
        """Markdown 텍스트를 후처리합니다."""
        # 연속 빈 줄 정리 (3개 이상 → 2개)
        md = re.sub(r"\n{3,}", "\n\n", md)

        # HTML 엔티티 정리
        md = md.replace("&amp;", "&")
        md = md.replace("&lt;", "<")
        md = md.replace("&gt;", ">")

        # 불필요한 escape 제거
        md = re.sub(r"\\([#*_`\[\]()])", r"\1", md)

        # 마지막 줄바꿈 보장
        if not md.endswith("\n"):
            md += "\n"

        return md


# ─── 이미지 다운로더 ──────────────────────────────────────────────────


class ImageDownloader:
    """이미지를 다운로드하고 Markdown 내 경로를 재작성합니다."""

    def __init__(self, client: HttpClient, images_dir: Path):
        self.client = client
        self.images_dir = images_dir
        self.downloaded: dict[str, str] = {}  # 원본URL -> 로컬 파일명

    def process_html_images(self, content: Tag, base_url: str,
                            book_key: str) -> Tag:
        """HTML 내 이미지를 다운로드하고 src를 로컬 경로로 변경합니다."""
        for img in content.find_all("img"):
            src = img.get("src", "")
            if not src:
                continue

            # Google 로고 등 불필요한 이미지 건너뛰기
            alt = img.get("alt", "")
            if alt == "Google" or "googleusercontent" in src and "logo" in src.lower():
                # 로고 이미지는 제거
                parent = img.parent
                if parent and parent.name == "a":
                    parent.decompose()
                else:
                    img.decompose()
                continue

            # 절대 URL 생성
            abs_url = urljoin(base_url, src)

            # 파일명 결정
            local_name = self._get_local_filename(abs_url, src, book_key)

            # 다운로드
            if abs_url not in self.downloaded:
                self._download_image(abs_url, local_name)
                self.downloaded[abs_url] = local_name

            # src를 로컬 경로로 변경
            img["src"] = f"images/{self.downloaded[abs_url]}"

        return content

    def rewrite_markdown_paths(self, md: str) -> str:
        """Markdown 내 이미지 경로를 로컬 경로로 재작성합니다.

        이미 HTML 단계에서 처리되었으므로 이 메서드는 보조적입니다.
        """
        return md

    def _get_local_filename(self, url: str, original_src: str,
                            book_key: str) -> str:
        """이미지의 로컬 파일명을 결정합니다."""
        if book_key == "bsrs":
            # BSRS는 이미 의미 있는 파일명을 가짐 (예: bsrs_0101.png)
            return os.path.basename(original_src)

        # googleusercontent URL의 경우 해시 기반 파일명 생성
        parsed = urlparse(url)
        path_parts = parsed.path.strip("/").split("/")

        # URL 해시로 고유 파일명 생성
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        ext = self._guess_extension(url)
        return f"{book_key}_{url_hash}{ext}"

    def _guess_extension(self, url: str) -> str:
        """URL에서 파일 확장자를 추측합니다."""
        parsed = urlparse(url)
        path = parsed.path.lower()
        for ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
            if path.endswith(ext):
                return ext
        # googleusercontent는 확장자가 없으므로 .png 기본값
        return ".png"

    def _download_image(self, url: str, filename: str):
        """이미지를 다운로드합니다."""
        filepath = self.images_dir / filename
        if filepath.exists():
            return

        data = self.client.get(url, binary=True)
        if data:
            filepath.write_bytes(data)
            print(f"    📷 {filename}")


# ─── 진행 상태 추적기 ─────────────────────────────────────────────────


class ProgressTracker:
    """JSON 체크포인트로 진행 상태를 추적합니다."""

    def __init__(self, book_dir: Path):
        self.checkpoint_file = book_dir / "_progress.json"
        self.state: dict = self._load()

    def _load(self) -> dict:
        """체크포인트 파일을 로드합니다."""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file) as f:
                return json.load(f)
        return {"completed": [], "failed": []}

    def save(self):
        """체크포인트를 저장합니다."""
        with open(self.checkpoint_file, "w") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def is_completed(self, slug: str) -> bool:
        """챕터가 이미 완료되었는지 확인합니다."""
        return slug in self.state["completed"]

    def mark_completed(self, slug: str):
        """챕터를 완료로 표시합니다."""
        if slug not in self.state["completed"]:
            self.state["completed"].append(slug)
        self.save()

    def mark_failed(self, slug: str, error: str):
        """챕터를 실패로 표시합니다."""
        self.state["failed"].append({"slug": slug, "error": error})
        self.save()


# ─── 메인 다운로더 ────────────────────────────────────────────────────


class SREBookDownloader:
    """SRE 책 다운로드 및 변환 메인 클래스."""

    def __init__(self, delay: float = REQUEST_DELAY, resume: bool = False):
        self.client = HttpClient(delay=delay)
        self.resume = resume

    def download_book(self, book_config: BookConfig,
                      chapter_slug: Optional[str] = None):
        """한 권의 책을 다운로드합니다."""
        book_dir = BASE_DIR / book_config.key
        book_dir.mkdir(parents=True, exist_ok=True)
        images_dir = book_dir / "images"
        images_dir.mkdir(exist_ok=True)

        tracker = ProgressTracker(book_dir)
        image_downloader = ImageDownloader(self.client, images_dir)

        chapters = book_config.chapters
        if chapter_slug:
            chapters = [c for c in chapters if c.slug == chapter_slug]
            if not chapters:
                print(f"✗ 챕터 '{chapter_slug}'을(를) 찾을 수 없습니다.")
                return

        print(f"\n📚 {book_config.title}")
        print(f"   챕터 수: {len(chapters)}")
        print(f"   출력 디렉토리: {book_dir}")
        print()

        completed = 0
        failed = 0

        for ch in chapters:
            # 재실행 시 건너뛰기
            if self.resume and tracker.is_completed(ch.slug):
                print(f"  ⏭ {self._format_filename(ch)} (이미 완료)")
                completed += 1
                continue

            print(f"  📖 {ch.title}...")

            try:
                success = self._process_chapter(
                    book_config, ch, book_dir, image_downloader
                )
                if success:
                    tracker.mark_completed(ch.slug)
                    completed += 1
                    print(f"    ✓ 완료")
                else:
                    tracker.mark_failed(ch.slug, "처리 실패")
                    failed += 1
            except Exception as e:
                print(f"    ✗ 오류: {e}")
                tracker.mark_failed(ch.slug, str(e))
                failed += 1

        # 메타데이터 저장
        self._save_metadata(book_config, book_dir)

        print(f"\n  📊 결과: {completed} 완료, {failed} 실패")

    def _process_chapter(self, config: BookConfig, chapter: ChapterInfo,
                         book_dir: Path,
                         image_downloader: ImageDownloader) -> bool:
        """단일 챕터를 처리합니다."""
        # 1. HTML 가져오기
        url = config.base_url + chapter.url_path
        html = self.client.get(url)
        if not html:
            return False

        # 2. 콘텐츠 추출
        content = ContentExtractor.extract(config.key, html)
        if not content:
            print(f"    ⚠ 콘텐츠를 추출할 수 없습니다")
            return False

        # 3. 이미지 다운로드 및 경로 재작성
        content = image_downloader.process_html_images(
            content, url, config.key
        )

        # 4. HTML 전처리
        processed_html = HtmlPreprocessor.process(content, config.key)

        # 5. pandoc으로 Markdown 변환
        markdown = MarkdownConverter.convert(processed_html)
        if not markdown:
            return False

        # 6. 후처리
        markdown = MarkdownPostprocessor.process(markdown)

        # 7. YAML frontmatter 추가
        frontmatter = self._build_frontmatter(config, chapter, url)
        final_md = frontmatter + markdown

        # 8. 파일 저장
        filename = self._format_filename(chapter)
        filepath = book_dir / filename
        filepath.write_text(final_md, encoding="utf-8")

        return True

    def _build_frontmatter(self, config: BookConfig,
                           chapter: ChapterInfo, source_url: str) -> str:
        """YAML frontmatter를 생성합니다."""
        lines = ["---"]
        lines.append(f'title: "{chapter.title}"')
        lines.append(f'book: "{config.title}"')

        if chapter.number > 0:
            lines.append(f"chapter: {chapter.number}")

        if chapter.part:
            lines.append(f'part: "{chapter.part}"')

        if chapter.authors:
            authors_str = json.dumps(chapter.authors, ensure_ascii=False)
            lines.append(f"authors: {authors_str}")

        if chapter.chapter_type != "chapter":
            lines.append(f'type: "{chapter.chapter_type}"')

        lines.append(f'source_url: "{source_url}"')
        lines.append("---\n\n")
        return "\n".join(lines)

    def _format_filename(self, chapter: ChapterInfo) -> str:
        """챕터 파일명을 생성합니다."""
        if chapter.chapter_type == "appendix":
            # 부록: appendix_a_slug.md
            letter = ""
            if chapter.part:
                match = re.search(r"Appendix ([A-Z])", chapter.part)
                if match:
                    letter = match.group(1).lower()
            return f"appendix_{letter}_{chapter.slug}.md"
        elif chapter.chapter_type in ("foreword", "preface", "conclusion"):
            return f"{chapter.chapter_type}_{chapter.slug}.md"
        elif chapter.number > 0:
            return f"ch{chapter.number:02d}_{chapter.slug}.md"
        else:
            # 번호 없는 챕터 (workbook ch01 등은 number 재설정됨)
            return f"{chapter.chapter_type}_{chapter.slug}.md"

    def _save_metadata(self, config: BookConfig, book_dir: Path):
        """책 메타데이터를 JSON으로 저장합니다."""
        metadata = {
            "title": config.title,
            "base_url": config.base_url,
            "chapters": [],
        }

        current_part = ""
        for ch in config.chapters:
            entry = {
                "number": ch.number,
                "title": ch.title,
                "slug": ch.slug,
                "file": self._format_filename(ch),
                "type": ch.chapter_type,
            }
            if ch.part:
                entry["part"] = ch.part
            if ch.authors:
                entry["authors"] = ch.authors
            metadata["chapters"].append(entry)

        filepath = book_dir / "_metadata.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)


# ─── 검증기 ──────────────────────────────────────────────────────────


class Verifier:
    """다운로드 결과를 검증합니다."""

    @staticmethod
    def verify():
        """모든 책의 다운로드 결과를 검증합니다."""
        print("\n🔍 검증 중...\n")
        all_ok = True

        for book_key, build_fn in ALL_BOOKS.items():
            config = build_fn()
            book_dir = BASE_DIR / book_key

            if not book_dir.exists():
                print(f"  ✗ {config.title}: 디렉토리 없음")
                all_ok = False
                continue

            md_files = list(book_dir.glob("*.md"))
            expected = len(config.chapters)

            print(f"  📚 {config.title}")
            print(f"     파일: {len(md_files)}/{expected}")

            # 누락된 챕터 확인
            existing_files = {f.name for f in md_files}
            for ch in config.chapters:
                fname = SREBookDownloader(delay=0)._format_filename(ch)
                if fname not in existing_files:
                    print(f"     ✗ 누락: {fname}")
                    all_ok = False

            # 비정상적으로 짧은 파일 검출
            for f in md_files:
                size = f.stat().st_size
                if size < 500:
                    print(f"     ⚠ 너무 짧음 ({size}B): {f.name}")

            # 이미지 참조 무결성
            images_dir = book_dir / "images"
            broken_refs = 0
            for f in md_files:
                content = f.read_text(encoding="utf-8")
                for match in re.finditer(r"!\[.*?\]\((images/[^)]+)\)", content):
                    img_path = book_dir / match.group(1)
                    if not img_path.exists():
                        broken_refs += 1
                        if broken_refs <= 3:
                            print(f"     ⚠ 깨진 이미지 참조: {match.group(1)} in {f.name}")

            if broken_refs > 3:
                print(f"     ⚠ 깨진 이미지 참조 총 {broken_refs}건")

            image_count = len(list(images_dir.glob("*"))) if images_dir.exists() else 0
            print(f"     이미지: {image_count}개")
            print()

        if all_ok:
            print("  ✓ 검증 통과!")
        else:
            print("  ⚠ 일부 항목에 문제가 있습니다.")


# ─── CLI ──────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Google SRE 3권 다운로드 및 Markdown 변환"
    )
    parser.add_argument(
        "--book",
        choices=["sre-book", "workbook", "bsrs", "all"],
        default="all",
        help="다운로드할 책 (기본: all)",
    )
    parser.add_argument(
        "--chapter",
        help="특정 챕터만 다운로드 (slug 지정, 예: introduction)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=REQUEST_DELAY,
        help=f"요청 간 지연(초) (기본: {REQUEST_DELAY})",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="이전 진행 상태에서 이어서 다운로드",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="다운로드 결과 검증만 수행",
    )

    args = parser.parse_args()

    if args.verify:
        Verifier.verify()
        return

    downloader = SREBookDownloader(delay=args.delay, resume=args.resume)

    if args.book == "all":
        for book_key, build_fn in ALL_BOOKS.items():
            config = build_fn()
            downloader.download_book(config, args.chapter)
    else:
        config = ALL_BOOKS[args.book]()
        downloader.download_book(config, args.chapter)

    print("\n✅ 다운로드 완료!")
    print("\n검증하려면: python3 scripts/download_sre_books.py --verify")


if __name__ == "__main__":
    main()
