import unittest
from generateur_passphrase import PassphraseGenerator
from generateur_password import PasswordGenerator
from testeur_password import PasswordTester

class TestMyProgram(unittest.TestCase):
    def test_passphrase_generator(self):
        word_list = ["apple", "banana", "cherry", "date", "elderberry"]
        generator = PassphraseGenerator(word_list)
        passphrase = generator.generate_passphrase(3)
        self.assertEqual(len(passphrase.split()), 3)

    def test_password_generator(self):
        generator = PasswordGenerator(4, 4, 2, 2)
        password = generator.generate_password()
        # Ajoutez des assertions appropriées pour tester les caractéristiques du mot de passe généré.

    def test_password_tester(self):
        tester = PasswordTester()
        entropy, strength = tester.test_password("ExempleMotDePasse")
        # Ajoutez des assertions appropriées pour tester l'entropie et la force du mot de passe.

if __name__ == '__main__':
    unittest.main()
