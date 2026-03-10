# Handling Overload 요약

## 핵심 원칙
- 로드 밸런싱 정책이 아무리 효율적이어도 시스템의 일부는 결국 과부하 상태가 된다 - 우아한 과부하 처리가 신뢰성의 기본이다
- "초당 쿼리 수(QPS)"로 용량을 모델링하는 것은 빈약한 메트릭이다 - 가용 리소스(CPU, 메모리)를 직접 측정하라
- 과부하된 백엔드는 모든 트래픽을 거부하는 것이 아니라, 용량이 허락하는 만큼 수락하고 나머지를 우아하게 거부해야 한다
- 클라이언트 측 스로틀링이 없으면 요청 거부 자체의 리소스 소비로 인해 백엔드가 과부하될 수 있다
- 재시도는 직접 상위 레이어에서만 수행해야 한다 - 여러 레이어에서 재시도하면 조합적 폭발이 발생한다

## 주요 프랙티스 및 권고사항
- CPU 소비를 리소스 프로비저닝의 주요 신호로 사용한다 - 가비지 컬렉션 플랫폼에서 메모리 압력이 CPU 소비로 자연 변환
- 고객별 할당량(Per-Customer Limits): 협상된 사용량에 기반하여 고객별 쿼터를 설정하고, 과부하 시 위반 고객만 오류를 받도록 한다
- 적응형 스로틀링(Adaptive Throttling): 클라이언트가 최근 2분간의 요청(requests)과 수락(accepts)을 추적하여 requests가 K배(기본 2배) 이상이면 로컬 거부를 시작
- K 승수 조정: 1.1로 줄이면 10건 수락당 1건만 거부되어 더 공격적으로 동작
- 임계도(Criticality) 4단계: CRITICAL_PLUS(최고), CRITICAL(기본 프로덕션), SHEDDABLE_PLUS(일부 불가용 허용), SHEDDABLE(빈번한 불가용 허용)
- 임계도를 RPC 시스템의 일급 개념으로 통합하여 전파하고, 브라우저/모바일 클라이언트에 최대한 가깝게 설정
- 활용도 신호: 실행기 부하 평균(executor load average)으로 프로세스 내 활성 스레드 수를 지수 감쇠로 평활화
- 요청당 재시도 예산: 최대 3회로 제한하여 데이터센터 전체 과부하 시 실패를 호출자에게 전달
- 클라이언트당 재시도 예산: 재시도 비율을 10% 이하로 유지하여 과부하 시 성장을 1.1배로 제한
- 재시도 횟수 히스토그램: 백엔드가 다른 태스크도 과부하인지 판단하여 "재시도 금지" 오류를 반환
- 연결 부하 관리: 대규모 배치 작업의 연결 폭주를 배치 프록시로 차단하여 실제 백엔드를 보호
- 저하된 응답(Degraded Response) 제공: 정확도를 낮추거나 데이터를 줄인 응답으로 극단적 과부하 시에도 서비스 유지

## 핵심 인용
> "It's a common mistake to assume that an overloaded backend should turn down and stop accepting all traffic."

> "A well-behaved backend, supported by robust load balancing policies, should accept only the requests that it can process and reject the rest gracefully."

## 관련 키워드
과부하 처리, 적응형 스로틀링, 임계도, 고객별 쿼터, 재시도 예산, 클라이언트 측 스로틀링, 활용도 신호, 저하된 응답, 배치 프록시, 조합적 재시도 폭발
