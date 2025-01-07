# question.py
class Question:
    def __init__(self, texte, reponses, bonne_reponse):
        self.texte = texte
        self.reponses = reponses
        self.bonne_reponse = bonne_reponse

    def verifier_reponse(self, reponse_utilisateur):
        conversion = {'a': 0, 'b': 1, 'c': 2}
        return conversion[reponse_utilisateur.lower()] == self.bonne_reponse