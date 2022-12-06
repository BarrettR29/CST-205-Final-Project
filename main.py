from flask import Flask, request, render_template
import os
import openai
import urllib.request
import re
# from flask_bootstrap import Bootstrap5, Bootstrap
# flask --app temp.py --debug run 
app = Flask(__name__)
# boostrap = Bootstrap(app)

openai.api_key = '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'


@app.route('/')
def home():
    return render_template('project_template.html')

@app.route('/', methods = ['POST'])
def image():
    #open ai generation
    image_des = request.form.get("idescript").lower()
    #resource: https://www.youtube.com/watch?v=czx7CxzcJzQ
    response = openai.Image.create(  prompt = image_des, 
    n=2,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

    #youtube search
    youtube_search_list = []
    genre = request.form.get("genre").split(", ")
    #works! makes every element in list have a + if space
    genre = [string.replace(' ', '+') for string in genre]
    for youtube_search in genre:
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={youtube_search}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        final_url = "https://www.youtube.com/watch?v="
        youtube_search_list.append((f"{final_url}{video_ids[0]}"))

    return "Your description was: \"" + image_url + "\" and your Genre was: \"" + str(youtube_search_list) + "\""



if __name__ == '__main__':
    app.run(debug=True)
# https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/