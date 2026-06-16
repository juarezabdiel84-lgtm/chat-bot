import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configurar Gemini con tu key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = ""
    if request.method == "POST":
        pregunta = request.form["pregunta"]
        try:
            response = model.generate_content(pregunta)
            respuesta = response.text
        except Exception as e:
            respuesta = f"Error con Gemini: {e}"
        return render_template("index.html", pregunta=pregunta, respuesta=respuesta)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
