# How SRE Relates to DevOps 요약

## 핵심 원칙
- SRE는 DevOps의 구체적 구현체이다: "class SRE implements interface DevOps"
- DevOps는 CALMS(Culture, Automation, Lean, Measurement, Sharing) 철학을 기반으로 한 광범위한 문화적 움직임이다
- SRE는 운영을 소프트웨어 문제로 취급하며, 소프트웨어 엔지니어링 방법론으로 해결한다
- 100% 가용성은 잘못된 목표이며, SLO(Service Level Objectives)를 통해 적절한 신뢰성 수준을 관리한다
- Toil(반복적 수작업)은 최소화 대상이며, SRE의 50% 이상 시간은 엔지니어링 프로젝트에 투자해야 한다
- 사고(Accidents)는 개인의 실수가 아닌 시스템적 안전장치 부재의 결과이다
- 변경은 작고 점진적으로 이루어져야 하며, CI/CD를 통해 관리한다
- 개발팀과 SRE팀 간 소유권 공유가 필수적이다
- 측정(Measurement)은 DevOps와 SRE 모두의 핵심 기반이다
- 도구(Tooling)는 조직 내 역할과 무관하게 동일해야 한다

## 주요 프랙티스 및 권고사항
- 좁고 경직된 인센티브는 조직 성과를 저해한다 - 출시 또는 안정성에만 연결된 성과 지표를 피하라
- 비난 없는 포스트모템(Blameless Postmortem)을 적극 지원하라
- 운영적으로 개선 불가능한 서비스에 대해서는 지원 철회를 허용하라
- 신뢰성 엔지니어링을 전문 역할로 인식하고, 별도 커뮤니티와 커리어 경로를 제공하라
- DevOps/SRE 조직이 개발 조직과 동등한 존중(Parity of Esteem)을 받도록 보장하라
- SRE 참여는 설계 단계부터 이루어져야 효과가 극대화된다
- MTTR(평균 복구 시간) 단축이 제품 개발 속도 향상으로 이어진다

## 핵심 인용
> "Operations, as a discipline, is hard. Not only is there the generally unsolved question of how to run systems well, but the best practices that have been found to work are highly context-dependent and far from widely adopted."

> "A good culture can work around broken tooling, but the opposite rarely holds true. As the saying goes, culture eats strategy for breakfast."

> "At the end of the day, we all face the same persistent problem: production, and making it better—no matter what we're called."

## 관련 키워드
DevOps, SRE, CALMS, SLO, Toil, Error Budget, Blameless Postmortem, CI/CD, 소유권 공유, 조직 문화, 인센티브 설계, 측정, 변경 관리
