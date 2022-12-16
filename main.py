# Sebastian Vera : worked on youtube search and open ai image search
# Camille Clendenon : worked on flask website and implementing search bars
# Barrett Reinhard : worked on css and rendering images and youtube videos on page

from flask import Flask, request, render_template
# from jinja2 import Environment, FileSystemLoader
import os
import openai
import urllib.request
import re
import credentials
# from flask_bootstrap import Bootstrap5, Bootstrap
# flask --app temp.py --debug run
app = Flask(__name__)
# boostrap = Bootstrap(app)

root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, 'html', 'project_template.html')

@app.route('/')
def home():
    return render_template('project_template.html')

@app.route('/', methods = ['POST'])
def image():
    #open ai generation - requires api key in credentials.py - we use gitignore to hide key - key in trello
    image_des = request.form.get("idescript").lower()
    #resource: https://www.youtube.com/watch?v=czx7CxzcJzQ
    response = openai.Image.create(  prompt = image_des, 
    n=1, #number of images to generate
    size="1024x1024"
    )
    #retrieves url of image
    image_url = response['data'][0]['url']

    #youtube search
    youtube_search_list = []
    #splits the searches by the comma
    genre = request.form.get("genre").split(", ")
    #makes every element in list have a + in place of a space
    genre = [string.replace(' ', '+') for string in genre]
    for youtube_search in genre:
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={youtube_search}")
        #if kanye is searched for, skip over
        if youtube_search.lower() == "kanye": 
            continue
        #uses regex. Each video has an 11 character sequence. This should match every 11 character sequence and store in list
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        final_url = "https://www.youtube.com/embed/"
        #takes the first 11 char sequence video id i.e. first result from search and appends this to the search list
        youtube_search_list.append((f"{final_url}{video_ids[0]}"))

    # return "Your description was: \"" + image_url + "\" and your Genre was: \"" + str(youtube_search_list) + "\""

    return render_template('playlist.html', img_url = image_url, yt_url = youtube_search_list)

if __name__ == '__main__':
    app.run(debug=True)
# https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/