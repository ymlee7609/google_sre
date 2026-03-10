# Simplicity 요약

## 핵심 원칙
- 단순성은 신뢰성과 강하게 상관된다: 단순한 시스템이 덜 고장나고 수리가 빠르다
- "작동하는 복잡한 시스템은 반드시 작동하는 단순한 시스템에서 진화한 것이다" (Gall의 법칙)
- 복잡성은 외부효과(externality)이다 - 도입한 당사자가 아닌 이후 작업자가 비용을 부담한다
- SRE는 시스템 전체를 다루는 역할이므로, 종단 간(end-to-end) 단순성의 챔피언이 될 자연적 적임자이다
- 단순화는 기능(feature)이다 - 명시적으로 우선순위를 부여하고 인력을 배정해야 한다
- 살아있는 소프트웨어 시스템에서 복잡성은 별도의 노력 없이는 계속 증가한다

## 주요 프랙티스 및 권고사항
- 시스템 복잡성 측정 대리지표: 교육 시간, 설명 시간, 관리 다양성, 배포된 설정의 다양성, 시스템 나이
- 코드 복잡성: Cyclomatic Complexity(순환 복잡도) 등 정량적 도구 활용
- 엔지니어 온콜 전 시스템 다이어그램 작성 및 정기적 갱신 권장
- 주요 설계 문서에 SRE 리뷰를 반드시 포함하라
- 리라이트(전체 재작성) 결정 시 이전 비용 주의: 이동 대상, 마이그레이션 계획, 전환 기간 추가 비용 평가 필요
- 시스템 다이어그램에서 증폭(Amplification), 순환 의존성(Cyclic Dependencies)을 찾아라
- 단순화 프로젝트를 기능 출시와 동등하게 보상하라, 코드 추가와 삭제를 동등하게 평가하라
- 엔지니어링 프로젝트 시간의 10%를 단순화 프로젝트에 예약하라
- **사례 연구**: Google Ads의 스파이더웹 단순화(단일 표준으로 통합), Borg/Omega 리라이트 교훈, pDNS 순환 의존성 제거, 공유 마이크로서비스 플랫폼 구축

## 핵심 인용
> "A complex system that works is invariably found to have evolved from a simple system that worked." (Gall의 법칙)

> "Complexity is an externality. Instead, complexity impacts those who continue to work in and around it."

> "Don't compare the expected result to your current system. Instead, compare the expected result to what your current system would look like if you invested the same effort in improving it."

## 관련 키워드
단순성, 복잡성, 순환 복잡도, 시스템 다이어그램, 리라이트, 마이크로서비스, 표준화, 순환 의존성, 외부효과, Gall의 법칙, Hyrum의 법칙
