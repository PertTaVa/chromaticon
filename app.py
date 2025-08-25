from flask import Flask, render_template, request, jsonify
from modules.analyzer import analyze_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = analyze_text(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)