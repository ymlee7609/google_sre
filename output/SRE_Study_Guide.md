# Google SRE 3권 교차 학습 진도표

## 1. 개요

### 3권의 역할

| 도서 | 약칭 | 역할 | 핵심 관점 |
|------|------|------|-----------|
| *Site Reliability Engineering* | **SRE Book** | 주교재 (이론) | Google SRE의 원칙, 실무, 조직 운영 |
| *The Site Reliability Workbook* | **Workbook** | 실습 보충 | SRE Book의 개념을 실무에 적용하는 방법 |
| *Building Secure and Reliable Systems* | **BSRS** | 보안/설계 보충 | 보안과 신뢰성을 통합한 시스템 설계 |

### 학습 방법

1. **SRE Book**을 주교재로 순서대로 학습
2. 각 챕터 학습 후 아래 교차 참조 테이블에서 관련 Workbook/BSRS 챕터 확인
3. Workbook으로 실무 적용 방법을 보충, BSRS로 보안/설계 관점을 보충
4. 매핑되지 않는 고유 챕터는 보충 학습 주간에 별도 학습

---

## 2. 12주 학습 진도표

### Week 1 — Part I: 서론

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch01 Introduction | Workbook Ch01, BSRS Ch01 | SRE 정의, DevOps 관계, 보안-신뢰성 교차점 |
| 2일 | Ch02 The Production Environment at Google | — | Google 프로덕션 환경 이해 |

### Week 2 — Part II: 원칙 (전반)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch03 Embracing Risk | Workbook Ch02-03, BSRS Ch04 | 리스크 수용, SLO 구현, 설계 트레이드오프 |
| 2일 | Ch04 Service Level Objectives | Workbook Ch02-03, Ch05 | SLO 정의, SLO 기반 알림 |
| 3일 | Ch05 Eliminating Toil | Workbook Ch06 | 토일 정의, 제거 전략 |
| 4일 | Ch06 Monitoring Distributed Systems | Workbook Ch04-05, BSRS Ch15 | 모니터링 원칙, SLO 알림, 시스템 조사 |

### Week 3 — Part II: 원칙 (후반)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch07 The Evolution of Automation at Google | BSRS Ch07 | 자동화 발전, 변화하는 환경을 위한 설계 |
| 2일 | Ch08 Release Engineering | Workbook Ch16, BSRS Ch14 | 릴리스 엔지니어링, 카나리 배포, 코드 배포 |
| 3일 | Ch09 Simplicity | Workbook Ch07, BSRS Ch06 | 단순성 원칙, 이해 가능한 설계 |

### Week 4 — Part III: 실무 (알림 & 온콜)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch10 Practical Alerting from Time-Series Data | Workbook Ch04-05 | 시계열 기반 알림 실무 |
| 2일 | Ch11 Being On-Call | Workbook Ch08 | 온콜 운영 원칙과 실무 |
| 3일 | Ch12 Effective Troubleshooting | BSRS Ch15 | 효과적인 문제 해결, 시스템 조사 |

### Week 5 — Part III: 실무 (인시던트 대응)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch13 Emergency Response | Workbook Ch09, BSRS Ch17 | 긴급 대응, 위기 관리 |
| 2일 | Ch14 Managing Incidents | Workbook Ch09, BSRS Ch17 | 인시던트 관리 프로세스 |
| 3일 | Ch15 Postmortem Culture | Workbook Ch10, BSRS Ch18 | 포스트모템 문화, 복구와 후속 조치 |
| 4일 | Ch16 Tracking Outages | — | 장애 추적 시스템 |

### Week 6 — Part III: 실무 (테스트 & 개발)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch17 Testing for Reliability | BSRS Ch13 | 신뢰성 테스트, 코드 테스트 |
| 2일 | Ch18 Software Engineering in SRE | BSRS Ch12 | SRE의 소프트웨어 엔지니어링, 코드 작성 |
| 3일 | Ch19 Load Balancing at the Frontend | Workbook Ch11 | 프론트엔드 로드 밸런싱 |

