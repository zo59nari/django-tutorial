from django.db import models

""" Questionモデルの作成 """
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	""" shellアクセス時の返り値設定 """
	# def __str__(self):
 #        return self.question_text

 #    def was_published_recently(self):
 #        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

""" Choiceモデルの作成 """
class Choice(models.Model):	
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	""" shellアクセス時の返り値設定 """
	# def __str__(self):
 #        return self.choice_text
