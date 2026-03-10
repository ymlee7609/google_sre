# Being On-Call 요약

## 핵심 원칙
- 온콜의 양(quantity)과 질(quality) 두 축의 균형이 필수적이다
- SRE 시간의 최대 25%만 온콜에 할당하고, 최소 50%는 엔지니어링 프로젝트에 투입한다
- 온콜 시프트당 최대 2건의 인시던트가 상한선이다 - 인시던트 하나에 약 6시간(근본 원인 분석, 복구, 포스트모템)이 소요된다
- 이성적이고 숙고적인(deliberate) 사고가 직관적이고 자동적인 반응보다 인시던트 대응에 더 효과적이다
- 스트레스 호르몬은 인지 기능을 손상시키고 최적이 아닌 의사결정을 유발한다
- 운영 과부하(overload)와 운영 과소부하(underload) 모두 위험하다
- 다중 사이트 팀의 "follow the sun" 로테이션이 야간 근무의 건강 영향을 제거한다
- 호출기 반환(give back the pager)은 SRE 팀의 최후 수단이지만, 건전한 팀 간 긴장의 표현이다

## 주요 프랙티스 및 권고사항
- 단일 사이트 팀 최소 8명, 다중 사이트 팀 각 사이트 최소 6명으로 25% 온콜 규칙을 준수한다
- 온콜 엔지니어에게 필요한 3대 리소스: 명확한 에스컬레이션 경로, 체계적 인시던트 관리 절차, 비난 없는 포스트모템 문화
- 응답 시간은 SLO에 연계한다 - 4나인 가용성이면 분기당 약 13분 다운타임 허용, 응답은 분 단위
- 모든 SRE가 분기당 최소 1~2회 온콜을 수행하여 프로덕션 감각을 유지한다
- Wheel of Misfortune와 DiRT(Disaster Recovery Training)로 정기적 훈련을 실시한다
- 잘못 설정된 모니터링이 운영 과부하의 주요 원인이다 - 알림/인시던트 비율을 1:1에 근접시킨다
- 과부하 시 경험 많은 SRE를 임시 파견하여 팀에 여유를 제공한다
- 온콜 보상은 금전 또는 대체 휴가로 제공하되, 과도한 온콜 방지를 위해 상한선을 설정한다

## 핵심 인용
> "We strongly believe that the 'E' in 'SRE' is a defining characteristic of our organization."

> "Being out of touch with production for long periods of time can lead to confidence issues."

## 관련 키워드
온콜, 25% 규칙, 인시던트 관리, 에스컬레이션, 운영 과부하, 운영 과소부하, follow the sun, Wheel of Misfortune, DiRT, 호출기 반환, 보상
