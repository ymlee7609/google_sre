# Organizational Change Management in SRE 요약

## 핵심 원칙
- 변화는 유일한 상수이며, SRE 팀은 빠른 혁신과 변화의 큰 수용을 특징으로 한다
- 조직 변경 관리(organizational change management)와 변경 통제(change control)는 별개 개념이다
- 단일한 변경 관리 모델이 모든 상황에 보편적으로 적용될 수는 없다
- 하나의 병목을 제거하면 다음 병목이 드러나므로, 변화는 순환적(cyclical) 과정이다
- 점진적 변화가 관리하기 훨씬 쉽다 - "완벽한" 솔루션으로 한 번에 도약하는 것은 너무 큰 단계이다
- 마이그레이션 비용이 거의 0에 가깝고 혜택이 명확해야 채택이 일어난다
- 채택(adoption)이 네트워크 효과를 유발한다 - 공통 도구의 규모가 커질수록 점진적 개선의 가치도 증가한다

## 주요 프랙티스 및 권고사항
- **주요 변경 관리 이론과 SRE 적용**:
  - **Lewin의 3단계 모델** (해빙-변화-동결): 거시적 조직 변화 계획에 유용
  - **McKinsey 7-S**: 시스템 관리 → SRE 전환 시 유용 (구조, 전략, 시스템, 기술, 스타일, 인력, 공유 가치)
  - **Kotter의 8단계 프로세스**: SRE에 가장 적합 - 긴급성 인식, 선도 연합, 전략적 비전, 장벽 제거, 단기 성과, 가속화, 변화 정착
  - **Prosci ADKAR**: 글로벌 분산 팀 간 변화 조율에 유용 (인식, 욕구, 지식, 능력, 강화)
  - **감정 기반 모델**: 관리자가 변화 중 팀원의 감정 반응을 이해하는 데 유용
  - **PDCA/Deming 사이클**: 프로세스 개선에는 적합하나 조직 변화에는 인간적 측면이 부족
- **사례 1 - Waze 확장** (Kotter 모델 적용):
  - 메시지 큐 교체: 긴급성 인식 → 2명 SRE + 시니어 엔지니어 연합 → 커스텀 솔루션 구축
  - 불필요한 메시지 정리와 압축 레이어로 임시 운영 여유 확보 후 신규 시스템 프로토타입 개발
  - 이중 쓰기(dual-write)를 통한 점진적 마이그레이션, 초기 성과로 투자 정당화
  - 배포 프로세스 개선: 마이크로서비스 프레임워크 → Spinnaker CI/CD → 95% 이상 채택
  - 대시보드 구축으로 릴리스 가시성 제공 → 개발팀의 자발적 채택 촉발
- **사례 2 - 공통 도구 채택** (ADKAR 모델 적용):
  - 문제: 동일 문제에 대해 여러 독립적 솔루션이 난립 (모니터링, 릴리스, 인시던트 대응 등)
  - 65+ 제안 프로젝트에서 시작하여 소수의 검증된 주제로 범위 축소
  - 초기 80/20 가상 팀 접근은 실패 → 소규모(6-10명) 전담 중앙화 팀으로 전환
  - Viceroy 모니터링: 팀별 커스텀 → 공통 프레임워크 → 제로 설정 표준 대시보드
  - "지식-능력 격차(knowledge-to-ability gap)": 기존 솔루션에서 새 솔루션으로의 전환 비용이 항상 높게 인식됨
  - 성공 비결: 제품 개발과 동일한 수준의 일정/지원, 투명한 개발 과정, 최악의 채택자를 먼저 타겟팅
- **핵심 교훈**:
  - 풀뿌리 변화도 SRE-개발-경영진 간 긴밀한 협업이 필요하다
  - "훌륭하게 만들면 사람들이 자연히 모일 것"이라는 가정은 맞지 않는다
  - 마이그레이션 설계는 백지 설계보다 복잡하지만, 현실에서 가장 어려운 엔지니어링 작업이다

## 핵심 인용
> "Incremental change is much easier to manage. Jumping straight to the 'perfect' solution is too large a step to take all at once."

> "Our initial thought that 'if you build something great, people will naturally flock to it' didn't hold true."

> "Migration costs need to be nearly zero and the benefits need to be clear to the team, to individuals, and to the company."

## 관련 키워드
조직 변경 관리, Kotter 8단계, ADKAR, Lewin, Waze, 마이그레이션, 점진적 변화, 공통 도구, 네트워크 효과, 채택, Spinnaker, Viceroy, 병목 제거, 풀뿌리 변화
