import WordCloud
from flask import Flask, request

api = Flask(__name__)

@api.route("/wordcloud", methods=["GET"])
def get_wordcloud():
    text = request.args.get('text')
    color = request.args.get('cor')
    tema = request.args.get('tema')
    try:
        svg_img = WordCloud.make_wordcloud(text, color, tema).to_svg()
    except(ValueError):
        return "Texto deve possuir ao menos uma palavra"

    return svg_img

if __name__ == "__main__":
    api.run(debug=True, port=5000)




    