# Convertisseur YouTube MP3/MP4

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

Une application desktop simple et élégante pour télécharger des vidéos YouTube en format MP4 ou MP3, développée en Python.

## 🛠️ Technologies utilisées

- **Language:** Python 3.x
- **Interface graphique:** CustomTkinter
- **Bibliothèques principales:**
  - `yt-dlp`: Pour le téléchargement YouTube
  - `customtkinter`: Pour l'interface graphique moderne
  - `threading`: Pour la gestion des téléchargements asynchrones

## ✨ Fonctionnalités

- Interface graphique moderne avec CustomTkinter
- Téléchargement de vidéos YouTube en MP4
- Extraction audio en format MP3
- Sélection de la qualité vidéo (144p à 1080p)
- Barre de progression en temps réel
- Interface en français

## 📋 Prérequis

- Python 3.x installé sur votre système
- Connexion Internet

## 🚀 Installation

1. Clonez le repository :
```bash
git clone https://github.com/VOTRE-USERNAME/convertisseur_MP3_MP4.git
cd convertisseur_MP3_MP4
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

1. Lancez l'application :
```bash
python main.py
```

2. Collez l'URL YouTube dans le champ prévu
3. Choisissez le format (Vidéo MP4 ou Audio MP3)
4. Sélectionnez la qualité pour les vidéos
5. Cliquez sur "Télécharger"

Les fichiers seront sauvegardés dans le dossier "downloads".

## 📁 Structure du projet

```
convertisseur_MP3_MP4/
├── main.py              # Programme principal
├── requirements.txt     # Dépendances Python
├── install_ffmpeg.py    # Script d'installation ffmpeg
├── README.md           # Documentation
└── LICENSE             # Licence MIT
```

## 📝 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Développeur

- [@VOTRE-USERNAME](https://github.com/VOTRE-USERNAME)
