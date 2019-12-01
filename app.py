from flask import Flask, request, render_template, abort, redirect, url_for
from flask_bootstrap import Bootstrap
from crwaler import app as crwaler

app = Flask(__name__)
bootstrap = Bootstrap(app)

CAMBRIDGE = 1
OXFORD = 2

@app.route('/')
def index():
  return render_template('index.html'), 200

@app.route('/search/cam', methods=['POST'])
def search():
  if request.method == 'POST':
    word = request.form['search']
    return redirect(url_for('cam_show', word=word))
  else:
    abort(500)

@app.route('/search/cam/<string:word>')
def cam_show(word):
  obj_array,item_array = crwaler.cam_crwaler(word)
  return render_template('page.html',
   obj_array=obj_array, item_array=item_array, temple=CAMBRIDGE, word=word), 200

@app.route('/search/oxf/<string:word>')
def oxf_show(word):
  obj, item_array = crwaler.oxf_crwaler(word)
  return render_template('page.html', obj=obj, item_array=item_array, temple=OXFORD, word=word), 200

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html',error=error), 404

@app.errorhandler(500)
def server_down(error):
  return render_template('500.html',error=error), 500

if __name__ == "__main__":
    app.run(debug=True)
