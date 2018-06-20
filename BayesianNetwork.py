from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class BayesianNetwork:
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
        infer = VariableElimination(self.musicModel)
        examResult = infer.query(
            variables=['Exam'], evidence={'Musicianship':1})['Exam']
        musicResult = infer.query(
            variables=['Musicianship'])['Musicianship']
        ratingResult = infer.query(
            variables=['Rating'], evidence={'Musicianship':1, 'Difficulty':0})['Rating']
        diffResult = infer.query(
            variables=['Difficulty'])['Difficulty']
        letterResult = infer.query(
            variables=['Letter'], evidence={'Rating':1})['Letter']

        print(examResult)
        print(musicResult)
        print(ratingResult)
        print(diffResult)
        print(letterResult)

        # THIS IS NOT WORKING IT IS PART 2 Getting weird results
        letterNoOtherEvidence = infer.query(
             variables=['Letter'])['Letter']
        letterResult = infer.query(
                 variables=['Letter'], evidence={'Musicianship':0})['Letter']
        print(letterNoOtherEvidence)
        print(letterResult)
        print('')



bayesianNetwork = BayesianNetwork()
bayesianNetwork.start()