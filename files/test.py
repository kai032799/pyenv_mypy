import sys
sys.path.append('/Users/tokisato/mypy/lib/python3.12/site-packages')

from pytubefix import YouTube # type: ignore
from pytubefix.cli import on_progress # type: ignore

url = 'https://www.youtube.com/shorts/Br98a7G8lUk'

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download()