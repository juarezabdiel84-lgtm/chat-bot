from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '')
    bot_msg = f"Dijiste: {user_msg}. Ya quedó en Render bro 👌"
    return jsonify({'response': bot_msg})  # ← CLAVE: dice 'response'

if __name__ == '__main__':
    app.run(debug=True)
