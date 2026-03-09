# SRE Knowledge Topic Index

Google SRE 3권의 주제별 상세 챕터 매핑입니다. 스킬이 사용자 질문에서 관련 챕터를 빠르게 찾기 위한 색인입니다.

## SRE Book (Site Reliability Engineering)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_introduction.md | SRE 정의, DevOps와의 관계, MTTR, MTTF, MTBF, 가용성 측정 |
| ch02 | ch02_production-environment.md | Google 프로덕션 환경 구조, 클러스터, 머신 관리, Borg |
| ch03 | ch03_embracing-risk.md | 리스크 수용, 에러 버짓 개념, 서비스 리스크 측정, 가용성 목표 |
| ch04 | ch04_service-level-objectives.md | SLI, SLO, SLA 정의 및 설정, 지표 선택, 목표 수준 |
| ch05 | ch05_eliminating-toil.md | 토일 정의, 측정, 제거 전략, 자동화 우선순위 |
| ch06 | ch06_monitoring-distributed-systems.md | 모니터링 원칙, 4 Golden Signals (latency, traffic, errors, saturation), white-box, black-box, 대시보드, 알림, 근본 원인 분석 |
| ch07 | ch07_automation-at-google.md | 자동화 전략, 가치 계층, 자동화 진화 단계 |
| ch08 | ch08_release-engineering.md | 릴리스 엔지니어링 원칙, 빌드, 배포, 릴리스 관리 |
| ch09 | ch09_simplicity.md | 시스템 단순성, 복잡성 관리, 최소 API |
| ch10 | ch10_practical-alerting.md | Borgmon, 실용적 알림 설계, 시계열 데이터, 알림 규칙 |
| ch11 | ch11_being-on-call.md | 온콜 운영, 부하 관리, 온콜 보상, 에스컬레이션 |
| ch12 | ch12_effective-troubleshooting.md | 체계적 트러블슈팅 방법론, 문제 분류, 진단, 검증 |
| ch13 | ch13_emergency-response.md | 긴급 대응 사례, 대응 절차 |
| ch14 | ch14_managing-incidents.md | 인시던트 관리 프로세스, 역할 분담, 변경 관리 |
| ch15 | ch15_postmortem-culture.md | 포스트모템 문화, 비난 없는 문화(blameless), 실수에서 배우기 |
| ch16 | ch16_tracking-outages.md | 장애 추적 시스템, Outalator |
| ch17 | ch17_testing-reliability.md | 신뢰성 테스트 전략, 카오스 엔지니어링, DiRT, MTTR/MTTF 측정 |
| ch18 | ch18_software-engineering-in-sre.md | SRE에서의 소프트웨어 엔지니어링, 도구 개발 |
| ch19 | ch19_load-balancing-frontend.md | 프론트엔드 로드 밸런싱 (DNS, VIP, Anycast) |
| ch20 | ch20_load-balancing-datacenter.md | 데이터센터 내 로드 밸런싱, 헬스 체크, 백엔드 선택 |
| ch21 | ch21_handling-overload.md | 과부하 처리, 부하 차단(load shedding), 우아한 성능 저하(graceful degradation), 재시도, 데드라인 전파 |
| ch22 | ch22_addressing-cascading-failures.md | 연쇄 장애, 서버 과부하, 리소스 고갈, 큐 관리, 부하 차단, 우아한 성능 저하, 재시도, 데드라인, 용량 계획 |
| ch23 | ch23_managing-critical-state.md | 분산 합의, Paxos, Raft, 중요 상태 관리 |
| ch24 | ch24_distributed-periodic-scheduling.md | 분산 주기 스케줄링 (Cron), 대규모 스케줄러 |
| ch25 | ch25_data-processing-pipelines.md | 데이터 처리 파이프라인, 워크플로우 관리 |
| ch26 | ch26_data-integrity.md | 데이터 무결성, 복구 전략, 백업, 복원 |
| ch27 | ch27_reliable-product-launches.md | 안정적 제품 출시 체크리스트, 용량 계획, 출시 조율 |
| ch28 | ch28_accelerating-sre-on-call.md | 온콜 가속화, 신규 SRE 온보딩, 교육 |
| ch29 | ch29_dealing-with-interrupts.md | 인터럽트 관리, 운영 부하, 티켓 처리 |
| ch30 | ch30_operational-overload.md | 운영 과부하 대응, 팀 확장 |
| ch31 | ch31_communication-and-collaboration.md | 커뮤니케이션, 협업, 프로덕션 미팅 |
| ch32 | ch32_evolving-sre-engagement-model.md | SRE 참여 모델 진화, PRR, 얼리 인게이지먼트 |
| ch33 | ch33_lessons-learned.md | 교훈 정리 |
| ch34 | ch34_conclusion.md | 결론 |
| app_a | appendix_a_availability-table.md | 가용성 테이블 (9의 개수), SLA 계산 |
| app_b | appendix_b_service-best-practices.md | 서비스 모범 사례 |
| app_c | appendix_c_incident-document.md | 인시던트 문서 템플릿 |
| app_d | appendix_d_example-postmortem.md | 포스트모템 예시, 타임라인, 근본 원인 |
| app_e | appendix_e_launch-checklist.md | 출시 체크리스트, 출시 준비도 |
| app_f | appendix_f_production-meeting.md | 프로덕션 미팅 가이드 |

