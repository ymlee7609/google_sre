# Google SRE, 통신사업자의 운영 패러다임을 바꾸다 — Swisscom 사례를 중심으로

> "SRE is what happens when you ask a software engineer to design an operations function."  
> — Ben Treynor Sloss, VP of Engineering at Google

---

## 들어가며: 왜 지금 SRE일까?

통신사업자의 네트워크 운영 환경이 근본적으로 달라지고 있습니다. 5G SA 코어의 클라우드 네이티브 전환, 가상화(NFV/SDN)의 보편화, AI/ML 기반 자동화의 확산… 이런 변화들이 전통적인 NOC(Network Operations Center) 중심의 운영 체계에 구조적 한계를 드러내고 있는 거죠. 수백 명의 운용인력이 대형 스크린 앞에서 초록-노랑-빨강 알람을 뚫어져라 바라보며, Tier-1 → Tier-2 → Tier-3로 에스컬레이션하던 방식은 마이크로서비스 기반 분산 아키텍처와 빠른 릴리스 주기 앞에서 점점 힘을 잃어가고 있습니다.

이 글에서는 Google이 만들어낸 SRE(Site Reliability Engineering)의 핵심 원리를 살펴보고, 통신사업자가 이걸 어떻게 자사 네트워크 운영에 적용할 수 있는지 정리해 보겠습니다. 마지막으로 스위스 1위 통신사업자 Swisscom이 SRE를 전사적으로 도입한 실제 사례도 함께 소개합니다.

---

## 1. Google SRE란 무엇인가

### 1.1 어떻게 시작됐을까?

SRE는 2003년, Google의 Ben Treynor Sloss가 프로덕션 운영팀을 이끌며 시작한 접근법입니다. 핵심 발상은 의외로 단순해요. **운영(Operations)을 소프트웨어 엔지니어링 문제로 재정의한 것입니다.** 원래 개발팀과 운영팀은 서로 다른 인센티브 구조를 갖고 있었습니다. 개발팀은 "빨리 기능 내자!", 운영팀은 "제발 안정적으로 좀 돌아가자!"를 외치면서 구조적 긴장이 생길 수밖에 없었죠. SRE는 이 오래된 긴장을 데이터 기반의 의사결정 프레임워크로 풀어냅니다.

### 1.2 핵심 개념 4가지

**① SLI / SLO / Error Budget — 신뢰성을 숫자로 말하기**

SRE에서 가장 중요한 개념은 서비스 수준을 "측정 가능한 지표"로 정의하는 겁니다.

- **SLI (Service Level Indicator)**: 사용자가 실제로 체감하는 서비스 품질을 측정하는 지표예요. 요청 성공률, 응답 지연시간(latency), 처리량(throughput) 같은 것들이 여기에 해당됩니다.
- **SLO (Service Level Objective)**: SLI에 대한 내부 목표값입니다. 예를 들면, "HTTP 요청의 99.9%가 200ms 이내에 성공 응답을 반환해야 한다" 같은 형태죠.
- **Error Budget**: "100% - SLO"로 산출되는 허용 불안정 예산입니다. SLO가 99.9%라면, 0.1%만큼의 장애나 성능 저하가 허용되는 거예요. 4주간 100만 건의 요청을 받는 서비스라면, 1,000건의 오류까지는 괜찮다는 뜻이죠.

Error Budget의 핵심 가치는 **개발 속도와 신뢰성 사이의 균형을 데이터로 관리**한다는 점입니다. 예산이 충분하면 새로운 기능을 적극적으로 배포하고, 예산이 바닥나면 릴리스를 동결하고 안정성 작업에 집중하는 거예요. 재밌는 건, 개발팀이 스스로 리스크를 관리하게 되는 자기 규율(self-policing) 메커니즘이 저절로 작동한다는 점입니다.

**② Toil 제거 — 반복 작업, 이제 그만!**

SRE에서 "Toil"이란 수동적이고, 반복적이며, 자동화 가능하고, 서비스 성장에 비례해서 선형적으로 늘어나는 운영 작업을 뜻합니다. 쉽게 말해, "사람이 꼭 안 해도 되는데 계속 사람이 하고 있는 일"이에요. Google SRE 팀은 전체 업무시간의 50% 이상을 Toil이 아닌 엔지니어링 프로젝트에 쓰도록 명시적으로 관리합니다. Toil 비율이 50%를 넘으면? 인력 충원이나 자동화 투자의 근거로 바로 활용되죠.

