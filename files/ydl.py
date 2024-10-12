import sys
sys.path.append('/Users/tokisato/mypy/lib/python3.12/site-packages')

from yt_dlp import YoutubeDL

# 下記URLの動画を最高画質で取得
link = 'https://www.youtube.com/shorts/Br98a7G8lUk'

ydl_opts = {
    'format': 'bestvideo+bestaudio/best', 
    'outtmpl': 'movie.webm'
}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])