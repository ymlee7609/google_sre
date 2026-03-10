# Eliminating Toil 요약

## 핵심 원칙
- Toil은 수작업적, 반복적, 자동화 가능한, 서비스 성장에 비례하는, 지속적 가치가 없는 운영 작업이다
- Google SRE는 Toil에 50% 이상 시간을 쓰지 않도록 제한한다
- Toil 측정이 Toil 감소의 첫 번째 단계이다
- Toil은 팀 사기, 혼란, 속도 저하, 전례 설정, 이직률 증가, 신뢰 위반을 초래한다
- Toil 제거는 엔지니어링 프로젝트로 취급해야 한다
- 자동화할 수 없는 작업이 남는 "Murphy-Beyer 효과"에 주의하라
- Toil 감소 프로젝트를 시작할 때 비즈니스 사례(ROI)를 제시하라

## 주요 프랙티스 및 권고사항
- Toil 분류 체크리스트: 수작업? 반복적? 자동화 가능? 전술적? O(n) 성장? 지속적 가치 없음?
- Toil 측정 방법: 설문조사, 시간 추적 도구, 티켓 데이터 분석
- Toil 우선순위 결정 요소: 비즈니스 영향도, 자동화 용이성, 시간 절감량
- 자동화 접근법: 완전 자동화보다 반자동화(사람의 판단 + 자동 실행)가 더 실용적일 수 있다
- 조직적 지원: Toil 감소를 성과 평가와 승진 기준에 포함하라
- 인수인계 시 Toil 부채도 함께 전달하고 문서화하라
- 새로운 서비스 도입 시 예상 Toil을 사전 평가하라
- Toil 제거를 "Toil Budget"으로 관리하여 팀별 목표를 설정하라

## 핵심 인용
> "Toil is seemingly unavoidable for any team that manages a production service. System maintenance inevitably demands a certain amount of rollouts, upgrades, restarts, alert triaging, and so forth."

> "The 50% rule isn't really a cap; it's a guarantee that SRE teams can spend at least half their time on engineering projects."

## 관련 키워드
Toil, 자동화, 운영 부하, Murphy-Beyer 효과, SRE 시간 배분, 반자동화, Toil 측정, 비즈니스 사례, 엔지니어링 프로젝트, 효율성
