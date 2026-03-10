# Conclusion 요약

## 핵심 원칙
- SRE의 압도적 성공의 열쇠는 그 운영 원칙의 본질에 있다 - 일반적이면서도 미래에도 적용 가능한 유연한 규칙 체계
- SRE는 파일럿이자 엔지니어/설계자의 역할을 동시에 수행한다 - 대규모 인프라 운영 경험을 실제 코드로 체계화하여 재사용 가능한 제품으로 패키징한다
- SRE의 핵심 책임과 관심사는 시간이 지나도 일관되지만, 구체적 활동은 서비스와 역량의 성숙에 따라 진화한다
- SRE 팀은 가능한 한 소규모여야 하며 높은 수준의 추상화에서 운영하되, 시스템의 일상적 운영에서 오는 포괄적 지식도 갖추어야 한다

## 주요 프랙티스 및 권고사항
- SRE 팀 구성: 두 가지 동등하게 중요한 업무 유형 사이에 시간을 분배 - 온콜 교대로 시스템이 어디서 어떻게 깨지는지 관찰하고, 이를 관리하기 쉽게 만들 것을 설계하고 구축
- 경험의 코드화: 대규모 컴퓨팅 인프라 운영 경험을 실제 코드로 구현하고 개별 제품으로 패키징하여 다른 SRE 팀과 Google 전체(심지어 Google Cloud를 통해 외부에도) 공유
- 항공 산업 비유: 100년 전 비행기는 단일 엔진에 파일럿이 정비사도 겸했지만, 오늘날 747은 수백 명의 승객과 수톤의 화물을 싣고 대륙 간 비행하면서도 조종석에는 여전히 두 명의 파일럿만 있다
- 확장의 비밀: 잘 설계되고 접근 가능한 인터페이스, 충분한 유연성, 훈련된 운영자, 견고한 백업 시스템과 신중한 API
- SRE의 불변 관심사: 시스템이 1,000배 커져도 여전히 신뢰성, 유연성, 비상 관리 용이성, 모니터링, 용량 계획이 필요
- 활동의 진화: "20대 머신의 대시보드 구축"에서 "수만 대 머신 플릿의 자동 발견, 대시보드 구축, 알림 자동화"로 발전
- Ben Treynor Sloss의 서론에서 제시한 책임과 원칙이 10년이 지나도 여전히 정확하게 적용됨 - 인프라와 팀의 변화와 성장에도 불구하고

## 핵심 인용
> "The interfaces to the plane's operating systems are well thought out and approachable enough that learning how to pilot them in normal conditions is not an insurmountable task."

> "An SRE team should be as compact as possible and operate at a high level of abstraction, relying upon lots of backup systems as failsafes and thoughtful APIs to communicate with the systems."

## 관련 키워드
SRE 결론, 항공 비유, 경험의 코드화, 추상화, 파일럿과 엔지니어, 확장성, 미래 지향 원칙, Google Cloud, 인터페이스 설계, 소규모 팀
