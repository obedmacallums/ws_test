# Se necesita instalar el paquete websocket-client
# pip install websocket-client


# importamos el paquete websocket-client
import websocket

def on_message(ws, message):
    print("Mensaje recibido:", message)

def on_error(ws, error):
    # Ha ocurrido un error durante la conexión
    if isinstance(error, KeyboardInterrupt):
        print('Cancelado por teclado')
    print('error: ', error)

def on_close(ws, close_status_code, close_msg):
    print("Conexión WebSocket cerrada")

def on_open(ws):
    print("Conexión WebSocket abierta")

if __name__ == "__main__":
    # URL del servidor WebSocket (cambiar solo la ip privada del dispositivo)
    websocket_url = "ws://192.168.0.113:9635"

    # Crea una instancia de WebSocketApp y establece los callbacks
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    # Inicia el cliente WebSocket
    ws.run_forever()