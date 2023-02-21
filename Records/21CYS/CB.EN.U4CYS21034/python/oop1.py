class individual:
    def __init__(self,character_name):
        self.character_name = character_name
    def get_character_name(self):
        return self.character_name
individual1=individual('BUSTER')
print(individual1.get_character_name())
individual2=individual('tobias')
print(individual2.get_character_name())


