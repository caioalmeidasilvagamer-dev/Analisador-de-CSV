from flask import Flask, render_template, request, jsonify
from analize import parseCsv, analisarLeads
import os
import math

app = Flask(__name__)

def limpar_nan(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return None
    if isinstance(obj, dict):
        return {k: limpar_nan(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [limpar_nan(i) for i in obj]
    return obj

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analisar", methods=["POST"])
def analisar():
    arquivo = request.files.get("csv")
    if not arquivo:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    os.makedirs("uploads", exist_ok=True)
    caminho = f"uploads/{arquivo.filename}"
    arquivo.save(caminho)

    leads = parseCsv(caminho)
    resultado = analisarLeads(leads)
    resultado = limpar_nan(resultado)

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)