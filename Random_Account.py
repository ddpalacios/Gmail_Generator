import random
import string


class Random_Gen:

    def random_pass(self, stringLength=10):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(stringLength))

    def random_first(self):
        names = ["dave", "bill", "bob"]
        return random.choice(names)

    def random_last(self):
        last = ["dfsdsfs", "fsdfew", "dsfsdf"]
        return random.choice(last)

    def randomUser(self, stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.sample(letters, stringLength))
