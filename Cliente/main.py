from flask.globals import request
from flask import Flask, render_template
import requests
from cairosvg import svg2png


api = Flask(__name__)
link = "http://127.0.0.1:5000/wordcloud?text="

@api.route("/")
def home():
    return render_template("index.html")

@api.route("/gerar", methods = ["GET", "POST"])
def gerar():
    text = request.form["texto"]
    cor = "&cor="+request.form["cor"]
    try:
        response = requests.get(link+text+cor)
    except:
        return "Erro ao gerar wordcloud"
    svg = response.content
    svg2png(bytestring=svg,write_to='./static/images/wordcloud.png')

    return render_template("index.html")
        

if __name__ == "__main__":
    api.run(debug=True, port=8000)




    