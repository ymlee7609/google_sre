---
name: sre-knowledge
description: >
  Google SRE 3권(SRE Book, Workbook, BSRS) 기반 지식 질의 및 조언 스킬.
  SRE 원칙, 사례, 보안/신뢰성 설계 패턴에 대해 근거 기반 답변을 제공합니다.
user-invocable: true
allowed-tools: Read, Grep, Glob
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-03-09"
  tags: "sre, reliability, monitoring, incident, toil, slo, security"
  aliases: "sre, google-sre"
  argument-hint: "SRE 관련 질문 또는 조언 요청"
---

# SRE Knowledge Skill

Google SRE 3권의 콘텐츠를 기반으로 SRE 관련 질문에 근거 기반 답변을 제공합니다.

## Source Documents

3권의 문서가 `docs/` 디렉토리에 Markdown 형태로 존재합니다:

| 약칭 | 정식명 | 경로 | 챕터 수 |
|------|--------|------|---------|
| SRE Book | Site Reliability Engineering | `docs/sre-book/` | 34 + 부록 6 |
| Workbook | The Site Reliability Workbook | `docs/workbook/` | 21 + 부록 3 |
| BSRS | Building Secure and Reliable Systems | `docs/bsrs/` | 21 + 부록 1 |

## Topic Quick Reference

| 주제 | SRE Book | Workbook | BSRS |
|------|----------|----------|------|
| SLO/SLI/SLA | ch03, ch04 | ch02, ch03, ch05 | - |
| Monitoring/Alerting | ch06, ch10 | ch04, ch05 | ch15 |
| Incident Management | ch13, ch14 | ch09 | ch17, ch18 |
| Postmortem | ch15 | ch10 | ch18 |
| Toil | ch05 | ch06 | - |
| On-Call | ch11, ch28, ch29 | ch08 | - |
| Load Balancing/Overload | ch19, ch20, ch21, ch22 | ch11, ch17 | ch10 |
| Release/Deploy | ch08 | ch16 | ch14 |
| Testing/Reliability | ch17 | - | ch13 |
| Automation | ch07 | - | - |
| Simplicity | ch09 | ch07 | ch06 |
| Security | - | - | ch01-ch21 |
| Data Integrity | ch26 | ch13 | - |
| Configuration | - | ch14, ch15 | - |
| Organizational | ch30, ch31, ch32 | ch18, ch19, ch20, ch21 | ch20, ch21 |
| Troubleshooting | ch12 | - | ch15 |
| Disaster/Recovery | - | - | ch08, ch09, ch16 |

상세 매핑은 `references/topic-index.md`를 참조하세요.

## Query Workflow

사용자 질문을 받으면 다음 절차를 따릅니다:

### Step 1: 주제 식별

사용자 질문에서 핵심 주제를 식별합니다. 위 Quick Reference 테이블 또는 `references/topic-index.md`를 참조하여 관련 챕터를 특정합니다.

### Step 2: 콘텐츠 검색

Grep 도구로 `docs/` 디렉토리에서 관련 키워드를 검색합니다:

- 특정 챕터가 확인된 경우: 해당 파일을 직접 Read
- 주제가 불명확한 경우: Grep으로 키워드 검색 후 관련 파일 특정
- 여러 책에 걸친 주제: 각 책의 관련 챕터를 병렬로 검색

### Step 3: 근거 기반 답변

답변에 반드시 출처를 포함합니다:

- 형식: `[SRE Book ch04]`, `[Workbook ch02]`, `[BSRS ch10]`
- 핵심 인용이나 원칙은 원문에서 직접 인용
- 여러 책의 관점을 종합하여 포괄적 답변 구성

### Step 4: 실무 적용 (조언 모드)

사용자가 특정 상황에 대한 조언을 요청한 경우:

- SRE 원칙을 사용자의 상황에 맞게 적용
- Google의 사례와 비교하여 권고사항 제시
- 관련 체크리스트나 프레임워크가 있으면 함께 제공

## File Naming Convention

문서 파일명 패턴: `ch{번호}_{slug}.md`

- SRE Book: `docs/sre-book/ch01_introduction.md` ~ `ch34_conclusion.md`
- Workbook: `docs/workbook/ch01_how-sre-relates.md` ~ `ch21_organizational-change.md`
- BSRS: `docs/bsrs/ch01_intersection-security-reliability.md` ~ `ch21_culture.md`
- 부록: `appendix_{letter}_{slug}.md`
- 결론: `conclusion_conclusion.md`

## Response Guidelines

- 답변 언어: 사용자의 conversation_language를 따릅니다
- 출처 표기: 모든 주장에 `[책명 ch번호]` 형태의 출처를 포함합니다
- 복수 출처: 같은 주제를 다루는 여러 챕터가 있으면 모두 참조합니다
- 실무 조언: 원칙만 나열하지 말고 구체적인 적용 방법을 함께 제시합니다
- 한계 인식: 문서에 없는 내용은 "SRE 3권에서는 이 주제를 직접 다루지 않습니다"라고 명시합니다
