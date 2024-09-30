from django.contrib.auth.models import AbstractUser
from django.db import models

# 커스텀 User 모델로 대체하기 위한 class 작성
class User(AbstractUser):
    pass 