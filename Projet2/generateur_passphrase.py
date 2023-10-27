#generate_passphrase
import random

class PassphraseGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_passphrase(self, num_words):
        passphrase = ' '.join(random.choice(self.word_list) for _ in range(num_words))
        return passphrase
