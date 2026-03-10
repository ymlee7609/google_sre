# The Production Environment at Google 요약

## 핵심 원칙
- Google은 자체 설계한 데이터센터에서 독자적 전력, 냉각, 네트워킹, 컴퓨팅 하드웨어를 사용한다
- Machine(하드웨어)과 Server(소프트웨어)를 명확히 구분하는 용어 체계를 사용한다
- 데이터센터 토폴로지: 머신 -> 랙 -> 행 -> 클러스터 -> 데이터센터 -> 캠퍼스
- Borg는 클러스터 수준에서 작업을 관리하는 분산 클러스터 운영체제이다
- 스토리지 계층: D(디스크) -> Colossus(클러스터 파일시스템) -> Bigtable/Spanner/Blobstore
- Jupiter 네트워크 패브릭은 최대 1.3 Pbps의 이분 대역폭을 지원한다
- B4 소프트웨어 정의 네트워크가 데이터센터 간 백본을 구성한다
- GSLB(Global Software Load Balancer)는 DNS, 서비스, RPC 세 수준에서 로드 밸런싱을 수행한다

## 주요 프랙티스 및 권고사항
- 리소스 할당을 Borg에 위임하여 하드웨어 장애를 추상화하고 자동 복구를 달성한다
- BNS(Borg Naming Service)를 통해 IP/포트 대신 논리적 이름으로 태스크에 접근한다
- Borg는 장애 도메인을 고려한 빈패킹으로 단일 장애 지점을 방지한다
- Chubby 분산 락 서비스로 마스터 선출과 일관성 있는 데이터 저장을 처리한다
- Borgmon으로 메트릭 수집, 알림 설정, 리소스 소비 추이 분석을 수행한다
- Protocol Buffers(protobuf)를 RPC 통신의 직렬화 형식으로 사용 (XML 대비 20~100배 빠름)
- N+2 이상의 리던던시로 업데이트 중 및 장애 발생 시에도 피크 로드 처리 가능하도록 설계한다
- 데이터 접근 지연 최소화를 위해 Bigtable 등 데이터를 지역별로 복제한다

## 핵심 인용
> "Machines can run any server, so we don't dedicate specific machines to specific server programs."

> "If a task tries to use more resources than it requested, Borg kills the task and restarts it."

## 관련 키워드
Borg, Colossus, Jupiter, B4, GSLB, BNS, Chubby, Borgmon, Protocol Buffers, gRPC, Bigtable, Spanner, 데이터센터 토폴로지, N+2 리던던시
