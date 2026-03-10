# Monitoring 요약

## 핵심 원칙
- 모니터링의 4가지 목적: 알림, 진단, 시각화, 장기 추세 분석
- 메트릭과 구조화된 로그는 SRE의 근본적 모니터링 요구를 가장 잘 충족한다
- 메트릭은 실시간 알림에, 로그는 근본 원인 분석에 적합하다
- 모니터링 설정은 코드처럼 취급하여 버전 관리 시스템에 저장하라
- 모니터링 시스템의 컴포넌트는 느슨하게 결합(Loose Coupling)되어야 한다
- 수집된 모든 메트릭은 명확한 목적이 있어야 한다
- 모니터링 및 알림 로직도 테스트 대상이다

## 주요 프랙티스 및 권고사항
- 모니터링 시스템 선택 시 고려 사항: 속도(데이터 신선도), 계산(통계 함수 지원), 인터페이스(대시보드), 알림(심각도 분류)
- 4가지 골든 시그널(Golden Signals)을 기반으로 의존성 모니터링을 구축하라
- 의도된 변경(바이너리 버전, 커맨드라인 플래그, 동적 설정)을 모니터링하라
- 리소스 포화도(RAM, 디스크, CPU, 파일 디스크립터, 스레드 풀 등)를 추적하라
- 알림 기반 메트릭과 디버깅용 메트릭을 구분하여 설계하라
- 로그 기반 정보를 메트릭으로 이동시켜 알림 정확도를 높이는 것을 고려하라
- 모니터링 테스트 3계층: 바이너리 리포팅, 모니터링 설정, 알림 설정
- 조직 전체에서 일관된 기본 메트릭을 내보내면 자동으로 기본 모니터링이 제공된다
- Prometheus, statsd, OpenMetrics 같은 개방형 표준 활용을 권장한다

## 핵심 인용
> "Make sure to collect metrics that serve a particular purpose. That purpose may be to enable better capacity planning, assist in debugging, or directly notify you about problems."

> "If you're alerting based on metrics, it might be tempting to add more alerting based on logs. We still recommend metrics-based alerting in such cases."

## 관련 키워드
모니터링, 메트릭, 로그, Golden Signals, 대시보드, 알림, Prometheus, 포화도, 느슨한 결합, 모니터링 테스트, SLI, 가시성