## Workbook (The Site Reliability Workbook)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_how-sre-relates.md | SRE와 DevOps 관계, 문화, 원칙 |
| ch02 | ch02_implementing-slos.md | SLO 구현 실무 가이드, SLI 선택, 목표 설정, 윈도우 |
| ch03 | ch03_slo-engineering-case-studies.md | SLO 엔지니어링 사례 연구, 실제 적용 |
| ch04 | ch04_monitoring.md | 모니터링 실무, 4 Golden Signals, 대시보드 설계, 메트릭 수집 |
| ch05 | ch05_alerting-on-slos.md | SLO 기반 알림 설계, 번 레이트(burn rate), 다중 윈도우 알림, 알림 정책 |
| ch06 | ch06_eliminating-toil.md | 토일 제거 실무, 자동화 ROI |
| ch07 | ch07_simplicity.md | 단순성 실무 적용, 복잡성 측정 |
| ch08 | ch08_on-call.md | 온콜 실무 가이드, 로테이션, 에스컬레이션 |
| ch09 | ch09_incident-response.md | 인시던트 대응 실무, 역할, 커뮤니케이션 |
| ch10 | ch10_postmortem-culture.md | 포스트모템 실무, 근본 원인 분석, 액션 아이템 |
| ch11 | ch11_managing-load.md | 부하 관리 실무, 용량 계획(capacity planning), 오토스케일링 |
| ch12 | ch12_non-abstract-design.md | 비추상적 시스템 설계 (NALSD), 설계 문서, 인터뷰 |
| ch13 | ch13_data-processing.md | 데이터 처리 파이프라인 실무, 배치 처리, 스트리밍 |
| ch14 | ch14_configuration-design.md | 설정 관리 설계, 설정 원칙 |
| ch15 | ch15_configuration-specifics.md | 설정 관리 세부사항, 설정 검증 |
| ch16 | ch16_canarying-releases.md | 카나리 릴리스 전략, 블루/그린 배포, 점진적 롤아웃 |
| ch17 | ch17_overload.md | 과부하 관리 실무, 부하 테스트, 용량 계획 |
| ch18 | ch18_engagement-model.md | SRE 참여 모델, 서비스 인수 |
| ch19 | ch19_reaching-beyond.md | SRE 확장 전략, 컨설팅 모델 |
| ch20 | ch20_team-lifecycles.md | SRE 팀 생명주기, 팀 구성 |
| ch21 | ch21_organizational-change.md | 조직 변화 관리, 변경 관리(change management) |
| app_a | appendix_a_slo-document.md | SLO 문서 템플릿, SLO 문서화 |
| app_b | appendix_b_error-budget-policy.md | 에러 버짓 정책 템플릿, 정책 수립, 위반 시 대응 |
| app_c | appendix_c_postmortem-analysis.md | 포스트모템 분석 가이드 |

## BSRS (Building Secure and Reliable Systems)