**③ Blameless Postmortem — "누가 잘못했냐"가 아니라 "왜 실패했냐"**

장애가 발생하면 범인 찾기가 아니라 시스템 차원의 원인 분석을 합니다. Google SRE 문화에서 포스트모템은 사건의 영향, 근본 원인(root cause), 재발 방지를 위한 액션 아이템을 구조화된 문서로 기록하는 프로세스예요. Error Budget의 20% 이상을 소진한 단일 인시던트에 대해서는 반드시 포스트모템을 수행합니다. 핵심은 "비난하지 않는 것(blameless)"인데, 사실 이게 말처럼 쉽지 않아서 문화적으로 정착시키는 데 상당한 노력이 필요합니다.

**④ Observability — 모니터링 그 너머**

전통적 NOC 모니터링이 미리 정해둔 임계값 기반의 정적 감시(watch)라면, SRE의 Observability는 시스템이 스스로 자기 상태를 설명할 수 있도록 설계하는 겁니다. 메트릭(Metrics), 로그(Logs), 트레이싱(Traces)이라는 세 기둥(three pillars)을 통해 "예상하지 못한 질문에도 답할 수 있는 시스템"을 만드는 거죠. 기존에는 "CPU가 90% 넘으면 알람"이었다면, Observability에서는 "왜 이 시점에 이 요청이 느려졌는지"까지 추적할 수 있어야 합니다.

### 1.3 DevOps와는 어떤 관계?

DevOps가 조직 문화와 협업 철학을 정의하는 추상 인터페이스라면, SRE는 그걸 구체적인 실천법으로 구현한 클래스입니다. Swisscom의 Michael Ludwig는 이걸 개발자답게 이렇게 표현했어요.

> "class SRE implements interface DevOps."

정말 깔끔한 비유죠? DevOps의 5대 축(Reduce Silos, Accept Failure, Implement Gradual Change, Leverage Tooling, Measure Everything)에 대해, SRE는 각각 SLO 기반 공동 책임, Error Budget, 카나리 릴리스, 자동화/Toil 제거, SLI 모니터링이라는 구체적 실행 방안을 매핑합니다.

---

## 2. 통신사업자에게 SRE를 적용한다는 것

### 2.1 왜 통신사에 SRE가 필요할까?

사실 통신사 네트워크 운영 환경은 Google의 인터넷 서비스 운영과 놀라울 정도로 비슷한 도전과제를 공유하고 있습니다.

**공통 도전 과제들:**

- 수백만 사용자에 대한 "Always-On" 가용성 요구
- 수천 개의 분산된 네트워크 요소(RAN, Core, Transport)에 대한 동시 모니터링
- 빈번한 소프트웨어 업데이트 및 설정 변경(5G SA, 가상화 환경)
- 레거시 시스템과 클라우드 네이티브 시스템의 공존(Hybrid 운영)
- 장애 시 막대한 재무 및 평판 손실

**하지만 구조적 차이도 분명히 있습니다:**

| 영역 | Google/IT SRE | 통신사업자 SRE 적용 |
|------|-------------|------------------|
| 서비스 대상 | 웹 서비스, API, 앱 | 무선 네트워크, 코어, 전송망, BSS/OSS |
| SLI 정의 | HTTP 성공률, 지연시간 | RAN KPI(CSSR, CDR, Throughput), 코어 세션 성공률, E2E 서비스 품질 |
| Error Budget 단위 | 요청 실패 건수 / 다운타임 | 네트워크 장애 시간, KPI 위반 시간, 영향 가입자 수 |
| Toil의 형태 | 수동 배포, 알람 대응 | 수동 파라미터 튜닝, 반복적 알람 필터링, 수기 보고서 작성 |
| 릴리스 주기 | 일 단위 배포 | 벤더 소프트웨어 업그레이드 주기(분기~반기) |
| 조직 구조 | DevOps 팀 내 SRE | NOC + NE(Network Engineering) + 벤더 다자 구조 |

이 차이를 인식하면서 적용해야 "Google 따라하기"가 아닌 "우리 맥락에 맞는 SRE"를 만들 수 있습니다.

### 2.2 통신사 SRE 적용의 핵심 전환 포인트

**① NOC에서 SRE로: "감시하는 사람"에서 "설계하는 엔지니어"로**

