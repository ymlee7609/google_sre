# The Evolution of Automation at Google 요약

## 핵심 원칙
- 자동화는 힘의 배수기(force multiplier)이지만 만능약은 아니다 - 자동화보다 자율적(autonomous) 시스템이 더 우수하다
- 자동화의 핵심 가치: 일관성, 플랫폼화, 빠른 복구(MTTR 감소), 빠른 실행, 시간 절약
- 자동화의 진화 5단계: 수동 -> 외부 유지 시스템별 자동화 -> 외부 유지 범용 자동화 -> 내부 유지 시스템별 자동화 -> 자율 시스템
- 자동화 플랫폼은 버그를 중앙 집중화하여 한 번 수정하면 영구적으로 해결된다
- 자동화 코드는 단위 테스트 코드처럼 유지보수팀이 지속적으로 동기화하지 않으면 죽는다
- 가장 기능적인 도구는 일반적으로 그것을 사용하는 사람이 작성한다
- 신뢰성은 근본적 기능이며, 자율적이고 복원력 있는 동작은 이를 달성하는 유용한 방법이다
- 높은 수준의 추상화는 관리가 쉽지만, "누수 추상화" 발생 시 시스템적으로 반복 실패한다

## 주요 프랙티스 및 권고사항
- MySQL on Borg(MoB) 사례: 자동 장애조치(Decider)로 30초 이내 95% 장애 복구, 운영 시간 95% 절감
- 클러스터 턴업 자동화: Prodtest(프로덕션 테스트)로 불일치 탐지, 멱등성 수정(idempotent fix)으로 자동 해결
- 서비스 소유팀이 자동화 코드를 직접 유지해야 한다 - 분리된 턴업 팀은 조직적 인센티브 불일치를 초래한다
- SOA 방식의 클러스터 턴업: 각 서비스팀이 Admin Server를 제공하고 API 계약을 정의한다
- Diskerase 사건 교훈: 빈 집합을 특수 값("모든 것")으로 해석한 자동화가 CDN 전체를 삭제했다
- 속도 제한(rate limiting)과 위생 검사(sanity check)를 자동화에 반드시 포함한다
- 충분히 큰 시스템에서는 자동화 또는 자율적 동작이 더 이상 선택사항이 아니다

## 핵심 인용
> "If we are engineering processes and solutions that are not automatable, we continue having to staff humans to maintain the system." - Joseph Bironas

> "We graduated from optimizing our infrastructure for a lack of failover to embracing the idea that failure is inevitable."

> "The value of automation comes from both what it does and its judicious application."

## 관련 키워드
자동화, 자율 시스템, 일관성, 플랫폼, MTTR, Borg, Decider, Prodtest, 멱등성, SOA, 클러스터 턴업, 기술 부채, Diskerase
