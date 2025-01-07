# qcm.py
import random
from question import Question

class QCM:
    def __init__(self):
        self.questions = self._initialiser_questions()
        self.score = 0
        self.reponses_utilisateur = {}

    def _initialiser_questions(self):
        """Initialise et mélange les questions"""
        questions = [
            Question("Quelle est la capitale de la France ?", 
                    ["Londres", "Paris", "Berlin"], 1),
            Question("Quel est le plus grand océan du monde ?", 
                    ["Atlantique", "Indien", "Pacifique"], 2),
            Question("Qui a peint la Joconde ?", 
                    ["Van Gogh", "Picasso", "Leonard de Vinci"], 2),
            Question("Quel est le symbole chimique de l'or ?", 
                    ["Ag", "Au", "Cu"], 1),
            Question("En quelle année a commencé la Révolution française ?", 
                    ["1789", "1792", "1795"], 0),
            Question("Quelle planète est surnommée la planète rouge ?", 
                    ["Venus", "Mars", "Jupiter"], 1),
            Question("Qui a écrit 'Les Misérables' ?", 
                    ["Victor Hugo", "Émile Zola", "Gustave Flaubert"], 0),
            Question("Quel est le plus long fleuve du monde ?", 
                    ["Nil", "Amazone", "Mississippi"], 1),
            Question("Dans quel pays se trouve le Taj Mahal ?", 
                    ["Inde", "Pakistan", "Bangladesh"], 0),
            Question("Quelle est la plus haute montagne du monde ?", 
                    ["Mont Blanc", "Kilimandjaro", "Mont Everest"], 2)
        ]
        random.shuffle(questions)  # Mélange les questions
        return questions

    def poser_questions(self):
        """Pose les questions dans un ordre aléatoire avec des réponses mélangées"""
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {question.texte}")
            
            # Création d'une liste de tuples (index_original, réponse)
            reponses_indexees = list(enumerate(question.reponses))
            # Mélange les réponses tout en gardant la trace de leur index original
            random.shuffle(reponses_indexees)
            
            # Affiche les réponses dans l'ordre mélangé
            mapping_reponses = {}  # Pour convertir la réponse utilisateur en index original
            for choix, (index_original, reponse) in enumerate(reponses_indexees):
                lettre = chr(97 + choix)  # 'a', 'b', 'c'
                print(f"{lettre}) {reponse}")
                mapping_reponses[lettre] = index_original
            
            # Demande la réponse à l'utilisateur
            while True:
                reponse = input("\nVotre réponse (a/b/c): ").lower()
                if reponse in ['a', 'b', 'c']:
                    break
                print("Veuillez répondre par a, b ou c.")
            
            # Vérifie si la réponse est correcte
            index_choisi = mapping_reponses[reponse]
            est_correct = (index_choisi == question.bonne_reponse)
            
            # Sauvegarde les informations de la réponse
            self.reponses_utilisateur[i] = {
                'lettre_choisie': reponse,
                'reponse_choisie': question.reponses[index_choisi],
                'bonne_reponse': question.reponses[question.bonne_reponse],
                'est_correct': est_correct
            }
            
            if est_correct:
                self.score += 1

    def afficher_resultats(self):
        """Affiche le score final et le corrigé"""
        print("\n" + "="*50)
        print("RÉSULTATS DU QCM")
        print("="*50)
        
        pourcentage = (self.score / len(self.questions)) * 100
        print(f"\nScore final : {self.score}/{len(self.questions)} ({pourcentage:.1f}%)")
        
        print("\nDétail des réponses :")
        print("-"*50)
        
        for i, question in enumerate(self.questions, 1):
            reponse = self.reponses_utilisateur[i]
            status = "✓" if reponse['est_correct'] else "✗"
            
            print(f"\nQuestion {i}: {question.texte}")
            print(f"Votre réponse:  {reponse['lettre_choisie']}) {reponse['reponse_choisie']} {status}")
            if not reponse['est_correct']:
                print(f"Bonne réponse: {reponse['bonne_reponse']}")
            print("-"*30)