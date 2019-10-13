import os

from flask import Flask, request, jsonify

from static.code.identify_face_image import identify_face

app = Flask(__name__)
algo = identify_face('')


@app.route("/upload", methods=['POST'])
def upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            last_file = os.path.join('static', 'images', photo.filename)
            location = os.path.join('static', 'images', photo.filename)
            photo.save(last_file)
            algo.img_path = location
            mensaje = algo.identify
            if mensaje.get('proba') > 0.5:
                return jsonify(mensaje), 200
            else:
                return jsonify(mensaje), 403
        return jsonify({'error': 'no photo provided'}), 400
    return jsonify({'error': 'no image provided'}), 400


if __name__ == '__main__':
    app.run(debug=True)
