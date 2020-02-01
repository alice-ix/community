from django.db import models

# Create your models here.


class Board(models.Model):
    
    objects = models.Manager()
    title = models.CharField (max_length=128, verbose_name='제목')
    contents = models.TextField (verbose_name='내용')
    writer = models.ForeignKey('alice_user.AliceUser', on_delete=models.CASCADE, verbose_name='작성자')
    registerDateTime = models.DateTimeField (auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'alice_board'
        verbose_name = '앨리스 게시글'
        verbose_name_plural = '앨리스 게시글'