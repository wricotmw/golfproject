from django.db import models

# Create your models here.


 
class ScoreDate(models.Model):
    score_date = models.DateField(null=True)



class Golfer(models.Model):
	name = models.CharField('name', max_length=120)

	def __str__(self):
		return self.name

class Scores(models.Model):
	name = models.ForeignKey(Golfer, blank= False, null = False, on_delete=models.CASCADE)
	score = models.IntegerField()
	score_date = models.DateTimeField()
	
	def __str__(self):
		return str(self.score)

class FiveScores(models.Model):
	name = models.ForeignKey(Golfer, blank= False, null = False, on_delete=models.CASCADE)
	score1 = models.IntegerField()
	score2 = models.IntegerField()
	score3 = models.IntegerField()
	score4 = models.IntegerField()
	score5 = models.IntegerField()
	total_score = models.IntegerField()

	def __str__(self):
		return str(self.name)
