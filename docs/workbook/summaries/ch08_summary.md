# On-Call 요약

## 핵심 원칙
- 온콜은 SRE의 핵심 특성 중 하나이며, 정해진 시간 동안 프로덕션 인시던트에 적절한 긴급도로 대응하는 것이다
- 온콜 엔지니어는 인시던트 진단, 완화, 수정, 에스컬레이션을 수행한다
- 온콜은 지속 가능해야 한다 - 번아웃을 방지하기 위해 운영 부하의 상한선을 설정하라
- Google에서는 온콜 시간의 최소 50%를 엔지니어링에 할애하도록 보장한다
- 소규모 팀도 지속 가능한 온콜 체계를 구축할 수 있다
- 온콜 로테이션 설계 시 공정성, 예측 가능성, 지식 공유를 고려하라

## 주요 프랙티스 및 권고사항
- 최소 온콜 인원: 이상적으로 8명 이상, 최소 2명의 활성 온콜러(프라이머리 + 세컨더리)
- 소규모 팀 전략: 로테이션 확장(다른 팀과 공유), 다중 사이트 활용, 에스컬레이션 경로 명확화
- 온콜 핸드오프: 다음 교대자에게 활성 인시던트, 잠재적 문제, 최근 변경사항 전달
- 페이징 부하 관리: 교대 당 2건 이하의 인시던트가 이상적, 너무 많으면 근본 원인 해결이 필요
- 온콜 보상: 금전적 보상이나 대체 휴무를 통해 온콜 부담을 인정하라
- 플레이북(Playbook) 작성: 일반적인 알림에 대한 대응 절차를 문서화하라
- 온콜 교육: 그림자 온콜(Shadow On-Call), 재해 역할극(Wheel of Misfortune) 등 실전 훈련 활용
- 운영 부하 추적: 페이징 빈도, 인시던트당 대응 시간, 야간 호출 비율 등을 측정하라
- Evernote 사례: 제한된 인원으로 온콜 체계 구축, 클라우드 이전과 SLO 도입으로 알림 품질 개선

## 핵심 인용
> "Being on-call means being available during a set period of time, and being ready to respond to production incidents during that time with appropriate urgency."

> "On-call is a large and complex topic, saddled with many constraints and a limited margin for trial and error."

## 관련 키워드
온콜, 로테이션, 에스컬레이션, 페이징, 플레이북, 번아웃, Shadow On-Call, Wheel of Misfortune, 인시던트 대응, 지속 가능성
