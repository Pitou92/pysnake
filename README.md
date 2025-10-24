# PySnake 🐍

Un jeu **Snake** développé en Python avec **Pygame**.  
Conçu pour être modulaire, maintenable et facile à étendre.

---

## 🎮 À propos du jeu

- Contrôlez le serpent avec les touches fléchées.  
- Mangez les fruits rouges pour grandir.  
- Le jeu se termine si le serpent touche un mur ou se mord lui-même.  
- Score affiché dans la console à la fin du jeu.

---

## 📂 Structure du projet

pysnake/  
├── snake/ # Code du jeu  
│ ├── init.py  
│ ├── game.py # Boucle principale du jeu  
│ ├── snake.py # Classe Snake  
│ ├── fruit.py # Classe Fruit  
│ └── settings.py # Constantes et configurations  
├── tests/ # Tests unitaires  
│ └── test_snake.py  
├── main.py # Point d'entrée du jeu  
├── requirements.txt # Dépendances Python  
└── README.md # Ce fichier  

---

## 🚀 Installation

1. **Cloner le dépôt :**
```bash
git clone <URL_DU_DEPOT>
cd pysnake
```

Créer et activer un environnement virtuel :

```bash
python -m venv venv
```

# Windows
```bash
.\venv\Scripts\activate
```
# macOS / Linux
```bash
source venv/bin/activate
```
Installer les dépendances :

```bash
pip install -r requirements.txt
```
🏃 Lancer le jeu

```bash
python main.py
```

🧪 Tests
Pour lancer les tests unitaires :

```bash
pytest
```

⚙️ Personnalisation
Les paramètres du jeu (taille de l’écran, vitesse, couleurs…) sont dans snake/settings.py.
Modifiez-les pour ajuster le jeu à votre goût.

💡 Bonnes pratiques suivies
Code modulaire et orienté objet (classes Snake et Fruit).

Fichier de configuration pour les constantes.

Tests unitaires pour la logique du jeu.

Structure prête pour futures extensions : score, obstacles, menus, etc.
