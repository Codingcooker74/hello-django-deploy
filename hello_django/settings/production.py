from .base import *
import os 

# ED내부에서 ALB가 EC2에 대한 헬스체크 요청대비
#- EC2 사설ip로 요청하는 경우 Disallowed Host 오류발생
#- ebhealthcheck애비 현재 EC@의 사설ip를 자동으로  ALLOWED_HOSTS에 추가하는 기능이 있음
INSTALLED_APPS.extend([
            'ebhealthcheck.apps.EBHealthCheckConfig'
])

DEBUG = False

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '.amanzonaws.com'
]

# 추가 ALLOWED_HOSTS 설정
additional_allowed_hosts = os.getenv('ALLOWED_HOSTS')
if additional_allowed_hosts:
    ALLOWED_HOSTS.extend([host.strip() for host in additional_allowed_hosts.split(',')])

print(f'[production] {ALLOWED_HOSTS = }')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}