from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from spleeter.separator import Separator
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'mp3', 'mp4', 'aiff', 'aif', 'aifc', 'caf', 'amr', '3gp', '3g2', 'aac', 'ac3', 'flv', 'mka', 'm4v', 'mov', 'mpg', 'mpeg', 'ts', 'm2ts', 'avi', 'mkv', 'vob', 'asf', 'wmv', 'mxf', 'ogv', 'rm', 'mp2', 'mp1', 'm1v', 'm2v', 'm2a', 'm4b', 'm4p', 'm4r', '3ga', 'aa', 'aax', 'act', 'au', 'awb', 'dct', 'dss', 'dvf', 'gsm', 'ivs', 'mmf', 'mpc', 'msv', 'nmf', 'nsf', 'ogg', 'opus', 'ra', 'raw', 'sln', 'tta', 'vox', 'wma', 'wv', 'webm', '8svx', 'cda'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return jsonify({
        'greeting': 'welcome to the audio processing API',
        'author': '@edvanioFC',
        'usage': 'send a POST request to /api/process with an audio file',
        'response': 'returns a JSON object with the path to the processed audio files',
        'voice': 'path to the voice audio file',
        'instruments': 'path to the instruments audio file',
        'download': 'download the processed audio files',
        'error': 'error message if something goes wrong',
        'status': 'HTTP status code',
        'message': 'HTTP status message',
        'additional info': '@articlespleeter2020',
        'doi' : '10.21105/joss.02154',
        'url' : 'https://doi.org/10.21105/joss.02154',
        'year' : '2020',
        'publisher' : 'The Open Journal',
        'volume' : '5',
        'number' : '50',
        'pages' : '2154',
        'authors' : 'Romain Hennequin and Anis Khlif and Felix Voituret and Manuel Moussallam',
        'title' : 'Spleeter: a fast and efficient music source separation tool with pre-trained models',
        'journal' : 'Journal of Open Source Software',
        'note' : 'Deezer Research'
    })

@app.route('/api/process', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())
        unique_filename1 = f"{unique_id}_{filename}"
        unique_filename = f"{unique_id}_{os.path.splitext(filename)[0]}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename1)
        file.save(file_path)

        # Usar Spleeter para separar o áudio
        separator = Separator('spleeter:2stems')
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], unique_id)
        os.makedirs(output_path, exist_ok=True)
        separator.separate_to_file(file_path, output_path)

        '''# Caminhos para os arquivos processados
        vocals_filename = os.path.join(output_path, 'vocals.wav')
        accompaniment_filename = os.path.join(output_path, 'accompaniment.wav')

        # acessar os arquivos dentro do diretório unique_id/unique_id_unique_filename/vocal.wav...
        vocals_output_path = os.path.join(unique_filename, 'vocals.wav')
        accompaniment_output_path = os.path.join(unique_filename, 'accompaniment.wav')
        os.makedirs(os.path.join(output_path, unique_filename), exist_ok=True)'''
                
        print('Unicoooo:', unique_filename)

        return jsonify({
            'voice': f'/api/stream/{unique_id}/{unique_filename}/vocals.wav',
            'instruments': f'/api/stream/{unique_id}/{unique_filename}/accompaniment.wav',
            'voice_download': f'/api/download/{unique_id}/{unique_filename}/vocals.wav',
            'instruments_download': f'/api/download/{unique_id}/{unique_filename}/accompaniment.wav'
        })

    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/stream/<unique_id>/<path:filename>')
def stream_file(unique_id, filename):
    directory = os.path.join(app.config['OUTPUT_FOLDER'], unique_id)
    file_path = os.path.join(directory, filename)
    if not os.path.isfile(file_path):
        return jsonify({'error': 'Ficheiro não encontrado'}), 404
    
    def generate():
        with open(file_path, 'rb') as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)
    return Response(generate(), mimetype="audio/wav"), 200

@app.route('/api/download/<unique_id>/<path:filename>')
def download_file(unique_id, filename):
    directory = os.path.join(app.config['OUTPUT_FOLDER'], unique_id)
    file_path = os.path.join(directory, filename)
    if not os.path.isfile(file_path):
        return jsonify({'error': 'Ficheiro não encontrado'}), 404
    return send_file(file_path, as_attachment=True), 200


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True, port=5009, host='localhost')
