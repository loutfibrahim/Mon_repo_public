import unittest
from question import Question
from qcm import QCM

class TestProgram(unittest.TestCase):
    def test_qcm_complet(self):
        # Créez un QCM avec des questions
        qcm = QCM()
        questions = [
            Question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin"], "a"),
            # ... Ajoutez d'autres questions ici ...
        ]
        for question in questions:
            qcm.ajouter_question(question)

        # Simulez l'entrée utilisateur (vous pouvez utiliser unittest.mock.patch)
        # Appelez la méthode passer_qcm pour exécuter le QCM
        # Utilisez les méthodes d'assertion pour vérifier les résultats
