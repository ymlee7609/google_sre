# Simplicity 요약

## 핵심 원칙
- 소프트웨어 단순성은 신뢰성의 전제 조건이다
- SRE의 핵심 역할: 시스템의 민첩성(agility)과 안정성(stability) 사이의 균형을 유지하는 것
- 본질적 복잡성(essential complexity)과 우발적 복잡성(accidental complexity)을 구분해야 한다
- "지루한" 코드가 좋은 코드이다 - 프로덕션에서 놀라움은 SRE의 적이다
- 새로 작성되는 모든 코드 라인은 잠재적 부채이다 - 코드 추가 시 신중해야 한다
- 완벽함은 더 이상 추가할 것이 없을 때가 아니라 더 이상 제거할 것이 없을 때 달성된다
- "No"라고 말하는 것은 혁신을 제한하는 것이 아니라, 진정한 엔지니어링에 집중할 수 있게 하는 것이다
- 신뢰성 있는 프로세스는 실제로 개발자 민첩성을 높인다

## 주요 프랙티스 및 권고사항
- 데드 코드를 적극적으로 삭제한다 - 주석 처리나 플래그 게이팅은 시한폭탄이다 (Knight Capital 사례)
- "네거티브 라인 오브 코드" 메트릭: 코드 삭제가 때로 가장 만족스러운 코딩이 될 수 있다
- 최소한의 API 설계: 메서드와 인수를 최소화하고, 각 메서드를 최대한 우수하게 만든다
- 모듈성 확보: 바이너리 간, 설정과 바이너리 간 느슨한 결합을 유지한다
- API 버전 관리로 개발자가 안전하게 업그레이드할 수 있게 한다
- 릴리스 단순성: 100개 변경을 동시 배포하는 대신, 작은 배치로 나누어 영향도를 측정한다
- "util" 또는 "misc" 바이너리를 프로덕션에 배포하지 않는다 - 각 컴포넌트에 명확한 목적을 부여한다
- 소프트웨어 비대화(bloat) 감지를 모든 수준의 테스트에 통합한다

## 핵심 인용
> "The price of reliability is the pursuit of the utmost simplicity." - C.A.R. Hoare

> "Unlike a detective story, the lack of excitement, suspense, and puzzles is actually a desirable property of source code." - Robert Muth

> "Perfection is finally attained not when there is no longer more to add, but when there is no longer anything to take away." - Antoine de Saint Exupery

## 관련 키워드
단순성, 민첩성, 안정성, 본질적 복잡성, 우발적 복잡성, 데드 코드, 최소 API, 모듈성, 느슨한 결합, 소프트웨어 비대화, 코드 삭제
