from flask.globals import request
from flask import Flask, render_template
import requests
from cairosvg import svg2png

"""DIRETORIO = "/home/luiz/Dropbox/ufopa/8 semestre/Sistemas_distribuídos/Projeto_Free WordCloud_/\
            Wordcloud from text/Cliente/static/images"""

api = Flask(__name__)
link = "http://127.0.0.1:5000/wordcloud?text="

@api.route("/")
def home():
    return render_template("index.html")

@api.route("/gerar", methods = ["GET", "POST"])
def gerar():
    text = request.form["texto"]
    #print(text)
    try:
        response = requests.get(link+text)
    except:
        return "Erro ao gerar wordcloud"
    svg = response.content
    svg2png(bytestring=svg,write_to='./static/images/wordcloud.png')

    return render_template("index.html")

"""@api.route("/baixar", methods=["GET"])
def baixar():
    return send_from_directory(DIRETORIO, "./static/images/wordcloud.png", as_attachment=True)"""
    #redirect(url_for('static', filename='./images/wordcloud.png'))

        

if __name__ == "__main__":
    api.run(debug=True, port=8000)




    