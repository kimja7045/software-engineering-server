from django.contrib.gis.db import models
import random
import string
import time
from io import BytesIO
from PIL import Image
from service.utils import image as image_utils


class Post(models.Model):
    class Meta:
        verbose_name = '창업정보'
        verbose_name_plural = verbose_name

    user = models.ForeignKey(
        to='User',
        verbose_name='창업정보 작성자',
        related_name='posts',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='제목',
        max_length=64,
    )
    content = models.TextField(
        verbose_name='내용',
    )
    favorite_users = models.ManyToManyField(
        to='User',
        related_name='favorite_users',
        verbose_name='찜(즐겨찾기)한 사람들',
        blank=True,
    )
    favorite_count = models.PositiveIntegerField(
        verbose_name='즐겨찾기 수',
        default=0
    )
    image = models.ImageField(
        upload_to='post_images',
        verbose_name='이미지',
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        verbose_name='작성일',
        auto_now=True
    )

    def __str__(self):
        return f'{self.user}/{self.title}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.image and not self.image.name.startswith('resized'):
            middle = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            self.image.name = f'resized_{middle}_{int(time.time() * 100)}.{self.image.name.split(".")[-1]}'
            size = [700, 700]
            tmp = Image.open(BytesIO(self.image.read()))
            image = image_utils.rotate(tmp)
            self.image = image_utils.make_thumbnail(size, image, self.image.name)
        super().save()


class Review(models.Model):
    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = verbose_name

    user = models.ForeignKey(
        to='User',
        verbose_name='창업정보 댓글 작성자',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to='Post',
        verbose_name='창업정보',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name='내용',
    )
    created_at = models.DateField(
        verbose_name='작성일',
        auto_now=True
    )

    def __str__(self):
        return f'{self.user}/{self.created_at}'
