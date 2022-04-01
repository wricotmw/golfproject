from django.contrib import admin

# Register your models here.
from .models import Golfer
from .models import Scores
from .models import FiveScores
admin.site.register(Golfer)
@admin.register(Scores)
class ScoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'score', 'score_date')
	ordering = ('-score_date',)
@admin.register(FiveScores)
class FiveScoresAdmin(admin.ModelAdmin):
	list_display = ('name', 'score1', 'score2', 'score3','score4', 'score5', 'total_score')
