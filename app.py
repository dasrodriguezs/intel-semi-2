import os
from flask import Flask, request, render_template, url_for, redirect
from static.code.identify_face_image import identify_face

app = Flask(__name__)
algo = identify_face('')


# last_file = None


@app.route('/')
def home_page():
    return render_template('index.html', css_path=os.path.join('static', 'layout.css'))


@app.route('/index')
def index_page():
    return render_template('index.html', css_path=os.path.join('static', 'layout.css'))


@app.route("/upload", methods=['POST'])
def upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            last_file = os.path.join('static', 'images', photo.filename)
            location = os.path.join('static', 'images', photo.filename)
            photo.save(last_file)
            algo.img_path = location
            mensaje = algo.identify()
            last = os.path.join('static', 'images', str(photo.filename).replace('.', '') + 'last.jpg')
            print(last)
            print(mensaje)
            return render_template('index.html', image=last, css_path=os.path.join('static', 'layout.css'), mensaje=mensaje)
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
