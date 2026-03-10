# Identifying and Recovering from Overload 요약

## 핵심 원칙
- 운영 부하(operational load)는 페이지, 티켓, 지속적 운영 책임의 세 가지 유형으로 구성된다
- 운영 과부하는 긴급한 이슈가 지속적으로 프로젝트 작업을 선점하여 핵심 우선순위에 진전을 이룰 수 없는 상태이다
- Google SRE 팀은 운영 작업을 엔지니어 시간의 50% 이내로 제한한다
- 인지된 과부하(perceived overload)는 실제 과부하와 동일한 영향을 미친다 - 객관적/주관적 구분은 중요하지 않다
- 과부하는 직업적 스트레스로 건강과 생산성에 악영향을 미치며, 자기 강화 순환(vicious cycle)을 만든다
- 심리적 안전감(psychological safety)의 저하는 협업 중단, 정보 공유 감소, 비효율 심화로 이어진다
- 업무가 적절히 우선순위화되지 않으면 모든 작업이 동등하게 긴급해 보여 과부하가 발생한다
- 팀원에게 더 많은 통제권과 권한을 부여하면 인지된 과부하가 감소한다

## 주요 프랙티스 및 권고사항
- **사례 1 - 팀 절반 이탈 시 업무 과부하**:
  - 팀 전원이 모든 책임을 나열하고 모든 항목을 트리아지하라
  - 매몰 비용 오류(sunk cost fallacy)를 인식하고 과감히 작업을 드롭하라
  - 의심스러우면 작업을 드롭하되 2차 트리아지 대상으로 표시하라
  - 낮은 노력의 자동화와 셀프서비스 문서화로 운영 부하를 줄여라
  - 2주마다 인터럽트를 트리아지하고, 팀원당 열린 티켓 10개 이하를 유지하라
- **사례 2 - 인지된 과부하**:
  - 단기: 스트레스 해소, 심리적 안전감 개선, 스팸 알림 감사/제거, 알림 관대하게 음소거
  - 중기: 운영 작업을 온콜 시간으로 제한, 서비스 반환, 상호 교육, 경청 이벤트 개최
  - 장기: SLO를 백엔드 SLO와 정렬, 서비스 균일화로 인지 부하 감소
- **과부하 증상 인식**: 사기 저하, 장시간 근무, 잦은 질병, 비정상적 작업 큐, 불균형 메트릭
- **핵심 메트릭**: 단일 이슈 해결 소요 시간, Toil에 소요된 시간 비율, 온콜 세션 후 이슈 해결 일수
- **심리사회적 스트레서 식별**: 팀이 통제할 수 있는 요소(백로그 크기, 페이지 음소거)에 집중하라
- **분기별 우선순위 재검토**: 팀이 함께 기존 및 미래 작업을 계획하고 우선순위를 정하라
- **인터럽트 없는 시간 확보**: 온콜이 아닌 시간을 캘린더에 예약하여 근본 원인 조사와 자동화에 집중하라
- **미래 보호**: 팀 부하를 평가하는 메트릭을 수립하고 정기적으로 검토하라
- **반복적 Toil 감소 프로젝트 우선순위 상향**: 과부하 상태일수록 미래 Toil을 줄이는 프로젝트에 더 투자하라

## 핵심 인용
> "Perceived overload is, in fact, overload, and has as much impact to a team as work overload caused by other factors."

> "When it comes to fixing a dysfunctional team, first and foremost, individual team members need to regain their sense of psychological safety."

> "In order to keep a team's workload in balance, it's important to constantly monitor (perceived or nonperceived) overload."

## 관련 키워드
운영 과부하, 인지된 과부하, 심리적 안전감, 인터럽트 관리, Toil, 트리아지, 팀 건강, 매몰 비용 오류, 온콜, 스트레스 관리, 알림 튜닝, 참여적 관리
