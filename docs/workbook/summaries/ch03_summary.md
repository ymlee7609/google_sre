# SLO Engineering Case Studies 요약

## 핵심 원칙
- SLO 문화는 일회성 솔루션이 아닌 지속적 프로세스이다
- "완벽은 좋음의 적(Perfect is the enemy of good)" - 완벽한 SLO를 기다리지 말고 시작하라
- SLO는 개발팀과 운영팀에게 공통의 성공 기준을 제공한다
- 클라우드 제공자와 고객 간 SLO를 공유하면 더 효과적인 협업이 가능하다
- SLO 도입에는 전략, 경영진 지원, 강력한 에반젤리즘, 쉬운 도입 패턴, 인내가 필요하다
- 각 조직은 자체 환경에 맞게 SLO를 맞춤화해야 한다
- SLO 자동화는 확산을 가속화하지만, 자동화 없이도 SLO 작성 자체만으로 가치가 있다

## 주요 프랙티스 및 권고사항
- **Evernote 사례**: 단순한 업타임 SLO(99.95%)로 시작하여 9개월 만에 v3까지 반복 개선
  - 월별 SLO 성과 리뷰와 6개월 SLO 검토 주기 설정
  - 유지보수 윈도우를 SLO 계산에서 다운타임으로 처리
  - 클라우드 제공자(Google)와 SLO 대시보드를 공유하여 공동 대응 체계 구축
- **Home Depot 사례**: VALET 프레임워크(Volume, Availability, Latency, Errors, Tickets) 개발
  - FiRE Academy(Fundamentals in Reliability Engineering) 교육 프로그램 운영
  - TPS Reports 자동화 프레임워크로 BigQuery 기반 SLO 데이터 수집
  - 1년 내 0에서 800개 서비스의 SLO 추적으로 확장
  - 챗봇 통합으로 채팅에서 직접 VALET 데이터 조회 가능
  - 배치 애플리케이션에도 VALET 프레임워크 적용
- 에반젤리즘: 블로그, Tech Talk, 워크숍, 스티커/티셔츠 등 다양한 마케팅 수단 활용

## 핵심 인용
> "Even when SLOs aren't perfect, they're good enough to guide improvements over time."

> "By providing a standard and defined way of measuring QoS, SLOs have allowed Evernote to better focus on how our service is running."

> "If we can introduce such a large change successfully, you can too."

## 관련 키워드
SLO, VALET, Error Budget, Evernote, Home Depot, FiRE Academy, TPS Reports, 에반젤리즘, 클라우드 제공자 협업, 배치 SLO, 문화 변화, 자동화
