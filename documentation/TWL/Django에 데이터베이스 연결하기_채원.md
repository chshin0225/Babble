# Django에 DB 연결하기

> 이 내용은 주로 [Django 공식 문서](https://docs.djangoproject.com/en/3.1/)에서 가져왔기 때문에 공식 문서를 직접 읽어보는 것을 추천한다.



Django는 다음 데이터베이스들을 공식적으로 지원한다:

- [PostgreSQL](https://docs.djangoproject.com/en/3.1/ref/databases/#postgresql-notes)
- [MariaDB](https://docs.djangoproject.com/en/3.1/ref/databases/#mariadb-notes)
- [MySQL](https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-notes)
- [Oracle](https://docs.djangoproject.com/en/3.1/ref/databases/#oracle-notes)
- [SQLite](https://docs.djangoproject.com/en/3.1/ref/databases/#sqlite-notes)

하지만 기본적으로는 SQLite3 db 연결을 default로 하고 있기 때문에 다른 데이터베이스를 사용하려면 설정을 바꿔줘야한다.



### 1. mysql과 mysqlclient 설치

[MySQLClient](https://pypi.org/project/mysqlclient/)은 Django ORM (Object Relational Management)을 사용하기 위해 필요한 코드를 설치해주는 adapter라고 보면된다. 다음과 같이 설치할 수 있으며, 이전에 mysql이 설치되어있어야한다.

```bash
$ pip install mysqlclient 
```



### 2. database 생성

```bash
# mysql 접속
$ mysql -u root -p
```

위의 명령을 실행하고 비밀번호 입력 후 접속한다. prompt의 머리가 `mysql>` 로 바뀌면 성공적으로 접속한 것이다. 이후 우리가 사용할 데이터베이스를 생성한다.

```mysql
mysql> CREATE DATABASE {database 이름};
mysql> USE {database 이름};
```



### 3. settings.py 변경

기본적으로는 SQLite를 DB로 설정하고 있기 때문에, 다른 데이터베이스를 사용하려면 settings.py에서 `DATABASES` 설정을 바꿔줘야한다.

ex) mysql을 사용하는 경우

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

정의할 수 있는 파라미터의 종류와 설명을 [공식문서](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASE-ENGINE)에서 자세히 읽어볼 것을 권장한다.



### 4. migrate

설정을 다 바꿨으면 변경사항들을 migrate해준다.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

migrate 완료 후 mysql에 다시 접속해서 database에서 테이블 조회를 했을 때 다음과 같은 결과가 나오면 성공이다.

```mysql
mysql> show tables;
+----------------------------+
| Tables_in_practice         |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
10 rows in set (0.00 sec)
```





### 참고자료

- [튜토리얼 영상](https://www.youtube.com/watch?v=SNyCV8vOr-g) (이해를 돕기 위해)
- [Ubuntu에서 Django랑 mysql 연결하기](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) (나중에 aws에서 할 때 참고하기 좋을 듯)

