from django.db import models


# Create your models here.

class AliceUser(models.Model):
    
    objects = models.Manager()
    userName = models.CharField (max_length=64, verbose_name='사용자명')
    userEmail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    passWord = models.CharField (max_length=64, verbose_name='비밀번호')
    signUpDateTime = models.DateTimeField (auto_now_add=True, verbose_name='가입일시')

    def __str__(self):
        return self.userName

    class Meta:
        db_table = 'alice_aliceUser'
        verbose_name = '앨리스 사용자'
        verbose_name_plural = '앨리스 사용자'