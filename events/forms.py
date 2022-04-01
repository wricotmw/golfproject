from django import forms
from django.forms import ModelForm
from.models import Scores, Golfer, ScoreDate



class GolferForm(ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Golfer
		fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'



class ScoreForm(forms.ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Scores
		fields = fields = '__all__'
		widgets = {
            'score_date': DateInput(),
        }
	


