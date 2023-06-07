#import all necessary modules
import yt_dlp
from mutagen.easyid3 import EasyID3
import os

#declare a function for extracting and downloading audio
def download_and_tag_audio():
    url = input("Enter audio url: ")
    genre = input("Genre of this music:\t")
    directory = os.path.expanduser('~/Music/')
    ytdl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
                    }],
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
    }
    ytdl = yt_dlp.YoutubeDL(ytdl_options) 
    info = ytdl.extract_info(url, download=False)
        
    if info is None:
            print("Error 404!")
    #note: The audio with character "|" can't be downloaded
    else:
        # Replace '|' character in title
        info['title'] = info['title'].replace('|', '-')        
        # Download audio
        ytdl.download(url)
        audio_file_path = ('/home/unish/Music/'+info['title']+'.mp3')
        metatag = EasyID3(audio_file_path)
        metatag['title'] = info['title']
        metatag['artist'] = info['uploader']
        metatag['genre'] = genre
        metatag.save()
    print("Download Completed.")

download_and_tag_audio()


