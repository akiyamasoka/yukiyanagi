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
    voice_first = models.TextField(default="準備中です")
    voice_second = models.TextField(default="準備中です")
    voice_third = models.TextField(default="準備中です")
    place = models.TextField(max_length=200, default="準備中です")
    screenshot = models.BooleanField(verbose_name='スクリーンショットを表示するか', default=False)
    maps = models.TextField(default="学生課")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
        

class Tag(models.Model):
	name = models.CharField('選択肢名', max_length=255)
	
	def __str__(self):
		return self.name
        

class YesOrNo(models.Model):
    name = models.CharField('選択肢名', max_length=255)

    def __str__(self):
        return self.name

class TwoChoices(models.Model):
    name = models.CharField('選択肢名', max_length=255)
    
    def __str__(seld):
        return self.name
        
class ThreeChoices(models.Model):
    name = models.CharField('選択肢名', max_length=255)

    def __str__(self):
        return self.name
    
class ThreeChoices_re(models.Model):
    name = models.CharField('選択肢名', max_length=255)

    def __str__(self):
        return self.name

    
class Servey_re(models.Model):
    question_already = models.ManyToManyField(YesOrNo, verbose_name='あなたに提示された学内機関の申し込み方法をもともと知っていましたか？')
    question_understanding = models.ManyToManyField(TwoChoices, verbose_name='本WEBサイトを利用することによって、申し込み方法を理解することはできましたか？')
    question_suitable = models.ManyToManyField(ThreeChoices, verbose_name='あなたの「困った」を解決するために適切な学内機関が提示されたと思いますか？')
    question_changes = models.ManyToManyField(ThreeChoices_re, verbose_name='今までと比べて、学内機関の利用のしやすさに変化はありましたか？')
    question_reasons = models.TextField('上記の具体的な理由をお書きください', default="特になし")
    question_requests = models.TextField('WEB各機能に対する感想・ご意見・ご要望（学生体験談、申し込み方法の提示、説明の口調やサイトデザイン・レイアウト等について）')
    
    institution = models.CharField(max_length=200, default="交通事故報告")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

        def __str__(self):
            return self.institution
        
    
class Servey(models.Model):
	student_number = models.IntegerField('① 学籍番号')
    #needs = models.ManyToManyField(Tag, verbose_name='② あなたのニーズに合った学内機関が表示されたと思いますか？')
	question = models.TextField('③ ②の理由、またはサイトデザインや質問内容等に関する要望があれば教えてください。')
	institution = models.CharField(max_length=200, default="交通事故報告")
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.save()
		
	def __str__(self):
		return self.institution