| 챕터 | 파일명 | 핵심 주제 |
|------|--------|----------|
| ch01 | ch01_intersection-security-reliability.md | 보안과 신뢰성의 교차점, 공통 원칙 |
| ch02 | ch02_understanding-adversaries.md | 적대자 이해, 위협 모델링(threat model), 공격 동기, ATT&CK |
| ch03 | ch03_safe-proxies.md | 안전한 프록시 설계, 접근 제어, 감사 로깅 |
| ch04 | ch04_design-tradeoffs.md | 보안/신뢰성 설계 트레이드오프, 비용 분석 |
| ch05 | ch05_design-least-privilege.md | 최소 권한 원칙 설계, 제로 트러스트(zero trust), 접근 제어 |
| ch06 | ch06_design-understandability.md | 이해 가능한 시스템 설계, 인지 부하, 복잡성 |
| ch07 | ch07_design-changing-landscape.md | 변화하는 환경 대응 설계, 의존성 관리 |
| ch08 | ch08_design-resilience.md | 복원력 설계 패턴, 장애 격리, 서킷 브레이커 |
| ch09 | ch09_design-recovery.md | 복구 설계 전략, 장애 복구, 재해 복구 |
| ch10 | ch10_mitigating-dos.md | DoS 완화 전략, DDoS 방어, 트래픽 관리 |
| ch11 | ch11_publicly-trusted-ca.md | 공개 신뢰 인증기관 운영, TLS/SSL |
| ch12 | ch12_writing-code.md | 안전한 코드 작성, 보안 코딩, 입력 검증 |
| ch13 | ch13_testing-code.md | 보안/신뢰성 테스트, 퍼즈 테스트, 정적 분석 |
| ch14 | ch14_deploying-code.md | 안전한 배포 전략, 배포 파이프라인, 롤백 |
| ch15 | ch15_investigating-systems.md | 시스템 조사, 디버깅, 포렌식, 로그 분석 |
| ch16 | ch16_disaster-planning.md | 재해 계획 수립, 런북(runbook), 플레이북(playbook), DR 테스트 |
| ch17 | ch17_crisis-management.md | 위기 관리 프로세스, 워 룸(war room), 커뮤니케이션 |
| ch18 | ch18_recovery-aftermath.md | 복구 및 사후 처리, 사후 분석 |
| ch19 | ch19_chrome-security.md | Chrome 보안 사례 연구, 샌드박싱 |
| ch20 | ch20_roles-responsibilities.md | 보안/신뢰성 역할과 책임, 조직 구조 |
| ch21 | ch21_culture.md | 보안/신뢰성 문화 구축, 교육, 인식 제고 |
| app_a | appendix_a_disaster-risk-matrix.md | 재해 리스크 매트릭스, 위험 평가 |

## Keyword-to-Topic Mapping

빠른 키워드 검색을 위한 매핑입니다. 한국어 동의어를 포함하여 다국어 질의를 지원합니다.