### Week 7 — Part III: 실무 (부하 & 장애)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch20 Load Balancing in the Datacenter | Workbook Ch11 | 데이터센터 로드 밸런싱 |
| 2일 | Ch21 Handling Overload | Workbook Ch17, BSRS Ch10 | 과부하 처리, DoS 대응 |
| 3일 | Ch22 Addressing Cascading Failures | Workbook Ch17, BSRS Ch08 | 연쇄 장애 대응, 복원력 설계 |

### Week 8 — Part III: 실무 (분산 시스템 & 데이터)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch23 Managing Critical State | — | 분산 합의, 크리티컬 상태 관리 |
| 2일 | Ch24 Distributed Periodic Scheduling | — | 분산 크론 스케줄링 |
| 3일 | Ch25 Data Processing Pipelines | Workbook Ch13 | 데이터 파이프라인 설계와 운영 |
| 4일 | Ch26 Data Integrity | BSRS Ch09 | 데이터 무결성, 복구 설계 |

### Week 9 — Part III: 실무 (출시) + Part IV: 관리 (시작)

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch27 Reliable Product Launches at Scale | Workbook Ch16, BSRS Ch14 | 대규모 제품 출시, 카나리 배포 |
| 2일 | Ch28 Accelerating SREs to On-Call and Beyond | Workbook Ch20 | SRE 온보딩, 팀 생명주기 |
| 3일 | Ch29 Dealing with Interrupts | — | 인터럽트 관리 |

### Week 10 — Part IV: 관리

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch30 Embedding an SRE to Recover from Operational Overload | Workbook Ch18 | SRE 파견, 운영 과부하 복구 |
| 2일 | Ch31 Communication and Collaboration in SRE | Workbook Ch19, BSRS Ch20 | SRE 커뮤니케이션, 역할과 책임 |
| 3일 | Ch32 The Evolving SRE Engagement Model | Workbook Ch18, Ch21 | SRE 참여 모델 진화, 조직 변화 관리 |

### Week 11 — Part V: 결론 및 부록

| 일차 | SRE Book | 보충 자료 | 학습 포인트 |
|------|----------|-----------|-------------|
| 1일 | Ch33 Lessons Learned from Other Industries | BSRS Ch21 | 타 산업의 교훈, 보안/신뢰성 문화 구축 |
| 2일 | Ch34 Conclusion | Workbook Conclusion, BSRS Conclusion | 3권 종합 정리 |
| 3일 | SRE Book 부록 A-F | Workbook 부록 A-C, BSRS 부록 A | 참조 자료 통합 학습 |

### Week 12 — 보충 학습 (고유 챕터)

| 일차 | 도서 | 챕터 | 학습 포인트 |
|------|------|------|-------------|
| 1일 | BSRS | Ch02 Understanding Adversaries | 위협 행위자 이해 |
| 1일 | BSRS | Ch03 Case Study: Safe Proxies | 안전한 프록시 설계 |
| 2일 | BSRS | Ch05 Design for Least Privilege | 최소 권한 원칙 |
| 2일 | BSRS | Ch11 Case Study: Publicly Trusted CA | 공개 CA 설계/운영 |
| 3일 | BSRS | Ch16 Disaster Planning | 재해 계획 수립 |
| 3일 | BSRS | Ch19 Case Study: Chrome Security Team | Chrome 보안팀 사례 |
| 4일 | Workbook | Ch12 Introducing Non-Abstract Large System Design | 비추상적 대규모 시스템 설계 |
| 4일 | Workbook | Ch14-15 Configuration Design and Best Practices / Configuration Specifics | 설정 관리 설계 |

---

## 3. 교차 참조 테이블

### Part I — 서론

| 진행 | SRE Book | Workbook | BSRS |
|:----:|----------|----------|------|
| [ ] | Ch01 Introduction | Ch01 How SRE Relates to DevOps | Ch01 The Intersection of Security and Reliability |
| [ ] | Ch02 The Production Environment at Google | — | — |

### Part II — 원칙

