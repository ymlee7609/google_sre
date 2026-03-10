# Data Processing Pipelines 요약

## 핵심 원칙
- 데이터 처리 파이프라인은 종종 비즈니스 크리티컬하며, 지연되거나 부정확한 데이터는 사용자에게 영향을 준다
- 파이프라인 설계 시 신뢰성, 확장성, 모니터링을 처음부터 고려해야 한다
- 데이터 처리에는 배치와 스트리밍 두 가지 주요 패러다임이 있다
- 파이프라인 SLO는 신선도(freshness), 정확성(correctness), 커버리지(coverage)로 측정한다
- 파이프라인의 복잡성은 시간이 지남에 따라 증가하므로 단순성을 유지하려는 노력이 필요하다

## 주요 프랙티스 및 권고사항
- 파이프라인 모니터링: 처리량, 지연시간, 에러율, 데이터 신선도를 추적하라
- 멱등성(Idempotency) 설계: 파이프라인이 재실행되어도 동일한 결과를 생성하도록 설계하라
- 체크포인팅: 장애 시 전체 재처리 없이 중단 지점부터 재개할 수 있도록 하라
- Spotify 사례: 대규모 데이터 처리 파이프라인의 신뢰성 확보 전략
  - 이벤트 전달 시스템의 신뢰성 보장
  - 파이프라인 소유권 명확화
  - 데이터 품질 검증 단계 도입
- 워크플로우 시스템을 활용한 파이프라인 관리 자동화
- 파이프라인 카나리: 새 버전을 일부 데이터에만 먼저 적용하여 검증
- 백프레셔(Backpressure) 메커니즘으로 과부하 방지
- 데드레터 큐(Dead Letter Queue)로 처리 실패한 레코드 관리

## 핵심 인용
> "Delayed or incorrect data in your pipeline can manifest in user-facing issues that are expensive, labor-intensive, and time-consuming to fix."

> "Data processing pipelines can turn these often unbounded, unordered, global-scale data sets into structured, indexed storage that can help inform crucial business decisions."

## 관련 키워드
데이터 파이프라인, 배치 처리, 스트리밍, 신선도, 정확성, 커버리지, 멱등성, 체크포인팅, 백프레셔, 데드레터 큐, Spotify, 워크플로우
