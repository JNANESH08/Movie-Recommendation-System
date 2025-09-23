from flask import Flask, render_template, request
from modal import Modal
from rapid_api import MovieDatabase

recommender_obj = Modal()
app = Flask(__name__)
# app.config['SECRET_KEY'] = ''


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/recomend', methods=['GET', 'POST'])
def recomend():
    recomended_movies = None
    if request.method == 'POST':
        movie = request.form['movie']
        try:
            recomended_movies = recommender_obj.get_recommendations(movie).head(8)
        except Exception:
            return render_template('errors/500.html')
        recomended_movies = MovieDatabase(recomended_movies).perform()
        print(recomended_movies)
    return render_template("recommendation.html", recomended_movies = recomended_movies)
@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    return render_template("sign_in.html")
@app.route('/main', methods=['GET','POST'])
def main():
    return render_template("main1.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port="5300")