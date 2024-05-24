from flask import Flask, render_template, url_for, request, redirect
from t2t import text_to_text
from t2i import text_to_image
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def text(): 
    if request.method == 'POST':
        prompt = request.form['message']

        print(prompt)
        response = text_to_text(prompt)
        return render_template('text.html', response=response, prompt=prompt)
    
    return render_template('text.html')


@app.route("/images", methods=['GET', 'POST']) 
def images():
    if request.method == 'POST':
        prompt = request.form['message']

        image_path = text_to_image(prompt)
        return render_template('images.html', path = image_path, prompt=prompt)
    
    return render_template('images.html')


@app.route("/sound") 
def sound():
    return render_template('sound.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080) # internal error
    app.run(debug = True) # Change this "True" to false in production enviornment