# SRE Knowledge Topic Index

Google SRE 3권의 주제별 상세 챕터 매핑입니다. 스킬이 사용자 질문에서 관련 챕터를 빠르게 찾기 위한 색인입니다.

## SRE Book (Site Reliability Engineering)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_introduction.md | SRE 정의, DevOps와의 관계 |
| ch02 | ch02_production-environment.md | Google 프로덕션 환경 구조 |
| ch03 | ch03_embracing-risk.md | 리스크 수용, 에러 버짓 개념 |
| ch04 | ch04_service-level-objectives.md | SLI, SLO, SLA 정의 및 설정 |
| ch05 | ch05_eliminating-toil.md | 토일 정의, 측정, 제거 전략 |
| ch06 | ch06_monitoring-distributed-systems.md | 모니터링 원칙, 4 Golden Signals |
| ch07 | ch07_automation-at-google.md | 자동화 전략, 가치 계층 |
| ch08 | ch08_release-engineering.md | 릴리스 엔지니어링 원칙 |
| ch09 | ch09_simplicity.md | 시스템 단순성, 복잡성 관리 |
| ch10 | ch10_practical-alerting.md | Borgmon, 실용적 알림 설계 |
| ch11 | ch11_being-on-call.md | 온콜 운영, 부하 관리 |
| ch12 | ch12_effective-troubleshooting.md | 체계적 트러블슈팅 방법론 |
| ch13 | ch13_emergency-response.md | 긴급 대응 사례 |
| ch14 | ch14_managing-incidents.md | 인시던트 관리 프로세스 |
| ch15 | ch15_postmortem-culture.md | 포스트모템 문화, 비난 없는 문화 |
| ch16 | ch16_tracking-outages.md | 장애 추적 시스템 |
| ch17 | ch17_testing-reliability.md | 신뢰성 테스트 전략 |
| ch18 | ch18_software-engineering-in-sre.md | SRE에서의 소프트웨어 엔지니어링 |
| ch19 | ch19_load-balancing-frontend.md | 프론트엔드 로드 밸런싱 (DNS, VIP) |
| ch20 | ch20_load-balancing-datacenter.md | 데이터센터 내 로드 밸런싱 |
| ch21 | ch21_handling-overload.md | 과부하 처리, 부하 차단 |
| ch22 | ch22_addressing-cascading-failures.md | 연쇄 장애 대응 패턴 |
| ch23 | ch23_managing-critical-state.md | 분산 합의, Paxos, 중요 상태 관리 |
| ch24 | ch24_distributed-periodic-scheduling.md | 분산 주기 스케줄링 (Cron) |
| ch25 | ch25_data-processing-pipelines.md | 데이터 처리 파이프라인 |
| ch26 | ch26_data-integrity.md | 데이터 무결성, 복구 전략 |
| ch27 | ch27_reliable-product-launches.md | 안정적 제품 출시 체크리스트 |
| ch28 | ch28_accelerating-sre-on-call.md | 온콜 가속화, 신규 SRE 온보딩 |
| ch29 | ch29_dealing-with-interrupts.md | 인터럽트 관리, 운영 부하 |
| ch30 | ch30_operational-overload.md | 운영 과부하 대응 |
| ch31 | ch31_communication-and-collaboration.md | 커뮤니케이션, 협업 |
| ch32 | ch32_evolving-sre-engagement-model.md | SRE 참여 모델 진화 |
| ch33 | ch33_lessons-learned.md | 교훈 정리 |
| ch34 | ch34_conclusion.md | 결론 |
| app_a | appendix_a_availability-table.md | 가용성 테이블 (9의 개수) |
| app_b | appendix_b_service-best-practices.md | 서비스 모범 사례 |
| app_c | appendix_c_incident-document.md | 인시던트 문서 템플릿 |
| app_d | appendix_d_example-postmortem.md | 포스트모템 예시 |
| app_e | appendix_e_launch-checklist.md | 출시 체크리스트 |
| app_f | appendix_f_production-meeting.md | 프로덕션 미팅 가이드 |

## Workbook (The Site Reliability Workbook)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_how-sre-relates.md | SRE와 DevOps 관계 |
| ch02 | ch02_implementing-slos.md | SLO 구현 실무 가이드 |
| ch03 | ch03_slo-engineering-case-studies.md | SLO 엔지니어링 사례 연구 |
| ch04 | ch04_monitoring.md | 모니터링 실무 |
| ch05 | ch05_alerting-on-slos.md | SLO 기반 알림 설계 |
| ch06 | ch06_eliminating-toil.md | 토일 제거 실무 |
| ch07 | ch07_simplicity.md | 단순성 실무 적용 |
| ch08 | ch08_on-call.md | 온콜 실무 가이드 |
| ch09 | ch09_incident-response.md | 인시던트 대응 실무 |
| ch10 | ch10_postmortem-culture.md | 포스트모템 실무 |
| ch11 | ch11_managing-load.md | 부하 관리 실무 |
| ch12 | ch12_non-abstract-design.md | 비추상적 시스템 설계 (NALSD) |
| ch13 | ch13_data-processing.md | 데이터 처리 파이프라인 실무 |
| ch14 | ch14_configuration-design.md | 설정 관리 설계 |
| ch15 | ch15_configuration-specifics.md | 설정 관리 세부사항 |
| ch16 | ch16_canarying-releases.md | 카나리 릴리스 전략 |
| ch17 | ch17_overload.md | 과부하 관리 실무 |
| ch18 | ch18_engagement-model.md | SRE 참여 모델 |
| ch19 | ch19_reaching-beyond.md | SRE 확장 전략 |
| ch20 | ch20_team-lifecycles.md | SRE 팀 생명주기 |
| ch21 | ch21_organizational-change.md | 조직 변화 관리 |
| app_a | appendix_a_slo-document.md | SLO 문서 템플릿 |
| app_b | appendix_b_error-budget-policy.md | 에러 버짓 정책 템플릿 |
| app_c | appendix_c_postmortem-analysis.md | 포스트모템 분석 가이드 |

