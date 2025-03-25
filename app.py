from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)

# Función que realiza el procesamiento en segundo plano
def proceso_largo():
    print("Iniciando procesamiento largo...")
    # Simula un procesamiento que tarda 10 segundos
    time.sleep(10)
    print("Procesamiento largo completado.")

@app.route('/iniciar', methods=['GET'])
def iniciar():
    # Responde inmediatamente con un mensaje
    response = jsonify({"message": "La solicitud fue recibida, el procesamiento está en curso."})
    response.status_code = 200

    # Ejecuta el procesamiento en segundo plano sin bloquear la respuesta
    threading.Thread(target=proceso_largo).start()
    
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
