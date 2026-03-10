# Alerting on SLOs 요약

## 핵심 원칙
- SLO 기반 알림은 에러 버짓에 대한 유의미한 위협이 있을 때만 온콜 엔지니어에게 알려야 한다
- 알림 전략 평가의 4가지 속성: 정밀도(Precision), 재현율(Recall), 탐지 시간(Detection time), 리셋 시간(Reset time)
- Burn Rate(소진율)는 SLO 대비 에러 버짓 소비 속도를 나타내는 핵심 개념이다
- 멀티윈도우, 멀티 번레이트 알림(방법 6)이 가장 권장되는 알림 전략이다
- Duration 파라미터는 SLO 기반 알림 기준으로 권장하지 않는다 (간헐적 에러 누락 위험)
- 저트래픽 서비스에는 별도의 알림 접근 방식이 필요하다
- 극단적 가용성 목표(99.999%)는 알림보다 시스템 설계로 방어해야 한다

## 주요 프랙티스 및 권고사항
- 6가지 알림 방법의 진화: 단순 임계값 -> 확대 윈도우 -> Duration -> Burn Rate -> 멀티 Burn Rate -> 멀티윈도우/멀티 Burn Rate
- 권장 알림 파라미터 (99.9% SLO 기준):
  - Page: 1시간 긴 윈도우 / 5분 짧은 윈도우 / 14.4x burn rate / 2% 에러 버짓 소진
  - Page: 6시간 긴 윈도우 / 30분 짧은 윈도우 / 6x burn rate / 5% 에러 버짓 소진
  - Ticket: 3일 긴 윈도우 / 6시간 짧은 윈도우 / 1x burn rate / 10% 에러 버짓 소진
- 짧은 윈도우는 긴 윈도우의 1/12로 설정하면 적절한 리셋 시간 확보 가능
- 저트래픽 서비스 대응: 인공 트래픽 생성, 소규모 서비스 통합, 클라이언트 재시도 구현, SLO 하향 조정
- 대규모 운영 시 요청 유형을 버킷(CRITICAL, HIGH_FAST, HIGH_SLOW, LOW, NO_SLO)으로 분류하여 관리
- 모든 서비스에 동일한 알림 파라미터를 적용하여 운영 부담을 줄여라

## 핵심 인용
> "Your goal is to be notified for a significant event: an event that consumes a large fraction of the error budget."

> "We believe that the multiwindow, multi-burn-rate alerting technique is the most appropriate approach to defending your application's SLOs."

> "The only way to defend this level of reliability is to design the system so that the chance of a 100% outage is extremely low."

## 관련 키워드
SLO 알림, Burn Rate, Error Budget, 멀티윈도우, 정밀도, 재현율, 탐지 시간, 리셋 시간, 저트래픽, Prometheus, 알림 규칙, 에러율
