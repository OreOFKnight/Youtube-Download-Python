from pytubefix import YouTube # importando a biblioteca de download do youtube
from pytubefix.cli import on_progress

try: # faco ele tentar pq pode quebrar o codigo

    url = input("digite a url do video: ") # pego a url da pessoa

    yt = YouTube(url, on_progress_callback = on_progress) # pega as informacoes do video
    print(yt.title) # printa o titulo do video

    ys = yt.streams.get_highest_resolution() # pega o video com maior resolucao
    ys.download() # baixa o video

except: # caso der erro ao baixar
    print("erro ao baixar o video")