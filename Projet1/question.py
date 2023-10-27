# question.py
import random

class Question:
    def __init__(self, enonce, reponses, reponse_correcte):
        self.enonce = enonce
        self.reponses = reponses
        self.reponse_correcte = reponse_correcte

    def melanger_reponses(self):
        # Mélanger les réponses tout en maintenant la réponse correcte à la même position
        reponses_melees = self.reponses.copy()
        random.shuffle(reponses_melees)

        # Trouver la nouvelle position de la réponse correcte
        nouvelle_position = reponses_melees.index(self.reponses[ord(self.reponse_correcte) - 97])

        # Mettre à jour la liste des réponses mélangées
        self.reponses = reponses_melees

        # Mettre à jour la réponse correcte en fonction de la nouvelle position
        self.reponse_correcte = chr(97 + nouvelle_position)

    def poser_question(self):
        self.melanger_reponses()  # Mélanger les réponses
        print(self.enonce)
        for i, reponse in enumerate(self.reponses):
            print(f"{chr(97 + i).upper()}. {reponse}")

    def verifier_reponse(self, reponse_utilisateur):
        return reponse_utilisateur.lower() == self.reponse_correcte
