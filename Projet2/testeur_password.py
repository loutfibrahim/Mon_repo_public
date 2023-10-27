#testeur_password
from generateur_password import PasswordGenerator
class PasswordTester:
    def __init__(self):
        self.anssi_criteria = {
            'lower': 26,
            'upper': 26,
            'digit': 10,
            'special': 32
        }

    def test_password(self, password):
        # Teste la force d'un mot de passe basé sur l'entropie
        password_generator = PasswordGenerator(4, 4, 2, 2)
        entropy = password_generator.calculate_entropy(password)
        strength = "Faible"
        if entropy >= 80:
            strength = "Fort"
        elif entropy >= 60:
            strength = "Moyen"
        return entropy, strength
