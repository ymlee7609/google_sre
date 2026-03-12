# Google SRE 3권 Knowledge Base

Google의 SRE(Site Reliability Engineering) 공개 서적 3권을 Markdown으로 변환하고, 학습 교재, 교차 참조 가이드, PPTX 슬라이드를 포함한 종합 지식 베이스입니다.

**[English README](README.md)**

## 포함 서적

| 서적 | 경로 | 파일 수 | 원본 |
|------|------|---------|------|
| Site Reliability Engineering | `docs/sre-book/` | 44 | [sre.google/sre-book](https://sre.google/sre-book/table-of-contents/) |
| The Site Reliability Workbook | `docs/workbook/` | 29 | [sre.google/workbook](https://sre.google/workbook/table-of-contents/) |
| Building Secure & Reliable Systems | `docs/bsrs/` | 27 | [sre.google/books](https://sre.google/books/) |

총 **100개** Markdown 파일 (76 챕터 + 부록 + 결론 + 요약)

## 프로젝트 구조

```
google_sre/
├── docs/
│   ├── sre-book/           # SRE Book (Ch01-34, 부록 A-F, 요약)
│   │   └── summaries/      # 챕터별 한국어 요약 (40개 파일)
│   ├── workbook/           # Workbook (Ch01-21, 부록 A-C, 결론)
│   └── bsrs/               # BSRS (Ch01-21, 부록 A, 결론)
├── scripts/
│   ├── download_sre_books.py       # 다운로드 및 Markdown 변환
│   ├── build_pdf.py                # Markdown → PDF/HTML 변환
│   ├── build_pptx.py               # SRE Book → PPTX (Nordic Minimalism)
│   ├── build_study_guide_pptx.py   # 학습 진도표 → PPTX (Glassmorphism)
│   └── pdf_style.css               # PDF 스타일링
└── output/
    ├── SRE_Study_Guide.md                  # 12주 교차 학습 진도표
    ├── SRE_Study_Guide_Glassmorphism.pptx  # 진도표 슬라이드 (26장)
    ├── SRE_Study_Part1-5_*.pptx            # SRE Book 슬라이드 (5권, 195장)
    ├── sre-book.pdf / .html                # SRE Book 전체 내보내기
    ├── workbook.pdf / .html                # Workbook 전체 내보내기
    └── bsrs.pdf / .html                    # BSRS 전체 내보내기
```

## 시작하기

### 사전 요구사항

```bash
pip install requests beautifulsoup4 python-pptx lxml
```

### 서적 다운로드

```bash
# 전체 3권 다운로드
python3 scripts/download_sre_books.py --book all

# 특정 책만 다운로드
python3 scripts/download_sre_books.py --book sre-book

# 중단 후 재개
python3 scripts/download_sre_books.py --book workbook --resume

# 다운로드 검증
python3 scripts/download_sre_books.py --verify
```

### 학습 교재 생성

```bash
# SRE Book PPTX 슬라이드 생성 (Nordic Minimalism, 5권)
python3 scripts/build_pptx.py

# 교차 학습 진도표 PPTX 생성 (Glassmorphism, 26장)
python3 scripts/build_study_guide_pptx.py

# PDF/HTML 내보내기
python3 scripts/build_pdf.py
```

## 학습 교재

### 12주 교차 학습 커리큘럼

[`output/SRE_Study_Guide.md`](output/SRE_Study_Guide.md)는 3권을 교차 참조하는 12주 학습 계획을 제공합니다:

| 주차 | 학습 내용 | 챕터 수 |
|------|----------|---------|
| 1주 | Part I: 서론 | 2 |
| 2-3주 | Part II: 원칙 | 7 |
| 4-8주 | Part III: 실무 | 18 |
| 9-10주 | Part IV: 관리 | 5 |
| 11주 | Part V: 결론 및 부록 | 2 + 부록 |
| 12주 | 보충 학습 (고유 챕터) | 9 |

### PPTX 슬라이드

| 파일 | 디자인 | 슬라이드 수 | 내용 |
|------|--------|-----------|------|
| `SRE_Study_Part1-5_*.pptx` | Nordic Minimalism | 195장 | SRE Book 챕터별 요약 |
| `SRE_Study_Guide_Glassmorphism.pptx` | Glassmorphism | 26장 | 교차 학습 진도표 및 참조 |

### 주제별 빠른 참조

| 주제 | SRE Book | Workbook | BSRS |
|------|----------|----------|------|
| SLO/SLI/SLA | Ch03-04 | Ch02-03, Ch05 | — |
| 모니터링/알림 | Ch06, Ch10 | Ch04-05 | Ch15 |
| 인시던트 관리 | Ch13-14 | Ch09 | Ch17-18 |
| 포스트모템 | Ch15 | Ch10 | Ch18 |
| 토일/자동화 | Ch05, Ch07 | Ch06 | — |
| 온콜 | Ch11, Ch28 | Ch08 | — |
| 로드 밸런싱/과부하 | Ch19-22 | Ch11, Ch17 | Ch10 |
| 릴리스/배포 | Ch08 | Ch16 | Ch14 |
| 보안 | — | — | Ch01-21 |

## Claude Code 연동

`/sre-knowledge` 스킬로 SRE 지식을 질의할 수 있습니다:

```
/sre-knowledge SLO를 어떻게 설정해야 하나요?
/sre-knowledge 포스트모템 작성 시 주의할 점은?
/sre-knowledge 온콜 로테이션 모범 사례
```

답변에는 항상 출처(`[SRE Book Ch04]`, `[Workbook Ch02]` 등)가 포함됩니다.

## 라이선스

원본 콘텐츠의 저작권은 Google에 있으며, [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스로 공개되어 있습니다.
