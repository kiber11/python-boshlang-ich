import pytubefix
from pytubefix import YouTube
from http.client import IncompleteRead

def download_video(url, output_path, filename):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=output_path, filename=filename)
        print("Video muvaffaqiyatli yuklandi!")
    except IncompleteRead as e:
        print(f"IncompleteRead xatosi: {e}. Qayta urinish...")
        download_video(url, output_path, filename)  
    except Exception as e:
        print(f"Boshqa xato: {e}")


url = "https://youtu.be/DVqFyinDgE4?si=B9TsvkiO_ZDTlXpQ"
output_path = r"C:\Users\abdul\Downloads\Telegram Desktop"
filename = "my_video.mp4"


download_video(url, output_path, filename)
