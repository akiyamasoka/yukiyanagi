from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tag = models.TextField(default=",0")
    #destination = models.TextField(default=",0")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=200, default="https://www.soka.ac.jp/inquiries/list")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Tag(models.Model):
	name = models.CharField('選択肢名', max_length=255)
	
	def __str__(self):
		return self.name
        
        
class Servey(models.Model):
	student_number = models.IntegerField('学籍番号')
	needs = models.ManyToManyField(Tag, verbose_name='あなたのニーズに合った学内機関が表示されたと思いますか？')
	question = models.TextField('2つ目の理由、またはサイトデザインや質問内容等に関する要望があれば教えてください。')
	link = models.CharField(max_length=200, default="https://www.soka.ac.jp/inquiries/list")
	institution = models.CharField(max_length=200, default="交通事故報告")
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.save()
		
	def __str__(self):
		return self.student_number



