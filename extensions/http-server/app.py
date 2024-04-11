from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is the index page.'

@app.route('/custom_endpoint', methods=['POST'])
def custom_endpoint():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        app.logger.info(f'Cuerpo de la solicitud: \n{data}')

        return 'Solicitud recibida correctamente. \n' + data
    else:
        return 'Error: Se esperaba una solicitud POST.', 400


@app.route('/home', methods=['GET'])
def home():
    app.logger.info(f'Hello, World! This is the index page.')
    return 'Hello, World! This is the index page.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
