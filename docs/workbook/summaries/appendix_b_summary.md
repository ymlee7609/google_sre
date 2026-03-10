# Example Error Budget Policy 요약

## 핵심 원칙
- 에러 버짓은 서비스 신뢰성과 혁신 속도의 균형을 맞추는 도구이다
- 에러 버짓 정책은 처벌이 아니라, 데이터가 신뢰성이 더 중요하다고 나타낼 때 팀이 신뢰성에 전적으로 집중할 수 있게 하는 허가이다
- 에러 버짓 = 1 - SLO (예: 99.9% SLO → 0.1% 에러 버짓)
- 변경은 불안정의 주요 원인이며, 약 70%의 장애가 변경에 의해 발생한다
- 기능 개발과 안정성 개발은 경쟁 관계이며, 에러 버짓이 주의를 안정성으로 전환하는 제어 메커니즘이다

## 주요 프랙티스 및 권고사항
- **정책 목표**: 반복적인 SLO 미달로부터 고객을 보호하고, 신뢰성과 기능 간 균형의 인센티브를 제공
- **SLO 미달 정책**:
  - SLO 이상이면: 릴리스 정책에 따라 정상 진행
  - 4주 에러 버짓 소진 시: P0 이슈와 보안 수정을 제외한 모든 변경/릴리스를 중단
- **신뢰성 작업 필수 조건**:
  - 코드 버그나 절차적 오류로 서비스 자체가 에러 버짓을 초과한 경우
  - 포스트모템에서 하드 의존성을 완화할 기회가 발견된 경우
  - 잘못 분류된 에러가 SLO 미달을 유발했을 버짓을 소비하지 못한 경우
- **비신뢰성 작업 계속 허용 조건**:
  - 회사 전체 네트워킹 문제로 인한 장애
  - 다른 팀이 관리하는 서비스로 인한 장애 (해당 팀이 이미 릴리스 동결한 경우)
  - SLO 범위 밖 사용자에 의한 에러 버짓 소비 (부하 테스트, 침투 테스트)
  - 사용자 영향 없이 잘못 분류된 에러가 버짓을 소비한 경우
- **장애 정책**:
  - 단일 인시던트가 4주 에러 버짓의 20% 이상 소비 → 포스트모템 필수 + P0 액션 아이템
  - 단일 장애 유형이 분기 에러 버짓의 20% 이상 소비 → 다음 분기 계획에 P0 항목 포함
- **에스컬레이션**: 에러 버짓 계산이나 정의된 조치에 대한 의견 불일치 시 CTO에게 에스컬레이션
- **적용 범위**: 백엔드와 클라이언트 릴리스 모두에 적용

## 핵심 인용
> "This policy is not intended to serve as a punishment for missing SLOs. Halting change is undesirable; this policy gives teams permission to focus exclusively on reliability when data indicates that reliability is more important than other product features."

> "Changes are a major source of instability, representing roughly 70% of our outages."

## 관련 키워드
에러 버짓, 에러 버짓 정책, SLO 미달, 릴리스 동결, P0, 포스트모템, 신뢰성 작업, 에스컬레이션, 변경 관리, 하드 의존성
