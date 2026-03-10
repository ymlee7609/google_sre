# SRE: Reaching Beyond Your Walls 요약

## 핵심 원칙
- 신뢰성은 모든 시스템의 가장 중요한 기능이다 - 신뢰할 수 없으면 사용자가 떠난다
- 모니터링이 아닌 사용자가 시스템의 신뢰성을 결정한다 - 사용자 경험이 유일한 신뢰성 척도이다
- 플랫폼을 운영한다면 신뢰성은 파트너십이다 - 고객의 선택이 고객이 경험하는 신뢰성에 직접 영향을 미친다
- 중요한 시스템은 결국 모두 플랫폼이 된다 - API 통합은 피할 수 없는 진화 단계이다
- 고객이 어려움을 겪으면 혁신 예산이 줄어든다 - 고객 지원에 소비되는 에너지는 시스템 발전에 투자할 수 없다
- SLO가 없으면 고객은 자체적으로 SLO를 만들고, 충족하지 못할 때까지 알려주지 않는다
- 네트워크 효과로 인해 사용자가 없는 시스템은 가치가 없다

## 주요 프랙티스 및 권고사항
- **고객과 SRE를 실천하는 5단계**:
  - **Step 1 - SLO/SLI로 대화하라**: 고객이 SLI를 측정하고 SLO 기반으로 알림하도록 도와라. 공유 지표를 통해 생산적인 대화가 가능해진다
  - **Step 2 - 모니터링 감사 및 공유 대시보드 구축**: 고객 측정 항목의 절반은 SLO에 무관하다. 불필요한 알림을 끄고 SLI 후보를 선별하라. SLO의 미측정 영역을 식별하고 커버하라
  - **Step 3 - 측정하고 재협상하라**: 1-2개월 데이터를 수집한 후 현실적인 SLO를 재설정하라. "5 nines" 환상을 깨고 실제 99.5-99.9%에 기반한 목표를 수립하라. 핵심 질문: 사용자가 현재 성능에 만족하는가?
  - **Step 4 - 설계 리뷰와 리스크 분석**: 숨겨진 SPOF를 찾고, 에러 버짓 소비량 기준으로 이슈를 순위화하라. 고객이 플랫폼을 어떻게 소비하는지, 어떤 신뢰성 실수를 하는지 파악하라
  - **Step 5 - 연습, 연습, 연습**: Wheel of Misfortune, 재해 복구 테스트, 공동 포스트모템을 실시하라. 위기 시 효과적인 커뮤니케이션 근육 기억을 형성하라
- **고객 선택 전략** (모든 고객과 깊이 참여할 수 없으므로):
  - 매출 커버리지: 최소 고객 수로 XX% 매출을 커버
  - 기능 커버리지: 최소 고객 수로 XX% 플랫폼 기능을 커버
  - 워크로드 커버리지: 주요 사용 사례별 코호트에서 1-2명 고객을 샘플링
  - 하나의 접근 방식을 선택하고 일관되게 유지하라 - 혼합은 혼란과 과부하를 초래한다
- **Peak-end rule**: 사용자는 최악의 순간과 마지막 순간의 경험을 기억한다 - 고객의 불안정 인식이 곧 현실이다
- **내부 플랫폼 팀도 동일하게 적용**: 사내 고객도 외부 고객과 동일한 동학을 겪으며, 오히려 먼저 직면한다

## 핵심 인용
> "If a system isn't reliable, users won't trust it. If users don't trust a system, when given a choice, they won't use it."

> "Your monitoring, logs, and alerting are valuable only insofar as they help you notice problems before your customers do."

> "In the absence of a stated SLO, your customer will inevitably invent one and not tell you until you don't meet it!"

## 관련 키워드
고객 신뢰성, CRE, SLO 공유, 플랫폼 신뢰성, 파트너십, 공동 포스트모템, 설계 리뷰, SPOF, 에러 버짓, 매출 커버리지, Peak-end rule, 네트워크 효과
