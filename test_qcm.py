# test_qcm.py
import unittest
from question import Question
from qcm import QCM

class TestQuestion(unittest.TestCase):
    def setUp(self):
        """Initialise les données de test avant chaque méthode de test"""
        self.question = Question(
            "Test question?",
            ["Réponse 1", "Réponse 2", "Réponse 3"],
            1  # La bonne réponse est l'index 1 (deuxième réponse)
        )

    def test_verifier_reponse_correcte(self):
        """Teste si une bonne réponse est correctement validée"""
        self.assertTrue(self.question.verifier_reponse('b'))
        self.assertTrue(self.question.verifier_reponse('B'))

    def test_verifier_reponse_incorrecte(self):
        """Teste si une mauvaise réponse est correctement invalidée"""
        self.assertFalse(self.question.verifier_reponse('a'))
        self.assertFalse(self.question.verifier_reponse('c'))

class TestQCM(unittest.TestCase):
    def setUp(self):
        """Initialise un QCM avant chaque test"""
        self.qcm = QCM()

    def test_nombre_questions(self):
        """Vérifie que le QCM contient bien 10 questions"""
        self.assertEqual(len(self.qcm.questions), 10)

    def test_score_initial(self):
        """Vérifie que le score initial est 0"""
        self.assertEqual(self.qcm.score, 0)

    def test_initialisation_reponses_utilisateur(self):
        """Vérifie que le dictionnaire des réponses est vide au départ"""
        self.assertEqual(len(self.qcm.reponses_utilisateur), 0)

    def test_questions_differentes(self):
        """Vérifie que toutes les questions sont différentes"""
        textes_questions = [q.texte for q in self.qcm.questions]
        self.assertEqual(len(textes_questions), len(set(textes_questions)))

if __name__ == '__main__':
    unittest.main()