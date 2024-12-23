from flask import Flask, render_template, request, send_file
from wordcloud import WordCloud
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    if not text:
        return "Please provide text to generate the word cloud.", 400

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    image_path = "static/wordcloud.png"
    wordcloud.to_file(image_path)

    return render_template('index.html', wordcloud_image=image_path)

if __name__ == '__main__':
    app.run(debug=True)
