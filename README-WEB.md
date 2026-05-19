# 🌐 SNAKE BIDY – Version Web (WebAssembly)

Ce guide explique comment compiler, tester en local et déployer **Snake Bidy** pour y jouer directement depuis n'importe quel navigateur web grâce à **Pygbag** et WebAssembly (WASM).

---

## 🎮 Instructions pour le Joueur (UX Web)

Pour garantir une expérience de jeu fluide sur le Web et éviter les comportements inattendus du navigateur (comme le défilement de la page), voici les consignes à suivre :

1. **Focus sur le jeu :** Une fois la page chargée, **cliquez à l'intérieur de la fenêtre du jeu** pour capturer les entrées de votre clavier.
2. **Commandes :**
   * `Flèches Directionnelles` : Déplacement du serpent.
   * `Touche ESPACE` : Mettre en pause.
   * `Touche ENTRÉE` : Reprendre la partie.

---

## 🏗️ 1. Adaptation Asynchrone du Code (`Fenetre.py`)

Les navigateurs web ne supportent pas les boucles infinies bloquantes (`while True`). Pour que le jeu tourne sur le Web, la boucle principale dans `Fenetre.py` doit céder le contrôle au navigateur à chaque frame via `asyncio`.

Modifier la boucle principale de la manière suivante :

```python
import asyncio
import pygame

# 1. Transformer la fonction ou méthode principale en fonction asynchrone
async def main_loop():
    # ... initialisation du jeu ...
    
    is_running = True
    while is_running:
        # ... logique de ton jeu (midona, voaHinana, dessin) ...
        
        pygame.display.update()
        
        # 2. OBLIGATOIRE : Permet au navigateur de rafraîchir la page
        await asyncio.sleep(0) 

# 3. Lancer la boucle via le gestionnaire asynchrone
asyncio.run(main_loop())
```

## 🛠️ 2. Exécution et Test Local

Pygbag intègre un serveur de test local pour vérifier le comportement du jeu avant sa publication.

Installez le compilateur Pygbag :
```bash
pip install pygbag
```

Lancez l'environnement de build à la racine de votre projet (là où se trouve votre script principal) :

```bash
pygbag .
```

Ouvrez votre navigateur et accédez à l'adresse locale :
👉 http://localhost:8000