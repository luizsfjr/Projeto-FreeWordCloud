import WordCloud
from flask import Flask, request

api = Flask(__name__)

@api.route("/wordcloud", methods=["GET"])
def get_wordcloud():
    text = request.args.get('text')
    color = request.args.get('cor')
    svg_img = WordCloud.make_wordcloud(text, color).to_svg()
    return svg_img

if __name__ == "__main__":
    api.run(debug=True, port=5000)




    