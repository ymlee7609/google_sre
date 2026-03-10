# Service Level Objectives 요약

## 핵심 원칙
- SLI(Service Level Indicator)는 서비스 수준의 정량적 측정 지표이다
- SLO(Service Level Objective)는 SLI의 목표값 또는 범위이다 (예: 지연시간 < 100ms, 99% 이상)
- SLA(Service Level Agreement)는 SLO를 포함하며 미달 시 결과(보상/벌칙)가 따르는 계약이다
- 서비스 유형별 핵심 SLI: 사용자 대면(가용성, 지연, 처리량), 스토리지(지연, 가용성, 내구성), 빅데이터(처리량, E2E 지연)
- 평균값보다 백분위수(percentile)를 사용해야 롱테일 지연을 포착할 수 있다
- SLO를 게시하면 사용자 기대치를 설정하여 근거 없는 불만을 줄일 수 있다
- SLO가 없으면 사용자는 자체적으로 기대치를 형성하며, 이는 과의존이나 과소평가로 이어진다
- 모든 시스템은 정확성(correctness)도 추적해야 한다

## 주요 프랙티스 및 권고사항
- SLO는 현재 성능이 아니라 사용자가 원하는 것에서 역방향으로 설정한다
- SLO는 가능한 적게 유지한다 - 우선순위 논의에서 인용할 수 없는 SLO는 불필요하다
- 내부 SLO는 외부 SLO보다 엄격하게 설정하여 안전 마진을 확보한다
- 의도적으로 과달성하지 않는다 - Chubby처럼 계획된 장애를 통해 과의존을 방지한다
- SLI 표준 템플릿을 만들어 재사용하고, 집계 간격/지역/빈도를 표준화한다
- 다양한 워크로드에 대해 별도의 SLO 목표를 정의한다 (처리량 클라이언트 vs 지연 클라이언트)
- SLO 위반율과 에러 버짓을 비교하여 릴리스 속도를 조절하는 제어 루프를 운영한다
- 처음부터 완벽한 SLO를 추구하지 않고, 느슨한 목표에서 시작하여 점진적으로 조정한다

## 핵심 인용
> "If you can't ever win a conversation about priorities by quoting a particular SLO, it's probably not worth having that SLO."

> "Choosing and publishing SLOs to users sets expectations about how a service will perform."

> Chubby 사례: 과도한 가용성이 비합리적 의존성을 만들어, 의도적 다운타임을 도입했다.

## 관련 키워드
SLI, SLO, SLA, 가용성, 지연시간, 처리량, 백분위수, 에러 버짓, 제어 루프, Chubby, 표준 템플릿, 내구성
