import WordCloud
import matplotlib.pyplot as plt
import os
from flask import Flask, request, jsonify, send_file, send_from_directory

"""DIRETORIO = "/home/luiz/Dropbox\
            /ufopa/8 semestre/Sistemas_distribuídos/\
            Projeto_Free WordCloud_/Wordcloud from text/Servidor-Back/output"""

api = Flask(__name__)

@api.route("/wordcloud", methods=["GET"])
def get_wordcloud():
    text = request.args.get('text')
    svg_img = WordCloud.make_wordcloud(text).to_svg()
    #img = WordCloud.make_wordcloud(text).to_image().save('./output/img2.jpg')
    return svg_img
    #return svg_img


"""# Útil apenas para interface web
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment=True)"""
    

if __name__ == "__main__":
    api.run(debug=True, port=5000)




    