전통적 NOC의 Tier-1 인력은 알람을 확인하고 티켓을 생성하는 "감시자" 역할에 머물러 있습니다. SRE 모델에서는 이런 반복 작업을 자동화하고, 운용인력은 시스템 복원력을 설계하고 장애를 사전에 예방하는 엔지니어링 활동에 집중하게 됩니다. 핵심 차이를 한 줄로 정리하면 이렇습니다. **SRE의 역할은 장애가 발생한 이후가 아니라, 장애가 발생하기 전에 시작됩니다.**

**② 네트워크 KPI를 SLI/SLO 체계로 재정의하기**

통신사에는 수백 가지 네트워크 KPI가 있는데, 이 중에서 "사용자 체감 품질"을 대변하는 핵심 SLI를 선별해야 합니다. 예를 들어 RAN 영역에서는 호 접속 성공률(CSSR), 호 절단율(CDR), 사용자 체감 다운로드 속도를 SLI로 정의하고, 각각에 대해 SLO를 설정하는 거예요. SLO가 위반되면 Error Budget이 소진되고, 이게 네트워크 변경(파라미터 최적화, SW 업그레이드) 속도를 조절하는 제어 장치가 됩니다. 꽤 강력한 메커니즘이죠.

**③ 벤더 협력에도 SRE 원칙 적용하기**

통신사 네트워크에는 Ericsson, Nokia, Samsung, Huawei 등 다수 벤더의 장비가 섞여 있습니다. SRE의 Error Budget Policy를 벤더 관리에 적용하면 어떻게 될까요? 특정 벤더 장비에서 발생한 장애가 전체 서비스 SLO에 미치는 영향을 정량적으로 추적하고, 벤더별 책임 소재를 데이터 기반으로 관리할 수 있게 됩니다. "느낌"이 아니라 "숫자"로 대화하게 되는 거죠.

**④ Chaos Engineering, 통신망에도 가능할까?**

Google SRE에서 파생된 Chaos Engineering(의도적으로 장애를 주입해서 시스템 복원력을 검증하는 방법)을 통신 네트워크에 적용할 수 있을까요? 물론 상용 네트워크에 바로 적용하기는 부담스럽습니다. 하지만 Pre-production 환경이나 디지털 트윈(Digital Twin) 기반의 시뮬레이션 환경에서 네트워크 장애 시나리오를 사전 검증하는 건 충분히 현실적입니다.

### 2.3 적용 로드맵 제안

통신사가 SRE를 도입할 때는 한 번에 다 바꾸려 하면 안 됩니다. 단계적 접근이 핵심이에요.

**Phase 1 — 기반 구축 (6-12개월)**
SLI/SLO를 시범 서비스(예: VoLTE, 5G 데이터)에 대해 정의하고, Error Budget 모니터링 체계를 구축합니다. Blameless Postmortem 프로세스를 도입하고, 기존 ITSM 프로세스(ITIL 기반)와 연계하는 작업도 함께 진행합니다.

**Phase 2 — Toil 제거 및 자동화 (12-24개월)**
반복적인 NOC 운영 작업을 식별하고 자동화합니다. Observability 플랫폼을 구축해서 기존 NMS/EMS 알람 중심의 모니터링을 메트릭-로그-트레이스 통합 관측 체계로 전환하고, On-call 로테이션 체계도 도입합니다.

**Phase 3 — 문화 내재화 (24개월+)**
Error Budget Policy를 조직 의사결정에 실질적으로 반영합니다. SRE Community of Practice를 운영하고 Reliability Champion 역할을 전파하며, Chaos Engineering을 디지털 트윈 기반으로 시범 적용합니다.

---

## 3. Swisscom 사례: 통신사 SRE 전환의 선두주자

### 3.1 Swisscom은 어떤 회사인가

Swisscom은 스위스 1위 통신사업자이자 ICT 기업입니다. 모바일, 인터넷, TV 서비스와 종합 IT 서비스를 제공하고 있고, 스위스 최고 모바일 네트워크 품질 평가를 수년간 유지하고 있어요. 900명 이상의 IT 전문가와 250명 이상의 AI 전문가가 근무하고 있으며, 2015년부터 DevOps 원칙에 기반한 운영 체계를 전사적으로 적용해 왔습니다.

### 3.2 SRE 도입, 어떻게 진행됐을까?

Swisscom의 SRE 여정은 DevOps 성숙도를 기반으로 한 자연스러운 진화였습니다. "SRE는 DevOps를 대체하는 게 아니라, DevOps가 해결하지 못하는 서비스 신뢰성 관리의 구체적 방법론을 제공하는 것"이라고 명확하게 포지셔닝한 게 인상적이에요.

