# Managing Load 요약

## 핵심 원칙
- 트래픽 관리에 단일 솔루션은 없다 - 로드 밸런싱, 로드 쉐딩, 오토스케일링의 조합이 필요하다
- 로드 밸런싱, 로드 쉐딩, 오토스케일링은 독립적이지 않으며 상호작용한다
- 이들 시스템을 격리하여 설정하면 피드백 루프로 인한 재앙적 결과를 초래할 수 있다
- 클라이언트 재시도 전략이 시스템 안정성에 큰 영향을 미친다 (thundering herd 문제)
- 실제 클라이언트 수요를 가능한 한 클라이언트에 가까운 곳에서 측정하라

## 주요 프랙티스 및 권고사항
- **Google Cloud Load Balancing (GCLB)**: Anycast + Maglev(패킷 레벨 로드 밸런서) + GFE(HTTP 리버스 프록시) + GSLB(글로벌 소프트웨어 로드 밸런서) 조합
- Stabilized Anycast로 BGP 라우트 변동에도 TCP 세션 안정성 유지
- **오토스케일링 모범 사례**:
  - 비정상 인스턴스를 사용률 평균에서 제외
  - 쿨다운 기간 설정으로 새 인스턴스 안정화 대기
  - 최소/최대 경계값 설정으로 통제 불능 스케일링 방지
  - Kill Switch와 수동 오버라이드 준비
  - 백엔드 의존성 분석 후 오토스케일러 한계 설정
- **Pokemon GO 사례**: 예상의 50배 트래픽으로 캐스케이딩 장애 발생
  - 클라이언트 동기화된 재시도가 thundering herd 유발
  - 해결: GFE 격리, 트래픽 제한, 이후 지터(jitter)와 지수적 백오프 도입
- **Dressy 사례**: 로드 쉐딩과 로드 밸런싱의 상호작용 문제
  - 로드 쉐딩이 에러를 반환하면서 CPU가 낮아져 로드 밸런서가 더 많은 트래픽을 보냄
  - 해결: 에러 응답을 높은 CPU 비용으로 처리하도록 로드 밸런서 로직 수정
- RPC 요청에 데드라인 설정, 서버는 오래 걸리는 요청 종료, 클라이언트는 불필요한 요청 취소

## 핵심 인용
> "There are no perfect traffic management configurations. Autoscaling is a powerful tool, but it's easy to get wrong."

> "No amount of load shedding, autoscaling, or throttling will save our services when they all fail in sync."

## 관련 키워드
로드 밸런싱, 오토스케일링, 로드 쉐딩, GCLB, Maglev, Anycast, GFE, GSLB, 캐스케이딩 장애, thundering herd, 지수적 백오프, 데드라인
