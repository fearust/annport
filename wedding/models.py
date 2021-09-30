from django.db import models
from taggit.managers import TaggableManager
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit
import os
from uuid import uuid4


class Backdrops(models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

    image = ProcessedImageField(verbose_name='배경사진',
                                upload_to=path_and_rename('wedding/profile_backdrop/'),
                                processors=[ResizeToFit(1200, 1200)],
                                format='JPEG',
                                options={'quality': 80})
    backdrop_name = models.CharField('배경이미지제목', max_length=50, blank=True)

    def __str__(self):
        return self.backdrop_name


class Mc(models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

    name = models.CharField('이름', max_length=10)
    title = models.CharField('호칭', max_length=20)
    tags = TaggableManager()
    description = models.TextField('설명')
    profile_photo = models.ImageField('프로필사진', upload_to=path_and_rename('wedding/profile_photo/'))
    profile_backdrop = models.ForeignKey(Backdrops, on_delete=models.SET_NULL, null=True)
    profile = models.TextField('프로필', blank=True)
    mcdisplay = models.BooleanField('홈페이지노출여부', default=True)
    mcmain = models.BooleanField('메인사회자', default=False)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}-{}.{}'.format(instance.pk, uuid4().hex, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

    wedding_mc = models.ForeignKey(Mc, on_delete=models.CASCADE)
    image = ProcessedImageField(verbose_name='사회자사진',
                                upload_to=path_and_rename('wedding/gallery/'),
                                processors=[ResizeToFit(1700, 1700)],
                                format='JPEG',
                                options={'quality': 80})


class Youtube(models.Model):
    wedding_mc = models.ForeignKey(Mc, on_delete=models.CASCADE)
    url = models.CharField('유튜브일련번호', max_length=20)


class Cast(models.Model):
    bride = models.CharField('신부님 성함', max_length=20, blank=True)
    groom = models.CharField('신랑님 성함', max_length=20, blank=True)
    bride_phone = models.CharField('신부님 연락처', max_length=20, blank=True)
    groom_phone = models.CharField('신랑님 연락처', max_length=20, blank=True)
    wedding_date = models.DateTimeField('본식 날짜,시간', null=True, blank=True)
    wedding_place = models.CharField('본식 장소', max_length=50, blank=True)
    officiator = models.BooleanField('주례', default=False)
    wedding_reception = models.BooleanField('2부 진행', default=False)
    email_addr = models.EmailField('메일주소', blank=True)
    wish_mc = models.CharField('희망 사회자', max_length=100, blank=True)
    customer_memo = models.TextField('고객 메모', blank=True)
    staff_memo = models.TextField('스탭 메모', blank=True)
    create_date = models.DateTimeField('문의시간')