| 진행 | SRE Book | Workbook | BSRS |
|:----:|----------|----------|------|
| [ ] | Ch03 Embracing Risk | Ch02 Implementing SLOs, Ch03 SLO Engineering Case Studies | Ch04 Design Tradeoffs |
| [ ] | Ch04 Service Level Objectives | Ch02-03 Implementing SLOs / Case Studies, Ch05 Alerting on SLOs | — |
| [ ] | Ch05 Eliminating Toil | Ch06 Eliminating Toil | — |
| [ ] | Ch06 Monitoring Distributed Systems | Ch04 Monitoring, Ch05 Alerting on SLOs | Ch15 Investigating Systems |
| [ ] | Ch07 The Evolution of Automation at Google | — | Ch07 Design for a Changing Landscape |
| [ ] | Ch08 Release Engineering | Ch16 Canarying Releases | Ch14 Deploying Code |
| [ ] | Ch09 Simplicity | Ch07 Simplicity | Ch06 Design for Understandability |

### Part III — 실무

| 진행 | SRE Book | Workbook | BSRS |
|:----:|----------|----------|------|
| [ ] | Ch10 Practical Alerting from Time-Series Data | Ch04 Monitoring, Ch05 Alerting on SLOs | — |
| [ ] | Ch11 Being On-Call | Ch08 On-Call | — |
| [ ] | Ch12 Effective Troubleshooting | — | Ch15 Investigating Systems |
| [ ] | Ch13 Emergency Response | Ch09 Incident Response | Ch17 Crisis Management |
| [ ] | Ch14 Managing Incidents | Ch09 Incident Response | Ch17 Crisis Management |
| [ ] | Ch15 Postmortem Culture: Learning from Failure | Ch10 Postmortem Culture | Ch18 Recovery and Aftermath |
| [ ] | Ch16 Tracking Outages | — | — |
| [ ] | Ch17 Testing for Reliability | — | Ch13 Testing Code |
| [ ] | Ch18 Software Engineering in SRE | — | Ch12 Writing Code |
| [ ] | Ch19 Load Balancing at the Frontend | Ch11 Managing Load | — |
| [ ] | Ch20 Load Balancing in the Datacenter | Ch11 Managing Load | — |
| [ ] | Ch21 Handling Overload | Ch17 Identifying and Recovering from Overload | Ch10 Mitigating Denial-of-Service Attacks |
| [ ] | Ch22 Addressing Cascading Failures | Ch17 Identifying and Recovering from Overload | Ch08 Design for Resilience |
| [ ] | Ch23 Managing Critical State | — | — |
| [ ] | Ch24 Distributed Periodic Scheduling with Cron | — | — |
| [ ] | Ch25 Data Processing Pipelines | Ch13 Data Processing Pipelines | — |
| [ ] | Ch26 Data Integrity: What You Read Is What You Wrote | — | Ch09 Design for Recovery |
| [ ] | Ch27 Reliable Product Launches at Scale | Ch16 Canarying Releases | Ch14 Deploying Code |

### Part IV — 관리

| 진행 | SRE Book | Workbook | BSRS |
|:----:|----------|----------|------|
| [ ] | Ch28 Accelerating SREs to On-Call and Beyond | Ch20 SRE Team Lifecycles | — |
| [ ] | Ch29 Dealing with Interrupts | — | — |
| [ ] | Ch30 Embedding an SRE to Recover from Operational Overload | Ch18 SRE Engagement Model | — |
| [ ] | Ch31 Communication and Collaboration in SRE | Ch19 SRE: Reaching Beyond Your Walls | Ch20 Understanding Roles and Responsibilities |
| [ ] | Ch32 The Evolving SRE Engagement Model | Ch18 SRE Engagement Model, Ch21 Organizational Change Management | — |

### Part V — 결론 및 부록

