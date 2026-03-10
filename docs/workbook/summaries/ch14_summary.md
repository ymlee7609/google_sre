# Configuration Design and Best Practices 요약

## 핵심 원칙
- 이상적인 설정은 설정이 전혀 없는 것이다 - 가능한 한 설정 항목을 줄이는 방향으로 설계하라
- 설정은 사용자에게 질문하는 것이다 - 사용자 중심(user-centric) 관점에서 설계하라
- 설정 철학(philosophy)과 설정 메커니즘(mechanics)을 분리하여 사고하라
- 사소한 설정 변경이 프로덕션 시스템에 극적인 영향을 미칠 수 있다
- 설정의 품질은 시스템 신뢰성에 직접적 영향을 미친다
- 설정 질문은 사용자의 목표(goal)에 가까워야 한다 - 인프라 세부사항이 아닌 사용자 의도를 물어라

## 주요 프랙티스 및 권고사항
- **필수 질문 최소화**: 필수 설정 항목을 선택적 항목으로 전환하고, 합리적인 기본값을 제공하라
- **동적 기본값(Dynamic Defaults)**: 시스템 환경에 따라 자동으로 결정되는 기본값 활용 (예: CPU 코어 수에 따른 스레드 수)
- **파워 유저 탈출구**: 고급 사용자를 위해 기본값을 오버라이드할 수 있는 선택적 설정 제공
- **설정과 데이터 분리**: 상위 수준 설정 언어(DSL)와 하위 수준 정적 데이터(JSON, YAML, Protocol Buffers) 분리
- **도구 지원**: 시맨틱 검증, 문법 하이라이팅, 린터, 자동 포매터 필수
- **소유권과 변경 추적**: 설정 파일의 명확한 소유자 지정, 버전 관리 시스템 활용
- **안전한 설정 변경 적용**: 점진적 배포, 롤백 가능성, 운영자 제어 상실 시 자동 롤백
- **밀폐적(Hermetic) 설정**: 외부 리소스에 의존하지 않아 롤백과 재현이 가능한 설정

## 핵심 인용
> "Trivial configuration changes can impact a production system in dramatic ways, so we need to deliberately design configuration to mitigate these risks."

> "A good culture can work around broken tooling, but the opposite rarely holds true."

> "Our ideal configuration is no configuration at all."

## 관련 키워드
설정 설계, 사용자 중심, 기본값, 동적 기본값, 밀폐성, 설정 검증, 롤백, 점진적 배포, DSL, 인프라 중심 vs 사용자 중심
