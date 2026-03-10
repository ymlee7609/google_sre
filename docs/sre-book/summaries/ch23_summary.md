# Managing Critical State: Distributed Consensus for Reliability 요약

## 핵심 원칙
- 리더 선출, 중요 공유 상태, 분산 잠금이 필요할 때는 반드시 공식적으로 증명되고 철저히 테스트된 분산 합의 시스템을 사용하라
- 하트비트와 가십 프로토콜 같은 비공식적 접근은 실제 운영에서 항상 신뢰성 문제를 초래한다
- CAP 정리: 네트워크 파티션은 불가피하므로, 일관성(Consistency)과 가용성(Availability) 사이의 트레이드오프를 이해해야 한다
- 시스템 설계자는 신뢰성이나 성능을 위해 정확성을 희생할 수 없다 - 특히 핵심 상태에 대해서는
- 분산 합의 알고리즘이 "느리다"는 통념은 사실이 아니다 - Google의 핵심 시스템에서 실제로 매우 효과적으로 작동한다

## 주요 프랙티스 및 권고사항
- 분산 합의가 필요한 문제: 리더 선출, 그룹 멤버십, 분산 잠금/리스, 신뢰성 있는 큐/메시징, 일관된 공유 상태
- Paxos 프로토콜: 다수결(majority)에 기반하여 합의를 달성 - 두 다수결은 최소 한 노드에서 겹치므로 두 다른 값이 동시에 커밋될 수 없다
- 복제 상태 머신(RSM): 합의 알고리즘 위에 구축된 시스템으로, 동일한 순서로 동일한 연산을 여러 프로세스에서 실행
- 사례 연구 1 - 스플릿 브레인: 단순 하트비트 타임아웃으로 리더 선출 시도 시 네트워크 장애로 양쪽이 모두 마스터를 주장하거나 둘 다 다운
- 사례 연구 2 - 수동 개입 필요: 자동 장애 조치가 인간 에스컬레이션에 의존하면 가용성이 저하되고 운영 부하가 증가
- 사례 연구 3 - 결함 있는 그룹 멤버십: 가십 프로토콜 기반 클러스터가 네트워크 파티션 시 양쪽에서 독립적으로 마스터를 선출하여 데이터 손상
- 합의 서비스: Zookeeper, Consul, etcd 등 - 라이브러리가 아닌 서비스로 제공하면 애플리케이션 유지보수자의 부담 경감
- 리더 선출 패턴: 단일 리더가 특정 작업을 수행하고, 리더 장애 시 합의 알고리즘으로 새 리더 선출 - GFS, Bigtable에서 사용
- 쿼럼 리스(Quorum Leases): 읽기 리스를 쿼럼에 부여하여 강한 일관성의 로컬 읽기를 가능하게 하되 쓰기 성능 일부 희생
- Multi-Paxos: 강한 리더 프로세스를 사용하여 안정 상태에서 합의에 한 번의 왕복만 필요
- 결투 제안자(Dueling Proposers) 방지: 무작위성을 도입하고 적절한 타임아웃/백오프 전략 사용
- ACID vs BASE: 결과적 일관성(eventual consistency)은 놀라운 결과를 초래할 수 있으며, 클록 드리프트와 네트워크 파티션에 취약

## 핵심 인용
> "Ad hoc means of solving these sorts of problems will always have reliability problems in practice."

> "System designers cannot sacrifice correctness in order to achieve reliability or performance, particularly around critical state."

## 관련 키워드
분산 합의, Paxos, Raft, CAP 정리, 복제 상태 머신, 리더 선출, 스플릿 브레인, 쿼럼 리스, Chubby, Zookeeper, ACID, BASE, 결과적 일관성, Spanner