## BSRS (Building Secure and Reliable Systems)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_intersection-security-reliability.md | 보안과 신뢰성의 교차점 |
| ch02 | ch02_understanding-adversaries.md | 적대자 이해, 위협 모델링 |
| ch03 | ch03_safe-proxies.md | 안전한 프록시 설계 |
| ch04 | ch04_design-tradeoffs.md | 보안/신뢰성 설계 트레이드오프 |
| ch05 | ch05_design-least-privilege.md | 최소 권한 원칙 설계 |
| ch06 | ch06_design-understandability.md | 이해 가능한 시스템 설계 |
| ch07 | ch07_design-changing-landscape.md | 변화하는 환경 대응 설계 |
| ch08 | ch08_design-resilience.md | 복원력 설계 패턴 |
| ch09 | ch09_design-recovery.md | 복구 설계 전략 |
| ch10 | ch10_mitigating-dos.md | DoS 완화 전략 |
| ch11 | ch11_publicly-trusted-ca.md | 공개 신뢰 인증기관 운영 |
| ch12 | ch12_writing-code.md | 안전한 코드 작성 |
| ch13 | ch13_testing-code.md | 보안/신뢰성 테스트 |
| ch14 | ch14_deploying-code.md | 안전한 배포 전략 |
| ch15 | ch15_investigating-systems.md | 시스템 조사, 디버깅, 포렌식 |
| ch16 | ch16_disaster-planning.md | 재해 계획 수립 |
| ch17 | ch17_crisis-management.md | 위기 관리 프로세스 |
| ch18 | ch18_recovery-aftermath.md | 복구 및 사후 처리 |
| ch19 | ch19_chrome-security.md | Chrome 보안 사례 연구 |
| ch20 | ch20_roles-responsibilities.md | 보안/신뢰성 역할과 책임 |
| ch21 | ch21_culture.md | 보안/신뢰성 문화 구축 |
| app_a | appendix_a_disaster-risk-matrix.md | 재해 리스크 매트릭스 |

## Keyword-to-Topic Mapping

빠른 키워드 검색을 위한 매핑입니다:

| 키워드 | 관련 주제 | 우선 참조 |
|--------|----------|----------|
| SLO, SLI, SLA, error budget | SLO/SLI/SLA | SRE Book ch03-04, Workbook ch02-03 |
| monitoring, metrics, alerting, golden signals | Monitoring/Alerting | SRE Book ch06, ch10, Workbook ch04-05 |
| incident, outage, emergency, response | Incident Management | SRE Book ch13-14, Workbook ch09 |
| postmortem, blameless, RCA, root cause | Postmortem | SRE Book ch15, Workbook ch10 |
| toil, automation, manual work | Toil/Automation | SRE Book ch05, ch07, Workbook ch06 |
| on-call, pager, rotation, escalation | On-Call | SRE Book ch11, ch28, Workbook ch08 |
| load balancing, overload, cascading, shedding | Load/Overload | SRE Book ch19-22, Workbook ch11, ch17 |
| release, deploy, canary, rollback | Release/Deploy | SRE Book ch08, Workbook ch16, BSRS ch14 |
| testing, reliability test, chaos | Testing | SRE Book ch17, BSRS ch13 |
| security, vulnerability, threat, adversary | Security | BSRS ch01-21 |
| least privilege, access control, proxy | Access Control | BSRS ch03, ch05 |
| resilience, recovery, disaster, DR | Disaster/Recovery | BSRS ch08, ch09, ch16 |
| crisis, war room, communication | Crisis Management | BSRS ch17, ch18, SRE Book ch14 |
| data integrity, backup, restore | Data | SRE Book ch26, Workbook ch13 |
| configuration, config management | Configuration | Workbook ch14-15 |
| simplicity, complexity, cognitive load | Simplicity | SRE Book ch09, Workbook ch07, BSRS ch06 |
| team, organization, culture, engagement | Organization | SRE Book ch30-32, Workbook ch18-21, BSRS ch20-21 |
| launch, checklist, readiness | Launch | SRE Book ch27, app_e |
| troubleshooting, debugging, investigation | Troubleshooting | SRE Book ch12, BSRS ch15 |
| distributed system, consensus, Paxos | Distributed Systems | SRE Book ch23-24 |
| pipeline, data processing, batch | Data Processing | SRE Book ch25, Workbook ch13 |
| DoS, DDoS, denial of service | DoS Mitigation | BSRS ch10 |
| availability, nines, uptime | Availability | SRE Book ch03, app_a |
| code review, secure coding | Secure Coding | BSRS ch12 |
