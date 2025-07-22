import socket
import keyboard

HOST = ''
PORT = 9999

def handle_command(data: bytes):
    if data == b'forward_down':
        print("→ Holding ‘W’ down")
        keyboard.press('w')
    elif data == b'forward_up':
        print("← Releasing ‘W’")
        keyboard.release('w')

    elif data == b'left_down':
        print("→ Holding ‘A’ down")
        keyboard.press('a')
    elif data == b'left_up':
        print("← Releasing ‘A’")
        keyboard.release('a')

    elif data == b'down_down':
        print("→ Holding ‘S’ down")
        keyboard.press('s')
    elif data == b'down_up':
        print("← Releasing ‘S’")
        keyboard.release('s')

    elif data == b'right_down':
        print("→ Holding ‘D’ down")
        keyboard.press('d')
    elif data == b'right_up':
        print("← Releasing ‘D’")
        keyboard.release('d')

    elif data == b'space_down':
        print("→ Holding ‘SPACE’ down")
        keyboard.press('space')
    elif data == b'space_up':
        print("← Releasing ‘SPACE’")
        keyboard.release('space')

    else:
        print(f"⚠️ Unknown command: {data!r}")

def main():
    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Listening on port {PORT} for button events…")
        while True:
            conn, _ = s.accept()
            with conn:
                data = conn.recv(32)
                handle_command(data)

if __name__ == "__main__":
    main()