#main_mdp
from generateur_password import PasswordGenerator
from testeur_password import PasswordTester
from generateur_passphrase import PassphraseGenerator

# Lisez la liste de mots de passe EFF Diceware depuis le fichier
with open(r"C:\Users\LOUTFI Brahim\Mon_repo_public\myenv\eff_large_wordlist.txt", "r") as file:
    word_list = [line.strip() for line in file]


while True:
    print("\n___________________ Menu: ___________________\n")
    print("1. Générer un mot de passe")
    print("2. Générer une passphrase")
    print("3. Vérifier un mot de passe")
    print("4. Quitter")

    choix = input("Sélectionnez une option (1/2/3/4) : ")

    if choix == "1":
        # Demandez à l'utilisateur d'entrer les critères
        print("\n_____________________________________________\n")
        min_upper = int(input("Entrer le nombre de lettres majuscules : "))
        print("\n_____________________________________________\n")
        min_lower = int(input("Entrer le nombre de lettres minuscules : "))
        print("\n_____________________________________________\n")
        min_digits = int(input("Entrer le nombre de chiffres : "))
        print("\n_____________________________________________\n")
        min_special = int(input("Entrer le nombre de caractères spéciaux : "))
        print("\n_____________________________________________\n")

        # Créez une instance de PasswordGenerator avec les critères de l'utilisateur
        password_generator = PasswordGenerator(min_lower, min_upper, min_digits, min_special)

        # Générez un mot de passe
        password = password_generator.generate_password()

        # Testez le mot de passe
        entropy, strength = PasswordTester().test_password(password)

        # Affichez le mot de passe généré, son entropie et sa force
        print(f"Le mot de passe généré est : {password}")
        print(f"Entropie : {entropy}")
        print(f"Force : {strength}")
        print("\n_____________________________________________\n")

    elif choix == "2":
        # Demandez à l'utilisateur le nombre de mots dans la passphrase
        print("\n_____________________________________________\n")
        num_words = int(input("Combien de mots souhaitez-vous dans la passphrase : "))

        # Générez la passphrase en utilisant le générateur de passphrase
        print("\n_____________________________________________\n")
        passphrase_generator = PassphraseGenerator(word_list)
        passphrase = passphrase_generator.generate_passphrase(num_words)

        # Affichez la passphrase générée
        print(f"Passphrase générée : {passphrase}")

    elif choix == "3":
        # Demandez à l'utilisateur de saisir un mot de passe à tester
        print("\n_____________________________________________\n")
        user_password = input("Saisissez un mot de passe à tester : ")

        # Testez le mot de passe saisi par l'utilisateur
        tester = PasswordTester()
        entropy, strength = tester.test_password(user_password)

        # Affichez les résultats pour le mot de passe saisi
        print("\n_____________________________________________\n")
        print(f"Mot de passe saisi : {user_password}")
        print(f"Entropie : {entropy}")
        print(f"Force : {strength}")
        print("\n_____________________________________________\n")

    elif choix == "4":
        break  # Quitter le programme

    else:
        print("Option invalide. Sélectionnez 1, 2 ou 3.")
