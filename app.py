from flask import Flask, request, render_template, abort, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from crawler import app as crawler
from weather import app as weather

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
  obj_array,item_array = crawler.cam_crawler(word)
  return render_template('page.html',
   obj_array=obj_array, item_array=item_array, temple=CAMBRIDGE, word=word), 200

@app.route('/search/oxf/<string:word>')
def oxf_show(word):
  obj, item_array = crawler.oxf_crawler(word)
  return render_template('page.html', obj=obj, item_array=item_array, temple=OXFORD, word=word), 200

@app.route('/weather')
def get_weather():
  province = request.args.get('province',type=str)
  city = request.args.get('city',type=str)
  observe, tips = weather.get_weather(province, city)
  return jsonify(observe, tips)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html',error=error), 404

@app.errorhandler(500)
def server_down(error):
  return render_template('500.html',error=error), 500

if __name__ == "__main__":
    app.run(debug=True)