구체적으로 어떤 활동들이 있었는지 하나씩 살펴보겠습니다.

**① Reliability Champion 제도**

SRE 전환의 첫 번째 추진체는 각 팀에 배치된 "Reliability Champion"이었습니다. 이 사람들이 자기 팀 서비스에 대한 SLI/SLO 정의, Error Budget 관리, Postmortem 문화 전파를 주도했어요. 전사 전담 SRE 팀을 한 번에 만드는 게 아니라, 기존 DevOps 팀 안에서 Reliability에 특화된 역할을 만드는 분산형 접근법을 택한 거죠. 실용적이면서도 현실적인 선택이라고 생각합니다.

**② SRE Community of Practice**

Swisscom은 SRE 실천 공동체(Community of Practice)를 만들어서 서로 다른 팀의 SRE 경험과 베스트 프랙티스를 공유하는 플랫폼을 운영하고 있습니다. 이 커뮤니티는 단순한 정보 공유를 넘어서, SLO 설정 기준의 표준화, Toil 측정 방법론의 통일, Postmortem 템플릿 공유 등 실질적인 운영 표준을 함께 만들어가고 있어요. 2024년 11월에는 Grafana Labs와 함께 베른에서 "Effective SRE & DevOps Conference"를 주최하기도 했습니다. 커뮤니티가 외부까지 확장된 셈이죠.

**③ 모바일 네트워크 인프라까지 SRE 확장 — 이게 진짜 핵심입니다**

Swisscom의 SRE 적용이 특히 주목받는 이유가 여기 있습니다. IT 서비스뿐 아니라 **모바일 네트워크 인프라** 운영에까지 SRE 원칙을 확장한 거예요. Romain Bonjour가 이끄는 팀이 모바일 네트워크 인프라의 SRE 전환을 주도하면서, 복잡계 시스템의 신뢰성을 위한 도구, 교육, 베스트 프랙티스를 구현하고 있습니다. 특히 클라우드 네이티브 시스템과 레거시 기술 모두에 대한 자동화된 릴리스 엔지니어링을 고가용성 시스템의 핵심 동력으로 삼고 있어요.

이 팀은 2023년 10월 더블린에서 열린 USENIX SREcon23 EMEA에서 "Implementing SRE in a Telco with Reliability Enhancing Procedures"라는 제목으로 발표를 했습니다. 통신사 환경에서 SRE를 구현하는 구체적인 방법론과 경험을 업계에 공유한, 정말 의미 있는 발표였어요.

**④ CRE (Customer Reliability Engineering) 서비스로 외부에도 제공**

흥미로운 건, Swisscom이 자사의 SRE 역량을 외부 기업고객에게도 서비스 형태로 제공한다는 점입니다. CRE(Customer Reliability Engineer)라는 직무를 통해 고객 기업 애플리케이션의 SLI/SLO 정의, Application Reliability Review, 리스크 모니터링, Reliability Reporting, 인시던트 관리 및 Postmortem까지 수행해 주는 거죠. Public Cloud와 Private Cloud를 모두 아우르는 하이브리드, 플랫폼 독립적인 접근 방식이 특징입니다.

**⑤ AI 기반 Network Assistant + SRE 원칙의 결합**

Swisscom은 Amazon Bedrock 기반의 Network Assistant를 구축해서, 네트워크 엔지니어들이 자연어로 네트워크 파라미터, 데이터 소스, 트러블슈팅 가이드에 접근할 수 있도록 만들었습니다. RAG(Retrieval Augmented Generation) 아키텍처를 기반으로 하고 있고, 엔지니어들이 일상적인 데이터 수집과 분석에서 벗어나 전략적 업무에 집중할 수 있게 해줍니다. Swisscom 스스로도 이 접근이 자사 SRE 원칙에 부합한다고 밝히고 있는데요, Toil 제거의 AI 기반 진화 형태라고 볼 수 있겠죠.

**⑥ 네트워크 컨버전스와 자동화 — 숫자가 말해줍니다**

Swisscom은 Cisco와의 파트너십을 통해 5개의 MPLS 네트워크를 단일 SRv6 네트워크로 통합하는 네트워크 컨버전스를 완료했습니다. 이 과정에서 CI/CD 파이프라인과 테스트 자동화를 네트워크 운영에 도입해서 완전 자동화된 네트워크 운영을 구현하고 있어요. 결과가 놀랍습니다. **400일 이상 단일 주요 에스컬레이션 장애 없는 기록**, 그리고 **전력 소비 약 50% 절감**. SRE의 자동화 원칙이 통신 인프라에 적용되면 이런 성과가 가능하다는 걸 확실히 보여주는 사례입니다.

