from datetime import datetime as dt

from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template


FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = ''
POST_DIR = 'posts'

app = Flask(__name__)

flatpages = FlatPages(app)
app.config.from_object(__name__)


@app.route('/blog')
def blog():
    posts = [p for p in flatpages if p.path.startswith('posts')]
    posts.sort(key=lambda item: dt.strptime(item['date'], '%B %d, %Y'), reverse=True)
    return render_template('blog.html', posts=posts)


@app.route('/blog/<permalink>')
def blog_post(permalink):
    path = f'{POST_DIR}/{permalink}'
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
