from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField(unique=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 服役年資
    SERVICE_YEARS_CHOICES = [
        (1, '未滿3年者'),
        (2, '滿3年未滿6年者'),
        (3, '滿6年未滿9年者'),
        (4, '滿9年未滿12年者'),
        (5, '滿12年未滿15年者'),
        (6, '滿15年未滿18年者'),
        (7, '滿18年未滿21年者'),
        (8, '滿21年未滿24年者'),
        (9, '滿24年以上者'),
    ]
    EDUCATION_CHOICES = [
        ( 1, '無'),
        ( 2, '二年制專科學校及進修學校肄業學生'),
        ( 3, '三年制專科學校及進修學校肄業學生'),
        ( 4, '五年制專科學校及進修學校肄業學生'),
        ( 5, '大學學士班（不包括空中大學）肄業'),
        ( 6, '自學進修學力鑑定考試通過'),
        ( 7, '國家考試及格，持有及格證書'),
        ( 8, '技能檢定合格'),
        ( 9, '符合年滿22歲、高級中等學校畢（結）業或修滿規定修業年限，且已修畢畢業應修學分80學分以上'),
        ( 10, '持有高級中等學校畢業證書後，從事相關工作經驗五年以上'),
        ( 11, '曾於大學校院擔任專業技術人員、於專科學校或高級中等學校擔任專業及技術教師'),
        ( 12, '持國外或香港、澳門專科以上學校畢（肄）業學歷'),
    ]
    SEX_CHOICES = [
        (1,'男'),
        (2,'女')
    ]
    # 性別
    sex = models.IntegerField(choices=SEX_CHOICES, blank=False, null=False)
    date_of_birth = models.DateField()
    username = models.CharField(max_length=50 , blank = False, null = False , default = '' )
    identity = models.CharField(max_length=15 , blank = False, null = False , default = '' )
    address = models.CharField(max_length=150 , blank = False, null = False , default = '' )
    home_phone = models.CharField(max_length=15 , blank = False, null = False , default = '' )
    mobile_phone = models.CharField(max_length=15 , blank = False, null = False , default = '' )
    email = models.EmailField()

    #緊急聯絡人
    emergency_contact = models.CharField(max_length=50,blank = False, null = False , default = '')
    emergency_contact_phone = models.CharField(max_length=15,blank = False, null = False , default = '')
    emergency_contact_relationship = models.CharField(max_length=15,blank = False, null = False , default = '')

    # 報考學歷
    education = models.IntegerField(choices=EDUCATION_CHOICES, blank=False, null=False)
    # 
    #兵籍號碼
    military_service_number = models.CharField(max_length=15,blank = False, null = False)
    # 軍種
    military_service = models.CharField(max_length=15,blank = False, null = False)
    # 階級
    military_rank = models.CharField(max_length=15,blank = False, null = False)
    # 退伍期間
    military_retired_date = models.DateField(blank = False, null = False)
    # 服役年資
    military_service_years = models.IntegerField(choices=SERVICE_YEARS_CHOICES, blank=False, null=False)
    # 身分證正面反面
    identity_front = models.ImageField(blank = False, null = False)
    identity_back = models.ImageField(blank = False, null = False)

    activity = models.ManyToManyField('Activity', through='Score')
    def date_of_birth_tw(self):
        return self.date_of_birth.year - 1911, self.date_of_birth.month, self.date_of_birth.day
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

# 活動
class Activity(models.Model):
    status = models.BooleanField(default = False)
    name = models.TextField(blank = False, null = False, default = '')
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)


class ScoreLabel(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    label = models.TextField(blank = False, null = False, default = '')

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    label = models.ForeignKey(ScoreLabel, on_delete=models.CASCADE)
    score = models.IntegerField(blank = False, null = False)
    class Meta:
        unique_together = ('student', 'activity')