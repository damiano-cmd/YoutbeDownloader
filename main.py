from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pytube
import youtube_dl

def downmp3(link):
    #for link in mp3s:
        video_inf = youtube_dl.YoutubeDL().extract_info(url=link,download=False)
        filename = str(video_inf['title'])+'.mp3'
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': 'C:\\Users\\Dell\\Downloads\\'+'"'+filename+'"',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        with youtube_dl.YoutubeDL(options) as ytd:
            ytd.download([video_inf['webpage_url']])

def downmp4(link):
    print(link)
    youtube = pytube.YouTube(link)
    vid = youtube.streams.filter(res = '720p', file_extension = 'mp4', progressive=True).first()
    if vid == None:
        vid = youtube.streams.filter(res = '144p', file_extension = 'mp4', progressive=True).first()
    vid.download('C:/Users/Dell/Downloads/')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def main():
    return jsonify({"s": "You are connected"})

@app.route('/mp3', methods=['POST'])
def mp3():
    link = request.get_json()
    link = link['link']
    #mp3s = mp3s + [link]
    downmp3(link)
    return jsonify({"s": "done"})
    

@app.route('/mp4', methods=['POST'])
def mp4():
    link = request.get_json()
    downmp4(link['link'])
    return jsonify({"s": "done"})

if __name__ == '__main__':
    app.run()
