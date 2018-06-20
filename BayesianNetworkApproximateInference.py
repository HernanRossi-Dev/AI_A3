from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.sampling import BayesianModelSampling


class BayesianNetworkApproximateInference:
    def __init__(self):
        self.musicModel = BayesianModel([('Difficulty', 'Rating'), ('Musicianship', 'Rating'),
                                         ('Rating', 'Letter'), ('Musicianship', 'Exam')])

    def start(self):

        cpd_difficulty = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.6], [0.4]])
        cpd_musicianship = TabularCPD(variable='Musicianship', variable_card=2, values=[[0.7], [0.3]])

        cpd_Rating = TabularCPD(variable='Rating', variable_card=3,
                                    values=[[0.3, 0.05, 0.9, 0.5],
                                            [0.4, 0.25, 0.08, 0.3],
                                            [0.3, 0.7, 0.02, 0.2]],
                                            evidence=['Difficulty', 'Musicianship'],
                                            evidence_card=[2, 2])

        cpd_Exam = TabularCPD(variable='Exam', variable_card=2,
                                values=[[0.95, 0.2],
                                        [0.05, 0.8]],
                                evidence=['Musicianship'],
                                evidence_card=[2])

        cpd_Letter = TabularCPD(variable='Letter', variable_card=2,
                                values=[[0.1, 0.4, 0.99],
                                        [0.9, 0.6, 0.01]],
                                evidence=['Rating'],
                                evidence_card=[3])
        self.musicModel.add_cpds(cpd_difficulty, cpd_musicianship, cpd_Rating, cpd_Exam, cpd_Letter)
        print(self.musicModel.check_model())
        inference = BayesianModelSampling(self.musicModel)

        #Part one P(m = strong)P(d = low)P(r = ∗∗|m = strong,d = low) P(e = high|m = strong)P(letter = weak|∗∗)
        resultOne = inference.forward_sample(size=10000, return_type='recarray')
        # Musicianship = 0, Exam = 1, Difficulty = 2, Rating = 3, Letter = 4
        # Musicianship = 0
        musSum = 0
        for sample in resultOne:
                if sample[0] == 1:
                    musSum += 1
        musProb = musSum/10000
        print('music prob: ', musProb)

        difSum = 0
        for sample in resultOne:
                if sample[2] == 0:
                    difSum += 1
        diffProb = difSum/10000
        print('difficulty prob: ', diffProb)

        examSum = 0
        for sample in resultOne:
                if sample[1] == 1 and sample[0] == 1:
                    examSum += 1
        examProb = (examSum/10000) / musProb
        print('exam prob: ', examProb)

        ratingSum = 0
        for sample in resultOne:
                if sample[3] == 1 and sample[0] == 1 and sample[2] == 0:
                    ratingSum += 1
        ratingProb = (ratingSum/10000)/ (diffProb * musProb)
        print('rating prob: ', ratingProb)

        letterSum = 0
        for sample in resultOne:
                if sample[4] == 0 and sample[3] == 1:
                    letterSum += 1
        letterProb = (letterSum/10000) / ratingProb
        print('letter prob: ', letterProb)

        letterStrongSum = 0
        for sample in resultOne:
                if sample[4] == 1:
                    letterStrongSum += 1
        letterStrongSumProb = (letterStrongSum/10000)
        print('letter strong no evidence prob: ', letterStrongSumProb)

        letterStrongGivenMusicianshipSum = 0
        for sample in resultOne:
                if sample[4] == 1 and sample[0] == 0:
                    letterStrongGivenMusicianshipSum += 1
        letterStrongGivenProb = (letterStrongGivenMusicianshipSum/10000) / (1-musProb)
        print('letter strong given weak music prob: ', letterStrongGivenProb)



bayesianNetwork = BayesianNetworkApproximateInference()
bayesianNetwork.start()