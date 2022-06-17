from flask.globals import request
from flask import Flask, render_template
import requests
from cairosvg import svg2png


api = Flask(__name__)
link = "http://127.0.0.1:5000/wordcloud"

@api.route("/")
def home():
    return render_template("index.html")

@api.route("/gerar", methods = ["GET", "POST"])
def gerar():
    text = "?text="+request.form["texto"]
    cor = "&cor="+request.form["cor"]
    tema = "&tema="+request.form["tema"]
    try:
        response = requests.get(link+text+cor+tema) #comunicação com outro sistema
        svg = response.content # pega a resposta
        svg2png(bytestring=svg,write_to='./static/images/wordcloud.png')
    except:
        return "Erro ao gerar wordcloud"

    return render_template("index.html")
        

if __name__ == "__main__":
    api.run(debug=True, port=8000)




    