# Managing Incidents 요약

## 핵심 원칙
- 효과적인 인시던트 관리는 장애 영향을 제한하고 정상 운영을 최대한 빨리 복구하는 핵심이다
- 비관리 인시던트의 3대 문제: 기술 문제에만 과몰입, 커뮤니케이션 부재, 무조율 단독 행동(Freelancing)
- Google의 인시던트 관리 시스템은 ICS(Incident Command System)에 기반한다
- 역할의 재귀적 분리(Recursive Separation of Responsibilities)가 개인에게 더 많은 자율성을 부여한다
- 인시던트 선언 기준을 사전에 명확히 정의해야 한다
- 인시던트를 일찍 선언하고 단순 해결 후 종료하는 것이 늦게 선언하는 것보다 낫다

## 주요 프랙티스 및 권고사항
- 4가지 핵심 역할: 인시던트 커맨더(총괄), 운영 리드(시스템 변경), 커뮤니케이션(외부 전달), 계획(장기 이슈/버그 관리)
- 인시던트 선언 기준: 두 번째 팀 투입 필요, 고객 가시적 장애, 1시간 집중 분석 후 미해결
- 실시간 인시던트 상태 문서(living document)를 유지하되, 기능적이면 지저분해도 된다
- 교대 시 명확한 핸드오프: "당신이 이제 인시던트 커맨더입니다, 확인해주세요"
- IRC(채팅)를 인시던트 대응의 통신 및 로그 수단으로 활용한다
- 인시던트 관리 프레임워크를 일상적 변경 관리에도 적용하여 역량을 유지한다
- 재난 복구 훈련과 역할극으로 인시던트 관리 역량의 퇴화를 방지한다
- 최우선 모범 사례 7가지: 우선순위 정하기, 준비하기, 신뢰하기, 자기성찰, 대안 고려, 연습, 역할 교체

## 핵심 인용
> "Stop the bleeding, restore service, and preserve the evidence for root-causing."

> "It is better to declare an incident early and then find a simple fix and close out the incident."

## 관련 키워드
인시던트 관리, ICS, 인시던트 커맨더, 운영 리드, 커뮤니케이션, 핸드오프, 실시간 문서, War Room, IRC, 역할 분리, Freelancing
