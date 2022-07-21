class Dog:

    count = 0

    # optional, if you want to move the Dog instance counting responsibility up here
    # def __init__(self):
    #     Dog.count += 1

    def sleep(self):
        return "zzz"

    @classmethod
    def get_all_dog_count(cls):
        return cls.count


class Puggle(Dog):
    count = 0

    def __init__(self, name="unknown"):
        self.name = name

        Puggle.count += 1
        Dog.count += 1

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count



class Boxer(Dog):
    def __init__(self, name="unknown"):
        self.name = name
        Boxer.count += 1
        Dog.count += 1

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    @staticmethod
    def get_characteristics():
        return "Boxers are lovers, not fighters."

    @classmethod
    def get_breed_count(cls):
        return cls.count