여기서 끝이 아닙니다. Ericsson과의 전략적 파트너십을 통해 EIAP(Ericsson Intelligent Automation Platform)와 AI 기반 rApp(Cell Anomaly Detector, Uplink Anomaly Detector, Anomaly Root Cause Explainer 등)을 상용 네트워크에 통합하고 있어요. 자율 네트워크(Autonomous Network) 비전의 실현이자, SRE의 Observability와 자동화 원칙이 RAN 영역으로까지 뻗어나간 모습입니다.

### 3.3 Swisscom이 우리에게 주는 시사점

Swisscom 사례에서 통신사업자가 참고할 핵심 교훈을 정리하면 이렇습니다.

첫째, **점진적 전환**입니다. Swisscom은 전사 SRE 팀을 하루아침에 만들지 않았어요. DevOps 기반 위에 Reliability Champion을 배치하고, Community of Practice를 통해 문화를 천천히 퍼뜨리는 단계적 접근법을 택했습니다.

둘째, **IT와 네트워크의 경계를 넘는 적용**입니다. 대부분의 통신사가 SRE를 BSS/OSS 같은 IT 시스템에만 적용하는 데 반해, Swisscom은 모바일 네트워크 인프라까지 SRE 원칙을 확장했어요. 클라우드 네이티브 전환이 가속화되는 환경에서 정말 선도적인 행보라고 볼 수 있습니다.

셋째, **SRE와 자율 네트워크의 자연스러운 연결**입니다. Swisscom이 추진하는 rApp 기반 네트워크 자동화, AI Network Assistant, CI/CD 기반 네트워크 릴리스는 모두 SRE의 Toil 제거, Observability, 자동화 원칙의 연장선에 있습니다. SRE는 TM Forum의 Autonomous Network Level 진화와도 자연스럽게 연결되는 프레임워크인 거죠.

---

## 4. 마치며: SRE는 도구가 아니라 사고방식입니다

SRE를 도입한다는 건 특정 도구를 설치하거나 조직도에 새로운 박스를 추가하는 게 아닙니다. **"100% 가용성은 불가능하다"는 현실을 인정하고, 허용 가능한 불안정의 범위를 데이터로 관리하며, 반복 작업을 엔지니어링으로 대체하고, 실패에서 시스템적으로 학습하는 문화**를 만드는 것입니다.

통신사업자에게 SRE의 진정한 가치는, 네트워크 품질 관리를 "문제가 터진 후의 대응"에서 "문제가 터지기 전의 설계"로 바꾸는 패러다임 시프트에 있습니다. Swisscom이 보여준 것처럼, 이 전환은 하루아침에 이루어지지 않아요. 하지만 SLI/SLO/Error Budget이라는 공통 언어를 갖추고, Reliability Champion이라는 변화의 씨앗을 심고, Community of Practice라는 토양을 만들면, 그 전환은 분명히 시작됩니다.

---

### 참고 자료

- Google, *Site Reliability Engineering* Book (sre.google)
- Google, *The Site Reliability Workbook* — Implementing SLOs, Error Budget Policy
- Swisscom getIT Blog, "SRE vs DevOps – Competitors or Friends" (2020.08)
- USENIX SREcon23 EMEA, Kammermann & Bonjour, "Implementing SRE in a Telco with Reliability Enhancing Procedures" (2023.10, Dublin)
- Swisscom B2B Magazine, "Site Reliability Engineering" (2022.08)
- Swisscom Career, Engineering & Technology — SRE Community of Practice
- AWS Blog, "Transforming network operations with AI: How Swisscom built a network assistant using Amazon Bedrock" (2025.07)
- Cisco Case Study, "Swisscom taps Agile Services Networking for success" (2025.07)
- Ericsson Press Release, "Swisscom and Ericsson advance autonomous network transformation" (2026.02)
- Digital Architects Zurich, "Effective SRE & DevOps Conference" — Swisscom & Grafana Labs (2024.11)

---

*이 글은 통신사업자의 네트워크 운영 품질 혁신을 위해 Google SRE 방법론의 적용 가능성을 탐색하는 시리즈의 일부입니다.*
