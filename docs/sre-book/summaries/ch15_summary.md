# Postmortem Culture: Learning from Failure 요약

## 핵심 원칙
- 포스트모템은 인시던트를 문서화하고, 근본 원인을 이해하며, 재발 방지 조치를 수립하기 위한 필수 도구이다
- 비난 없는 포스트모템(Blameless Postmortem)은 SRE 문화의 핵심 원칙이다
- 포스트모템 작성은 처벌이 아니라 전체 회사를 위한 학습 기회이다
- "사람은 고칠 수 없지만, 시스템과 프로세스는 고칠 수 있다"
- 검토되지 않은 포스트모템은 존재하지 않는 것과 같다
- 포스트모템 문화는 지속적 배양과 강화가 필요하다 - 한 번 만들어지지 않는다
- 의료 및 항공 산업에서 유래한 비난 없는 문화는 모든 실수를 시스템 강화 기회로 본다

## 주요 프랙티스 및 권고사항
- 포스트모템 트리거 기준: 사용자 가시적 다운타임, 데이터 손실, 온콜 개입(롤백 등), 해결 시간 초과, 모니터링 실패
- 사건 발생 전에 포스트모템 기준을 미리 정의한다
- 포스트모템 검토 기준: 핵심 데이터 수집 여부, 영향 평가 완전성, 근본 원인 깊이, 조치 계획 적절성
- 조치 항목의 후속 이행에 대해 본인과 타인에게 책임을 물어야 한다
- 포스트모템 문화 강화 활동: 월간 뉴스레터, 포스트모템 읽기 클럽, Wheel of Misfortune 역할극
- 실시간 협업 도구(Google Docs 등)로 신속한 데이터 수집과 크라우드소싱 솔루션을 가능하게 한다
- 포스트모템 작성을 공개적으로 보상하고 축하한다 - Google TGIF에서의 SRE 인정 사례
- 정기적 설문으로 포스트모템 프로세스의 효과성을 측정하고 개선한다
- 제품 경계를 넘어 공통 주제와 개선 영역을 식별하기 위한 집계 도구를 활용한다

## 핵심 인용
> "The cost of failure is education." - Devin Carraway

> "You can't 'fix' people, but you can fix systems and processes to better support people making the right choices."

> "Writing a postmortem is not punishment - it is a learning opportunity for the entire company."

## 관련 키워드
포스트모템, 비난 없는 문화, 근본 원인 분석, 조치 항목, 학습 기회, 포스트모템 읽기 클럽, Wheel of Misfortune, 실시간 협업, 트리거 기준, 추세 분석
