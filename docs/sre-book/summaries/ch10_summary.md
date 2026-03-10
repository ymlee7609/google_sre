# Practical Alerting from Time-Series Data 요약

## 핵심 원칙
- Borgmon은 커스텀 스크립트 기반 점검-알림 모델을 시계열 데이터 수집과 중앙화된 규칙 평가로 대체했다
- 시계열 데이터는 (타임스탬프, 값) 쌍으로 저장되며, 레이블셋(key=value)으로 고유하게 식별된다
- 카운터(단조 증가)가 게이지(임의 값)보다 선호된다 - 수집 간격 사이의 활동을 놓치지 않는다
- Borgmon 규칙은 시계열에서 새 시계열을 계산하는 대수 표현식이다
- 집계(Aggregation)가 분산 환경 규칙 평가의 초석이다
- 모니터링 유지 비용은 서비스 규모에 대해 서브리니어하게 확장되어야 한다
- 화이트박스 모니터링만으로는 불완전하다 - Prober를 통한 블랙박스 검증이 필수적이다
- 알림은 "플래핑" 방지를 위해 최소 2회 규칙 평가 주기 동안 유지되어야 발송된다

## 주요 프랙티스 및 권고사항
- /varz HTTP 핸들러로 표준화된 메트릭 형식 수집 - 계측 추가 장벽을 최소화한다
- 시계열 아레나: 인메모리 고정 크기 블록에 약 12시간 데이터를 유지하고, TSDB에 아카이빙한다
- Borgmon 계층 구조: 데이터센터별 Borgmon이 수집하고, 글로벌 Borgmon이 상위 집계를 수행한다
- 알림 규칙 예시: 에러 비율 > 1%이면서 에러 수 > 1/s일 때, 2분간 지속되면 페이지 발송
- Alertmanager: 알림 억제, 중복 제거, 라벨 기반 팬인/팬아웃을 중앙에서 처리한다
- 변수 이름 명명 규칙: "집계수준:변수명:연산" (예: dc:http_errors:ratio_rate10m)
- 규칙 라이브러리 템플릿으로 반복을 줄이고, 단위/회귀 테스트로 규칙 동작을 검증한다
- Prometheus, Riemann, Bosun 등 오픈소스 도구가 Borgmon과 유사한 접근법을 제공한다

## 핵심 인용
> "May the queries flow, and the pager stay silent." - Traditional SRE blessing

> "Borgmon is really just a programmable calculator, with some syntactic sugar that enables it to generate alerts."

## 관련 키워드
Borgmon, 시계열, varz, 레이블, 카운터, 게이지, 집계, Alertmanager, Prober, TSDB, Prometheus, 규칙 평가, 화이트박스 모니터링
