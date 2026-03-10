# Embracing Risk 요약

## 핵심 원칙
- 극단적 신뢰성은 비용이 기하급수적으로 증가하며, 오히려 서비스에 해가 될 수 있다
- 99% 신뢰성의 스마트폰을 사용하는 유저는 99.99%와 99.999% 서비스 차이를 구분할 수 없다
- 서비스 리스크는 비계획 다운타임(unplanned downtime)으로 정량화한다
- Google은 시간 기반 가용성 대신 요청 성공률(request success rate) 기반 가용성을 사용한다
- 리스크 허용 범위는 기술적 결정이 아니라 비즈니스/프로덕트 결정이다
- 에러 버짓 = 1 - 가용성 목표. 이 예산을 혁신과 빠른 출시에 사용한다
- 인프라 서비스는 명시적으로 구분된 서비스 레벨을 제공하여 클라이언트가 비용/리스크를 선택하게 한다
- 가용성 목표는 최소값이자 최대값으로 취급한다 - 과도한 신뢰성도 낭비이다

## 주요 프랙티스 및 권고사항
- 분기별 가용성 목표를 설정하고 주간/일간 단위로 추적한다
- 에러 버짓 소진 시 릴리스를 일시 중단하고 시스템 안정성에 투자한다
- 서비스 유형별 리스크 허용 범위를 차별화한다 (예: 기업용 서비스 vs YouTube)
- 장애 유형의 영향도를 구분한다 (지속적 저비율 장애 vs 간헐적 전면 장애)
- 인프라 서비스는 저지연 클러스터와 처리량 클러스터를 분리 운영하여 비용을 최적화한다
- ISP 백그라운드 에러율(0.01%~1%)을 참고하여 서비스 에러율 목표를 설정한다
- 비용/수익 분석으로 추가 나인(nine)의 가치를 정량적으로 평가한다

## 핵심 인용
> "100% is probably never the right reliability target: not only is it impossible to achieve, it's typically more reliability than a service's users want or notice."

> "An outage is no longer a 'bad' thing - it is an expected part of the process of innovation."

> "Hope is not a strategy."

## 관련 키워드
리스크 관리, 에러 버짓, 가용성, 요청 성공률, SLO, 비용-편익 분석, 리스크 허용 범위, 서비스 레벨, 나인(nines), 혁신 속도
