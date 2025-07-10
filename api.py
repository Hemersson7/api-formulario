from flask import Flask, request, jsonify

app = Flask(__name__)

CAMPOS = [
    "nombre",
    "apellido",
    "fecha_nacimiento",
    "telefono",
    "rut",
    "correo",
    "fecha_contratacion"
]

@app.route("/guardar", methods=["POST"])
def guardar_datos():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "mensaje": "No se recibió JSON"}), 400

    faltantes = [campo for campo in CAMPOS if campo not in data]
    if faltantes:
        return jsonify({"status": "error", "mensaje": f"Faltan campos: {', '.join(faltantes)}"}), 400

    print("Datos recibidos:", data)
    return jsonify({"status": "ok", "mensaje": "Datos recibidos correctamente"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
