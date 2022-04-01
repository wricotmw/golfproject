from .models import Scores, Golfer, FiveScores

def get_scores(gname):
		return_list = []
		individual = []
		score_list = Scores.objects.filter(name=gname).order_by('-score')
		
		score_list =score_list[0:5]


		
		#for score in score_list:
		#	individual.append(score)
		for x in score_list:
			individual.append(x.score)
			
		

		if len(individual) < 5 :


			s = 5 -len(individual)

			
			while s > 0:
				individual.append(0)
				s = s - 1




		total_score = individual[0] + individual[1] + individual[2] + individual[3] + individual[4]
		individual.append(total_score)

		FiveScores.objects.create(
			name=gname,
			score1=individual[0],
			score2=individual[1],
			score3=individual[2],
			score4=individual[3],
			score5=individual[4],
			total_score=individual[5])
			

		return_list = FiveScores.objects.all().order_by('-total_score')


		return(return_list)

