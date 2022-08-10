# 단축 url 서비스

## 프로젝트 관리
- poetry를 사용하여 python 패키지 관리

- alembic을 사용하여 프로젝트 sql 작업 관리
    ``` bash
    alembic history
    alembic upgrade head
    alembic downgrade -1
    ```

## 프로젝트 구성
- 레이어드 아키텍처를 적용합니다
    - app/service 
        - url 단축에 대한 비즈니스 코드를 관리합니다
    - app/models
        - url 엔티티 관리
    - app/repository
        - 단축 url 영속화 관리
    - app/base62
        - 단축 url의 고유 id생성에 사용되는 코드
    - app/orm
        - orm 연결 관련 코드 관리
    - app/context
        - 프로젝트에서 재사용 가능하도록 서비스 인스턴스를 관리

## 프로젝트 실행
- 실행 환경에 따라 설정값을 다르게 설정할 수 있습니다.
    ``` bash
    python run.py --env prod
    ```


## API 문서 생성
- redoc-cli 설치
```
npm i -g redoc-cli
```

- 문서 추출 후 렌더링
```
FLASK_APP=app.wsgi:create_wsgi_app flask openapi write --format=json docs/apispec.json

redoc-cli build docs/apispec.json -o docs/index.html
```