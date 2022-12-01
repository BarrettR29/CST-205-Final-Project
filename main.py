from flask import Flask, request, render_template
# from flask_bootstrap import Bootstrap5, Bootstrap
# flask --app temp.py --debug run 
app = Flask(__name__)
# boostrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('project_template.html')

@app.route('/', methods = ['POST'])
def image():
    # if request.methods == "POST":
    image_des = request.form.get("idescript")
    genre = request.form.get("genre").split(", ")
    return "Your description was: \"" + image_des.lower() + "\" and your Genre was: \"" + str(genre) + "\""

    # return render_template('project_template.html')

if __name__ == '__main__':
    app.run(debug=True)
# https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/