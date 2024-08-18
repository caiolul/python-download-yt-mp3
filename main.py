import yt_dlp

def baixar_audio_yt_dlp(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def run():
    print("Iniciando o download do áudio do vídeo...")
    list_urls_str = input("Digite uma lista de números separados por vírgula: ")
    list_url = list_urls_str.split(',')
    for video_url in list_url:
        baixar_audio_yt_dlp(video_url)
    print("Download concluído!")

if __name__ == '__main__':
    run()