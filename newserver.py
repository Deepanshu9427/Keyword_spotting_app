import random
from flask import Flask, request,render_template
from service import Keyword_Spotting_Service
import os

# instantiate flask app
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
	"""Endpoint to predict keyword

    :return (json): This endpoint returns a json file with the following format:
        {
            "keyword": "down"
        }
	"""
	predicted_keyword = None
	if request.method == 'POST':
		audio_file = request.files['audio']
		file_name = str(random.randint(0, 100000))
		audio_file.save(file_name)

		#audio = AudioSegment.from_ogg(temp_audio_path)
		# instantiate keyword spotting service singleton and get prediction
		kss = Keyword_Spotting_Service()
		predicted_keyword = kss.predict(file_name)

		# we don't need the audio file any more - let's delete it!
		os.remove(file_name)
	return render_template('index.html',predicted_keyword=predicted_keyword)


if __name__ == "__main__":
    app.run(debug=True)