# Questionnaire à Choix Multiples (QCM)

Ce projet est un QCM interactif en Python permettant de :
- Tester vos connaissances avec 10 questions
- Répondre avec des choix multiples
- Obtenir votre score et un corrigé détaillé

## Fonctionnalités

- **📝 Questions et Réponses**
  - 10 questions de culture générale
  - 3 choix de réponses par question
  - Ordre aléatoire des questions et réponses
  
- **🎯 Interface Simple**
  - Réponses par a, b, ou c 
  - Navigation intuitive
  - Instructions claires

- **📊 Résultats**
  - Score final sur 10
  - Corrigé détaillé
  - Vue comparative des réponses données/correctes

## Installation

1. Cloner le repository :
```bash
git clone https://github.com/Ronel16/QCM_Python
cd QCM_Python
```

2. Vérifier que tous les fichiers sont présents :
- main.py
- qcm.py
- question.py
- test_qcm.py
- README.md

## Utilisation

Lancer le programme :
```bash
python main.py
```

## Tests

Lancer les tests unitaires :
```bash
python -m test_qcm
```

## Structure du Projet

- `main.py` : Point d'entrée du programme
- `qcm.py` : Gestion du QCM (questions, score, affichage)
- `question.py` : Classe pour la gestion des questions individuelles
- `test_qcm.py` : Tests unitaires du programme

## Auteur

Ronel BANKOLE