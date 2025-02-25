from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    user_input = request.form.get('text', '')
    conversion_type = request.form.get('conversion_type', 'upper')

    if conversion_type == 'upper':
        converted_text = user_input.upper()
    elif conversion_type == 'lower':
        converted_text = user_input.lower()
    else:
        converted_text = user_input

    return jsonify(converted_text=converted_text)

if __name__ == '__main__':
    app.run(debug=True)
