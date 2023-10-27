# qcm.py

import random
from question import Question

class QCM:
    def __init__(self):
        self.questions = []  # Liste pour stocker les questions

    def ajouter_question(self, question):
        self.questions.append(question)

    def melanger_questions(self):
        random.shuffle(self.questions)

    def afficher_qcm(self):
        for question in self.questions:
            question.poser_question()

    def passer_qcm(self):
        score = 0
        reponses_correctes = {}  # Pour stocker les réponses correctes

        for question in self.questions:
            print("______________________________________________________________________\n")
            question.poser_question()

            while True:
                try:
                    reponse_utilisateur = input("Votre réponse (a/b/c) : ").lower()
                    if reponse_utilisateur not in ['a', 'b', 'c']:
                        raise ValueError("Veuillez choisir une réponse parmi les options a, b, ou c.")

                    reponse_correcte = question.reponses[ord(question.reponse_correcte) - 97]

                    if question.verifier_reponse(reponse_utilisateur):
                        score += 1
                        reponses_correctes[question.enonce] = reponse_correcte
                        print("Bonne réponse !")
                    else:
                        reponses_correctes[question.enonce] = reponse_correcte
                        print("Mauvaise réponse.")
                    break  # Sortez de la boucle une fois que la réponse de l'utilisateur est valide
                except ValueError as e:
                    print(e)

        print("\n______________________________________________________________________\n")
        print(f"Score final : {score}/{len(self.questions)}")

        # Affiche le corrigé
        print("Corrigé :")
        for question in reponses_correctes:
            print(f"Question : {question}")
            print(f"Réponse correcte : {reponses_correctes[question]}\n")
        print("\n______________________________________________________________________\n")
        return score
