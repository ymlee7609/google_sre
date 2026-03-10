# Canarying Releases 요약

## 핵심 원칙
- 카나리는 변경의 부분적이고 시간 제한된 배포 후 평가하는 프로세스이다 (A/B 테스트와 유사)
- 릴리스 속도와 신뢰성은 대립 목표가 아니다 - SLO와 에러 버짓으로 균형을 잡을 수 있다
- Google의 대다수 인시던트는 바이너리 또는 설정 푸시에 의해 트리거된다
- 테스트 환경은 프로덕션과 100% 동일하지 않으므로, 일부 결함은 반드시 프로덕션에 도달한다
- 카나리를 통해 결함을 가능한 빨리, 가능한 적은 영향으로 탐지한다

## 주요 프랙티스 및 권고사항
- **릴리스 엔지니어링 원칙**: 재현 가능한 빌드, 자동화된 빌드/테스트/배포, 작은 배포 단위
- **카나리 구현 요소**: 부분 집합 배포 방법, 평가 프로세스, 릴리스 프로세스와의 통합
- **카나리 인구와 기간 결정 시 고려사항**:
  - 개발 속도에 맞는 카나리 기간 설정
  - 동시에 하나의 카나리만 실행 권장
  - 트래픽이 많을수록 짧은 시간에 대표적 샘플 확보 가능
  - 피크 시간에 배포하여 성능 결함 탐지
- **메트릭 선택 기준**: 문제를 나타내는가? 대표성이 있는가? 변경에 귀속 가능한가?
  - SLI를 카나리 메트릭의 출발점으로 활용
  - 메트릭은 12개 이하로 제한
  - CPU 사용량보다 HTTP 응답 코드, 지연시간이 더 효과적
- **점진적 카나리**: 작은 인구로 시작하여 신뢰도가 높아지면 단계적으로 확대
- **Before/After 평가의 위험성**: 시간이 가장 큰 변수이므로 A/B 동시 비교가 더 안전
- **모니터링 요구사항**: 카나리와 컨트롤 인구별 메트릭 분리, 메트릭 집계 간격이 카나리 기간 이하
- 피처 플래그로 바이너리 릴리스와 기능 출시를 분리하라

## 핵심 인용
> "Canarying allows the deployment pipeline to detect defects as quickly as possible with as little impact to your service as possible."

> "A majority of incidents are triggered by binary or configuration pushes."

> "No single testing methodology is a panacea, and testing strategies should be informed by the requirements and behavior of the system."

## 관련 키워드
카나리, 릴리스 엔지니어링, CI/CD, A/B 테스트, 에러 버짓, 점진적 배포, 피처 플래그, Blue/Green 배포, 메트릭 선택, 롤백, 트래픽 분할
