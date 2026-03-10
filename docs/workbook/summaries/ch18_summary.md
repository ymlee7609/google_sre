# SRE Engagement Model 요약

## 핵심 원칙
- SRE 원칙의 목표는 개발팀의 엔지니어링 속도를 극대화하면서 제품의 신뢰성을 유지하는 것이다
- SRE 모델은 도메인이 너무 크고 복잡하면 효과가 떨어진다 - 어디에 집중할지 결정해야 한다
- SRE 참여(engagement)는 서비스 자체를 넘어 개발팀과 제품팀의 목표를 이해하고 지원하는 것이다
- SRE의 장기 목표는 지속적인 인간 작업이 더 이상 필요하지 않도록 서비스 운영을 최적화하는 것이다
- SRE 참여는 영구적이지 않다 - 가치가 비용을 정당화하지 못하면 재검토해야 한다
- 신뢰성은 제품 개발의 핵심 기둥이며, 테스팅이나 보안과 같은 수준으로 투자되어야 한다

## 주요 프랙티스 및 권고사항
- **서비스 생명주기 7단계**: 아키텍처/설계 → 활발한 개발 → 제한적 가용성 → 일반 가용성 → 폐기 → 방치 → 미지원
  - 설계 단계의 조기 참여로 비용이 많이 드는 재설계를 방지하라
  - GA 전에 SLO를 정의하여 객관적 신뢰성 측정 기준을 확보하라
  - GA 단계에서도 개발팀이 운영 작업의 일부를 담당하게 하여 운영 관점을 유지하라
- **관계 설정**:
  - 비즈니스/제품 목표를 깊이 이해하고, SRE/개발 리더십이 정기적으로 소통하라
  - 공유 목표 수립: SRE는 개발팀의 릴리스 속도를 지원하고, 개발팀은 신뢰성 수정에 시간을 투자하라
  - SLO와 에러 버짓에 합의하고 이를 기반으로 엔지니어링 우선순위를 결정하라
  - 운영 작업에 대한 정의와 엄격한 상한선을 설정하라
- **New York Times 사례**: 공유 목표 모델 채택
  - 참여 범위 정의 → 공유 목표/마일스톤 설정 → 스프린트/커뮤니케이션 → 영향 측정
  - 참여 전후 성숙도 매트릭스를 통한 점진적 평가(point-in-time assessment)
  - SRE는 전통적 운영 엔지니어가 아님을 명확히 하라
- **지속적 관계 유지**: 분기별 "프로덕션 상태" 발표, 정기적 서비스 리뷰, 연례 대면 회의
- **SLO/에러 버짓에 따른 우선순위 조정**: SLO 위반 시 양 팀이 고우선순위로 복구, 에러 버짓 여유 시 기능 속도 증가
- **확장 전략**:
  - 단일 제품/유사 기술 스택/소수 개발팀의 서비스는 하나의 SRE 팀으로 지원 가능
  - 기술 스택 기반으로 SRE 팀을 조직하여 개발팀 재편에 대한 영향을 최소화하라
  - 글로벌 분산 팀 운영 시 단독 팀(singleton) 구성을 피하라
- **참여 종료**: Ares 사례(개발팀 내 인프라팀 육성 후 성공적 이관), 데이터 분석 파이프라인 사례(소통 단절로 인한 비자발적 종료)

## 핵심 인용
> "Simply put, SRE principles aim to maximize the engineering velocity of developer teams while keeping products reliable."

> "Investing in aligning team goals and understanding each other's objectives is as important as defending SLOs."

> "If the majority of the work is no longer on the engineering (versus operations) side, you may need to revisit the ongoing SRE engagement."

## 관련 키워드
SRE 참여 모델, 서비스 생명주기, PRR, 공유 목표, SLO, 에러 버짓, 관계 관리, 팀 확장, 서비스 반환, New York Times, Ares, 성숙도 평가, 로드맵
