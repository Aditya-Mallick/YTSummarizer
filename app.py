from flask import Flask, Response, request
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi as YTApi

video_url = "www.youtube.com/watch?v=UF8uR6Z6KLc"

def getTranscript(video_id):
    transcript_json = YTApi.get_transcript(video_id)
    transcript = ''
    for i in transcript_json:
        if 'text' in i:
            transcript += ' ' + i['text']
    return transcript

def getSummary(video_id):
    transcript = getTranscript(video_id)
    print(len(transcript))
    summarizer = pipeline('summarization')
    num_iters = int(len(transcript)/800)
    start, end = 0, 800
    summary = ''
    for _ in range(num_iters):
        summary += summarizer(transcript[start:end])[0]['summary_text'] + ' '
        start, end = end, end+800
    print(summary)
    return Response(status=201) 

app = Flask('__name__')
@app.route('/Aditya/api/summarize', methods=["GET", "POST", "PUT"])
def summary():
    url = request.args.get('youtube_url')
    video_id = url.split('=')[1]
    summary = getSummary(video_id)
    print(summary)
    return Response(status=200)

app.run(debug=True)