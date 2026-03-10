# Monitoring Distributed Systems 요약

## 핵심 원칙
- 모니터링의 네 가지 골든 시그널: 지연시간(Latency), 트래픽(Traffic), 에러(Errors), 포화도(Saturation)
- 증상(Symptom)과 원인(Cause)을 명확히 구분해야 한다 - "무엇이 고장났는가"와 "왜 고장났는가"
- 화이트박스 모니터링(내부 상태 기반)과 블랙박스 모니터링(사용자 관점)을 결합하여 사용한다
- 페이징은 비용이 큰 행위이므로, 모든 페이지는 긴급하고 실행 가능하며 지능적 대응이 필요해야 한다
- Google은 단순하고 빠른 모니터링 시스템을 선호하며, 자동 임계값 학습 같은 "마법" 시스템을 지양한다
- 이메일 알림은 가치가 매우 제한적이며 노이즈에 쉽게 매몰된다 - 대시보드를 선호한다
- 개별 머신 장애에 대한 알림은 대규모 시스템에서 노이즈가 너무 많아 실행 불가능하다
- 장기적 관점의 모니터링 결정이 중요하다 - 단기적 가용성을 희생해서라도 장기적 안정성을 확보한다

## 주요 프랙티스 및 권고사항
- 페이지 알림 작성 시 5가지 질문으로 검증: 미탐지 조건인가? 무시 가능한가? 사용자 영향이 확실한가? 조치 가능한가? 중복인가?
- 증상 기반 알림에 더 많은 노력을 투입하고, 원인 기반 알림은 디버깅 보조 수단으로 제한한다
- Bigtable 사례: 과도한 알림 시 SLO 목표를 일시적으로 완화하여 근본 문제 해결 시간을 확보한다
- Gmail 사례: 정형화된 대응이 필요한 페이지는 자동화 대상으로, 자동화 미실행은 기술 부채 신호이다
- 모니터링 시스템 복잡도를 최소화한다 - 분기 1회 미만 실행되는 수집/알림 설정은 제거 대상이다
- 분기별 페이지 빈도 통계를 관리자에게 보고하여 팀 건강 상태를 추적한다
- 10~12명 SRE 팀에 1~2명의 모니터링 전담 엔지니어를 배치한다

## 핵심 인용
> "Every time the pager goes off, I should be able to react with a sense of urgency. I can only react with a sense of urgency a few times a day before I become fatigued."

> "Pages with rote, algorithmic responses should be a red flag."

> "What's broken" indicates the symptom; the "why" indicates a cause.

## 관련 키워드
골든 시그널, 지연시간, 트래픽, 에러, 포화도, 화이트박스, 블랙박스, 페이지, 알림, 증상 기반 모니터링, SLO, 대시보드, 알림 피로
