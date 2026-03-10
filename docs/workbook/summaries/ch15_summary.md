# Configuration Specifics 요약

## 핵심 원칙
- 설정 관련 Toil에는 두 가지 유형이 있다: 복제 Toil(중복 설정 관리)과 복잡성 Toil(자동화의 부작용)
- 설정 언어의 핵심 속성: 좋은 도구 지원, 밀폐적(hermetic) 평가, 설정과 데이터의 분리
- 범용 스크립팅 언어(Python, Ruby, Lua)를 설정 언어로 사용하는 것은 함정이다
- 데이터 형식에 프로그래밍 언어 기능이 뒷문으로 들어오는 것을 경계하라
- 설정은 "코드로서의 설정(Configuration as Code)" 원칙을 따라야 한다

## 주요 프랙티스 및 권고사항
- **설정 언어의 5가지 함정**:
  1. 설정을 프로그래밍 언어 문제로 인식하지 못함
  2. 우발적/임기응변적 언어 기능 설계
  3. 과도한 도메인 특화 최적화
  4. 설정 평가와 부작용(side effects)의 혼합 (밀폐성 위반)
  5. 범용 스크립팅 언어 사용 (무거움, 샌드박싱 필요)
- **Jsonnet 활용**: 밀폐적 오픈소스 DSL로 Kubernetes 등 다양한 애플리케이션 설정 통합
- **Kubernetes 설정 사례**: YAML 중복을 Jsonnet 템플릿으로 추상화하여 Toil 감소
- **커스텀 애플리케이션 설계 원칙**:
  - 단일 순수 데이터 파일 소비
  - 명명된 엔티티 컬렉션에 배열 대신 객체 사용
  - 논리적 관련 설정을 같은 하위 트리에 그룹화
- **운영 모범 사례**: 버전 관리, 소스 컨트롤, 린팅/포매팅 도구, 단위 테스트
- **설정 평가 시점**: 체크인 전(Very Early), 빌드 시(Middle), 런타임(Late) - 각각의 장단점 고려
- **악용 방지**: 신뢰할 수 없는 설정 코드는 샌드박싱(ulimit, 별도 프로세스) 필요

## 핵심 인용
> "If you're not intentionally designing a language, then it's highly unlikely the 'language' you'll end up with is a good one."

> "At a minimum, the critical properties of a configuration language are good tooling, hermetic configurations, and separation of configuration and data."

## 관련 키워드
Jsonnet, 설정 언어, DSL, Kubernetes, YAML, 밀폐성, 복제 Toil, 복잡성 Toil, 템플릿, 설정 검증, 샌드박싱, 튜링 완전성
