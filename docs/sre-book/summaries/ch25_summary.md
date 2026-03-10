# Data Processing Pipelines 요약

## 핵심 원칙
- 주기적 파이프라인은 처음에는 안정적이지만, 유기적 성장과 변화가 불가피하게 시스템에 스트레스를 가한다
- 데이터 처리 문제가 연속적이거나 연속적으로 성장할 것이라면, 주기적 파이프라인 대신 Workflow 같은 연속 처리 기술을 사용하라
- 빅데이터의 핵심 돌파구인 "부끄러울 정도로 병렬적" 알고리즘도 불균등한 청크(hanging chunk) 문제에 취약하다
- 파이프라인 깊이(depth)는 체인된 프로그램 수를 측정하며, 깊은 파이프라인은 수십에서 수백 프로그램에 달할 수 있다

## 주요 프랙티스 및 권고사항
- 주기적 파이프라인의 문제점: 데드라인 초과, 리소스 고갈, 행잉 청크, 운영 부하 증가
- 불균등 작업 분배: 고객별 파티셔닝 시 일부 청크가 훨씬 커서 전체 파이프라인 완료가 최악의 청크에 종속
- 행잉 청크 대응의 함정: 작업을 즉시 죽이고 재시작하면 체크포인팅 없이 모든 청크의 작업이 처음부터 재시작
- 분산 환경의 한계: 배치 작업은 낮은 우선순위로 실행되어 선점(preemption) 위험, 실행 간격 축소 시 겹침 발생
- 모아레 부하 패턴(Moire Load Pattern): 두 개 이상의 파이프라인이 동시에 실행되어 공유 리소스를 동시 소비하는 패턴
- 선더링 허드: 수천 워커가 동시에 시작되어 서버, 클러스터 서비스, 네트워크를 압도
- 모니터링 한계: 주기적 파이프라인은 보통 완료 시에만 메트릭을 보고하여 실행 중 장애 대응이 어려움
- Google Workflow: 2003년 개발된 리더-팔로워 패턴 기반 연속 처리 시스템으로, 정확히 한 번(exactly-once) 의미론 보장
- Workflow의 MVC 패턴: Model(Task Master - 모든 작업 상태를 메모리에 유지), View(워커 - 완전 무상태), Controller(스케일링, 스냅샷, 롤백 등)
- 4중 정확성 보장: (1) 설정 태스크 기반 작업 장벽 (2) 유효한 리스를 가진 워커만 커밋 가능 (3) 출력 파일 이름 고유성 (4) 서버 토큰으로 Task Master 검증
- 비즈니스 연속성: Spanner에 저널을 저장하고, Chubby로 쓰기 권한 선출, 글로벌 참조 태스크로 페일오버 자동화
- 파이프라인 설계 시 초기에 확인할 사항: 예상 성장 궤적, 설계 변경 수요, 추가 리소스, 지연시간 요구사항

## 핵심 인용
> "If a data processing problem is continuous or will organically grow to become continuous, don't use a periodic pipeline."

> "Nothing is harder on cluster infrastructure and the SREs responsible for a cluster's various services than a buggy 10,000 worker pipeline job."

## 관련 키워드
데이터 처리 파이프라인, 주기적 파이프라인, 연속 파이프라인, Workflow, Task Master, 정확히 한 번, 모아레 부하 패턴, 선더링 허드, 행잉 청크, MVC 패턴, Spanner, Chubby
