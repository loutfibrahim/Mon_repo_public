#generate_password
import random
import string
import math

class PasswordGenerator:
    def __init__(self, min_lower, min_upper, min_digits, min_special):
        self.min_lower = min_lower
        self.min_upper = min_upper
        self.min_digits = min_digits
        self.min_special = min_special

    def generate_password(self):
        # Génère un mot de passe en fonction des critères
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.min_lower))
        password += ''.join(random.choice(string.ascii_uppercase) for _ in range(self.min_upper))
        password += ''.join(random.choice(string.digits) for _ in range(self.min_digits))
        password += ''.join(random.choice(string.punctuation) for _ in range(self.min_special))
        # password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12 - len(password)))
        return ''.join(random.sample(password, len(password)))

    def calculate_entropy(self, password):
        # Calcule l'entropie d'un mot de passe
        character_set = string.ascii_letters + string.digits + string.punctuation
        entropy = math.log2(len(character_set) ** len(password))
        return entropy
