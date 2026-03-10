# Non-Abstract Large System Design (NALSD) 요약

## 핵심 원칙
- NALSD는 추상적 요구사항을 구체적 리소스 추정치로 변환하는 반복적 시스템 설계 방법론이다
- 신뢰성은 프로덕션 시스템의 가장 중요한 기능이다 - 설계 시 신뢰성 문제를 미루면 더 높은 비용과 적은 기능이 된다
- "Non-Abstract"의 의미: 화이트보드 설계를 실제 컴퓨터, 데이터센터, 네트워크의 구체적 리소스 추정으로 연결해야 한다
- 완벽한 가정보다 합리적 추론과 근사가 더 중요하다
- 설계의 가치는 여러 불완전하지만 합리적인 결과를 결합하여 더 나은 이해를 얻는 것에 있다

## 주요 프랙티스 및 권고사항
- **NALSD 4가지 핵심 질문**:
  1. 가능한가? (Is it possible?) - 제약 없이 설계할 수 있는가?
  2. 더 나아질 수 있는가? (Can we do better?) - 더 빠르고 효율적으로?
  3. 실현 가능한가? (Is it feasible?) - 예산, 하드웨어 등 실제 제약 하에서?
  4. 회복력이 있는가? (Is it resilient?) - 컴포넌트 장애, 데이터센터 장애 시?
- **반복적 설계 프로세스**: 단일 머신 -> 분산 시스템 -> 샤딩 -> 멀티 데이터센터
- AdWords CTR 대시보드 예제를 통한 실전 적용:
  - 단일 머신: 100TB/일 스토리지, IOPS 제약으로 불가
  - MapReduce: 배치 처리로 5분 이내 신선도 SLO 불충족
  - LogJoiner: 스트리밍 조인으로 실시간 처리
  - 샤딩: query_id 기반 샤딩으로 수평 확장
  - 멀티 데이터센터: Paxos 합의 알고리즘으로 데이터 복제
- 과학적 표기법을 활용한 리소스 계산으로 단위 오류 방지
- 각 반복에서 새로운 요구사항과 제약이 드러남을 받아들이라
- 컴포넌트를 성장 패턴에 따라 분리하여 독립적 스케일링 가능하게 설계하라

## 핵심 인용
> "We consider reliability to be the most critical feature of any production system. We find that deferring reliability issues during design is akin to accepting fewer features at higher costs."

> "The value of this exercise is in combining many imperfect-but-reasonable results into a better understanding of the design."

> "NALSD is a learned skill. As with any skill, you need to practice it regularly to maintain your proficiency."

## 관련 키워드
NALSD, 시스템 설계, 반복적 설계, 용량 계획, 샤딩, MapReduce, Paxos, 멀티 데이터센터, SLO, 리소스 추정, 장애 도메인, 수평 확장
