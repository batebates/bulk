#!/usr/bin/env python


import praw,re,youtube_dl


options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl':u'%(id)s.%(ext)s',
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

reddit = praw.Reddit(client_id='id',
                     client_secret='secret',
                     user_agent='my user agent')

for submission in reddit.subreddit('Music').hot(limit=10):
    if(re.match("^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$",submission.url)):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([submission.url])
