import os
import zipfile
import requests
from pathlib import Path
import sys
import shutil

def download_ffmpeg():
    print("Téléchargement de ffmpeg...")
    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    
    # Créer un dossier temporaire
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)
    
    # Télécharger le fichier
    response = requests.get(url, stream=True)
    zip_path = temp_dir / "ffmpeg.zip"
    
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    print("Extraction des fichiers...")
    # Extraire le fichier ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Trouver le dossier ffmpeg extrait
    ffmpeg_dir = next(temp_dir.glob("ffmpeg-master-*"))
    bin_dir = ffmpeg_dir / "bin"
    
    # Ajouter ffmpeg au PATH
    ffmpeg_path = str(bin_dir.absolute())
    
    if ffmpeg_path not in os.environ['PATH']:
        print(f"Ajout de ffmpeg au PATH: {ffmpeg_path}")
        os.environ['PATH'] += os.pathsep + ffmpeg_path
        
        # Modification permanente du PATH pour l'utilisateur
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS) as key:
            try:
                path_value, _ = winreg.QueryValueEx(key, 'Path')
                if ffmpeg_path not in path_value:
                    new_path = path_value + os.pathsep + ffmpeg_path
                    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path)
            except WindowsError:
                winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, ffmpeg_path)
    
    print("Installation terminée!")
    print("Veuillez redémarrer votre application pour utiliser ffmpeg.")
    
    # Nettoyer les fichiers temporaires
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    try:
        download_ffmpeg()
    except Exception as e:
        print(f"Erreur lors de l'installation: {str(e)}")
        input("Appuyez sur Entrée pour quitter...")