| 키워드 | 한국어 동의어 | 관련 주제 | 우선 참조 |
|--------|-------------|----------|----------|
| SLO, SLI, SLA, error budget | 서비스 수준 목표, 서비스 수준 지표, 에러 버짓, 오류 예산 | SLO/SLI/SLA | SRE Book ch03-04, Workbook ch02-03 |
| monitoring, metrics, alerting, golden signals | 모니터링, 메트릭, 알림, 경보, 골든 시그널 | Monitoring/Alerting | SRE Book ch06, ch10, Workbook ch04-05 |
| four golden signals, latency, traffic, errors, saturation | 4대 골든 시그널, 지연시간, 트래픽, 오류율, 포화도 | Golden Signals | SRE Book ch06, Workbook ch04 |
| burn rate, multi-window alert, alert policy | 번 레이트, 소진율, 다중 윈도우 알림, 알림 정책 | SLO Alerting | Workbook ch05 |
| incident, outage, emergency, response | 인시던트, 장애, 긴급 대응, 사고 대응 | Incident Management | SRE Book ch13-14, Workbook ch09 |
| postmortem, blameless, RCA, root cause | 포스트모템, 사후 분석, 비난 없는 문화, 근본 원인 분석 | Postmortem | SRE Book ch15, Workbook ch10 |
| toil, automation, manual work | 토일, 자동화, 수작업, 반복 작업 | Toil/Automation | SRE Book ch05, ch07, Workbook ch06 |
| on-call, pager, rotation, escalation | 온콜, 호출, 로테이션, 에스컬레이션, 당직 | On-Call | SRE Book ch11, ch28, Workbook ch08 |
| load balancing, overload, cascading, shedding | 로드 밸런싱, 부하 분산, 과부하, 연쇄 장애, 부하 차단 | Load/Overload | SRE Book ch19-22, Workbook ch11, ch17 |
| graceful degradation, load shedding, backpressure | 우아한 성능 저하, 부하 차단, 백프레셔, 과부하 보호 | Overload Protection | SRE Book ch21-22, Workbook ch17 |
| release, deploy, canary, rollback | 릴리스, 배포, 카나리, 롤백 | Release/Deploy | SRE Book ch08, Workbook ch16, BSRS ch14 |
| canary, blue/green, progressive rollout | 카나리 배포, 블루/그린 배포, 점진적 롤아웃 | Canary/Deploy Strategy | Workbook ch16, BSRS ch14 |
| testing, reliability test, chaos | 테스트, 신뢰성 테스트, 카오스 엔지니어링 | Testing | SRE Book ch17, BSRS ch13 |
| chaos engineering, DiRT, game day | 카오스 엔지니어링, 장애 주입, 재해 복구 훈련 | Chaos Engineering | SRE Book ch17, BSRS ch16 |
| security, vulnerability, threat, adversary | 보안, 취약점, 위협, 적대자 | Security | BSRS ch01-21 |
| threat model, attack surface, ATT&CK | 위협 모델링, 공격 표면, 위협 분석 | Threat Modeling | BSRS ch02 |
| zero trust, least privilege, access control | 제로 트러스트, 최소 권한, 접근 제어 | Zero Trust/Access | BSRS ch05, ch03 |
| least privilege, access control, proxy | 최소 권한, 접근 제어, 프록시 | Access Control | BSRS ch03, ch05 |
| resilience, recovery, disaster, DR | 복원력, 복구, 재해, 재해 복구, DR | Disaster/Recovery | BSRS ch08, ch09, ch16 |
| crisis, war room, communication | 위기, 워 룸, 상황실, 커뮤니케이션 | Crisis Management | BSRS ch17, ch18, SRE Book ch14 |
| data integrity, backup, restore | 데이터 무결성, 백업, 복원, 데이터 보호 | Data | SRE Book ch26, Workbook ch13 |
| configuration, config management | 설정, 설정 관리, 구성 관리, 컨피그 | Configuration | Workbook ch14-15 |
| simplicity, complexity, cognitive load | 단순성, 복잡성, 인지 부하, 시스템 단순화 | Simplicity | SRE Book ch09, Workbook ch07, BSRS ch06 |
| team, organization, culture, engagement | 팀, 조직, 문화, SRE 참여 모델 | Organization | SRE Book ch30-32, Workbook ch18-21, BSRS ch20-21 |
| launch, checklist, readiness | 출시, 체크리스트, 출시 준비도, 런치 | Launch | SRE Book ch27, app_e |
| troubleshooting, debugging, investigation | 트러블슈팅, 디버깅, 조사, 문제 해결 | Troubleshooting | SRE Book ch12, BSRS ch15 |
| distributed system, consensus, Paxos, Raft | 분산 시스템, 합의 알고리즘, 분산 합의 | Distributed Systems | SRE Book ch23-24 |
| pipeline, data processing, batch | 파이프라인, 데이터 처리, 배치 처리, 스트리밍 | Data Processing | SRE Book ch25, Workbook ch13 |
| DoS, DDoS, denial of service | 서비스 거부 공격, 디도스 | DoS Mitigation | BSRS ch10 |
| availability, nines, uptime | 가용성, 나인, 업타임, 가동률 | Availability | SRE Book ch03, app_a |
| code review, secure coding | 코드 리뷰, 보안 코딩, 안전한 코드 | Secure Coding | BSRS ch12 |
| MTTR, MTTF, MTBF, mean time | 평균 복구 시간, 평균 장애 시간, 평균 장애 간격, 신뢰성 지표 | Reliability Metrics | SRE Book ch01, ch03, ch17 |
| capacity planning, resource planning | 용량 계획, 리소스 계획, 수요 예측, 확장 계획 | Capacity Planning | SRE Book ch22, ch27, Workbook ch11, ch17 |
| change management, rollout, migration | 변경 관리, 롤아웃, 마이그레이션, 변경 프로세스 | Change Management | SRE Book ch14, Workbook ch21, BSRS ch14 |
| error budget policy, budget exhaustion | 에러 버짓 정책, 예산 소진, 예산 정책 | Error Budget Policy | Workbook app_b, SRE Book ch03 |
| NALSD, non-abstract design, system design | 비추상적 설계, 시스템 설계, 설계 면접 | System Design (NALSD) | Workbook ch12 |
| runbook, playbook, procedure | 런북, 플레이북, 운영 절차서, 대응 매뉴얼 | Runbook/Playbook | BSRS ch16, SRE Book ch14 |
| war room, command post, incident commander | 워 룸, 상황실, 지휘소, 인시던트 커맨더 | War Room | BSRS ch17, SRE Book ch14 |
| circuit breaker, bulkhead, fault isolation | 서킷 브레이커, 격벽, 장애 격리, 회로 차단기 | Resilience Patterns | BSRS ch08, SRE Book ch22 |
| retry, timeout, deadline, exponential backoff | 재시도, 타임아웃, 데드라인, 지수 백오프 | Retry/Timeout | SRE Book ch21-22, Workbook ch17 |
| dashboard, visualization, white-box, black-box | 대시보드, 시각화, 화이트박스, 블랙박스 모니터링 | Monitoring Patterns | SRE Book ch06, ch10, Workbook ch04 |
