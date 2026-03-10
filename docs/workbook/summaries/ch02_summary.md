# Implementing SLOs 요약

## 핵심 원칙
- SLO는 SRE 실천의 핵심이며, 신뢰성에 대한 데이터 기반 의사결정의 기반이다
- 100% 신뢰성은 잘못된 목표 - 사용자 경험의 99.999%와 100% 차이는 미미하지만 비용은 극단적이다
- SLI(Service Level Indicator)는 좋은 이벤트 / 전체 이벤트 비율로 표현하는 것이 가장 효과적이다
- SLI 사양(specification)과 구현(implementation)을 구분하여 관리하라
- Error Budget = 100% - SLO 목표치, 이 예산을 의사결정 도구로 활용한다
- 첫 SLO는 완벽하지 않아도 된다 - 측정 시작 후 반복 개선이 핵심이다
- 4주 롤링 윈도우가 범용적으로 적합한 SLO 기간이다
- 모든 이해관계자(제품 관리자, 개발팀, SRE팀)의 합의가 필수적이다
- SLO 위반 시 대응 방안을 명시한 Error Budget Policy가 반드시 필요하다

## 주요 프랙티스 및 권고사항
- 서비스 유형별 SLI 선택: Request-driven(가용성, 지연시간), Pipeline(신선도, 정확성, 커버리지), Storage(내구성)
- SLO 결정 매트릭스 활용: SLO 달성 여부 x Toil 수준 x 고객 만족도 조합으로 조치 결정
- 복수 등급의 SLO 설정 권장(예: 90% 요청 < 100ms, 99% 요청 < 400ms)
- Critical User Journey(핵심 사용자 여정) 기반 SLO 설계로 사용자 중심 측정
- 요청 중요도에 따른 버킷팅(CRITICAL, HIGH_FAST, HIGH_SLOW, LOW, NO_SLO)
- SLO 문서와 Error Budget Policy를 공식적으로 문서화하고 정기 검토하라
- 대시보드와 보고서를 통해 SLO 준수 현황을 가시화하라
- 지원 티켓 수와 Error Budget 소진의 상관관계를 분석하여 SLO 품질을 검증하라

## 핵심 인용
> "Our experience has shown that 100% reliability is the wrong target."

> "SREs' core responsibilities aren't merely to automate 'all the things' and hold the pager. Their day-to-day tasks and projects are driven by SLOs."

> "One could even claim that without SLOs, there is no need for SREs."

## 관련 키워드
SLO, SLI, Error Budget, Error Budget Policy, 가용성, 지연시간, 신선도, 내구성, 롤링 윈도우, Critical User Journey, 이해관계자 합의, 의사결정 매트릭스
