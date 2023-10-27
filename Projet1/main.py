# main.py

import random
from question import Question
from qcm import QCM

# Créez des questions et ajoutez-les au QCM
questions = [
    Question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin"], "a"),
    Question("Quelle est la couleur du ciel par temps clair ?", ["Bleu", "Vert", "Rouge"], "a"),
    Question("Combien de planètes dans notre système solaire ?", ["5", "8", "9"], "b"),
    Question("Quelle est la plus grande planète du système solaire ?", ["Mercure", "Vénus", "Jupiter"], "c"),
    Question("Quel est le composant principal de l'air que nous respirons ?", ["Azote", "Oxygène", "Dioxyde de carbone"], "b"),
    Question("Quelle est la distance moyenne entre la Terre et la Lune ?", ["100 000 km", "384 400 km", "1 000 000 km"], "b"),
    Question("Combien de doigts a une main ?", ["3", "4", "5"], "c"),
    Question("Quel est le plus grand océan du monde ?", ["Atlantique", "Pacifique", "Indien"], "b"),
    Question("Quelle est la capitale de l'Espagne ?", ["Paris", "Londres", "Madrid"], "c"),
    Question("Quel est le symbole chimique de l'oxygène ?", ["O2", "O3", "O"], "c")
]

print("\n____________________________ QCM ALEATOIRE ____________________________")
qcm = QCM()

for question in questions:
    qcm.ajouter_question(question)

qcm.melanger_questions()
score = qcm.passer_qcm()
print("\n______________________________________________________________________\n")