| 진행 | SRE Book | Workbook | BSRS |
|:----:|----------|----------|------|
| [ ] | Ch33 Lessons Learned from Other Industries | — | Ch21 Building a Culture of Security and Reliability |
| [ ] | Ch34 Conclusion | Conclusion | Conclusion |
| [ ] | Appendix A: Availability Table | Appendix A: SLO Document Example | Appendix A: Disaster Risk Assessment Matrix |
| [ ] | Appendix B: Service Best Practices | Appendix B: Error Budget Policy Example | — |
| [ ] | Appendix C: Incident Document | Appendix C: Postmortem Analysis Example | — |
| [ ] | Appendix D: Example Postmortem | — | — |
| [ ] | Appendix E: Launch Checklist | — | — |
| [ ] | Appendix F: Production Meeting | — | — |

---

## 4. 보충 학습 — 매핑되지 않는 고유 챕터

3권의 교차 참조에 포함되지 않는 고유 챕터입니다. Week 12에 집중 학습하거나, 관심 분야에 따라 본 과정 중 병행할 수 있습니다.

### Workbook 고유 챕터

| 진행 | 챕터 | 주제 | 관련 분야 |
|:----:|------|------|-----------|
| [ ] | Ch12 Introducing Non-Abstract Large System Design | 비추상적 대규모 시스템 설계 (NALSD) | 시스템 설계 |
| [ ] | Ch14 Configuration Design and Best Practices | 설정 관리 설계 원칙 | 설정 관리 |
| [ ] | Ch15 Configuration Specifics | 설정 관리 구체적 패턴 | 설정 관리 |

### BSRS 고유 챕터

| 진행 | 챕터 | 주제 | 관련 분야 |
|:----:|------|------|-----------|
| [ ] | Ch02 Understanding Adversaries | 위협 행위자 유형과 동기 분석 | 보안 기초 |
| [ ] | Ch03 Case Study: Safe Proxies | 안전한 프록시를 통한 접근 제어 | 보안 설계 |
| [ ] | Ch05 Design for Least Privilege | 최소 권한 원칙 적용 | 보안 설계 |
| [ ] | Ch11 Case Study: Publicly Trusted CA | 공개 인증 기관 설계/구현/운영 | 인증/암호화 |
| [ ] | Ch16 Disaster Planning | 재해 대비 계획 수립 | 재해 복구 |
| [ ] | Ch19 Case Study: Chrome Security Team | Chrome 보안팀 운영 사례 | 보안 조직 |

---

## 5. 학습 팁

### 효과적인 교차 학습 방법

1. **SRE Book 챕터를 먼저 읽고**, 핵심 개념과 원칙을 파악합니다
2. **Workbook 관련 챕터**로 "어떻게 적용하는가"를 학습합니다
3. **BSRS 관련 챕터**로 "보안/신뢰성 관점에서 어떻게 설계하는가"를 보충합니다
4. 체크박스를 활용하여 학습 진행 상황을 추적합니다

### 주제별 집중 학습 경로

관심 분야에 따라 아래 경로를 따를 수 있습니다:

**SLO/모니터링 집중**: SRE Ch03-06 → Workbook Ch02-05 → BSRS Ch04, Ch15

**인시던트 대응 집중**: SRE Ch13-15 → Workbook Ch09-10 → BSRS Ch17-18

**보안 중심 학습**: BSRS Ch01-05 → SRE Ch17-18 → BSRS Ch12-14

**대규모 시스템 설계**: SRE Ch19-24 → Workbook Ch11-13 → BSRS Ch08-09

**조직/문화**: SRE Ch28-32 → Workbook Ch18-21 → BSRS Ch20-21

---

## 6. 참고 자료

### 원서 정보

| 도서 | 챕터 수 | 부록 수 |
|------|---------|---------|
| SRE Book | 34 | 6 (A-F) |
| Workbook | 21 + Conclusion | 3 (A-C) |
| BSRS | 21 + Conclusion | 1 (A) |

### 학습 교재

- PPTX 학습 교재: `output/sre_study_*.pptx` (5권, 195장)
- SRE Book 원문: `docs/sre-book/`
- Workbook 원문: `docs/workbook/`
- BSRS 원문: `docs/bsrs/`
