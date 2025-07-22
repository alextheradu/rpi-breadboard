from gpiozero import Button
import socket, signal

HOST = 'your pc ip'
PORT = 9999

button = Button(26, pull_up=True)

def send(msg: bytes):
    try:
        with socket.socket() as s:
            s.settimeout(1.0)
            s.connect((HOST, PORT))
            s.sendall(msg)
    except Exception as e:
        print(f"✖ Error sending {msg!r}: {e}")

def on_press():
    print("Button down")
    send(b'forward_down')

def on_release():
    print("Button up")
    send(b'forward_up')

button.when_pressed  = on_press
button.when_released = on_release

button2 = Button(16, pull_up=True)

def on_press2():
    """Function called when second button is pressed"""
    print("Second button down")
    send(b'left_down')

def on_release2():
    """Function called when second button is released"""
    print("Second button up")
    send(b'left_up')

button2.when_pressed  = on_press2
button2.when_released = on_release2

button3 = Button(13, pull_up=True)

def on_press3():
    """Function called when third button is pressed"""
    print("Down button pressed")
    send(b'down_down')

def on_release3():
    """Function called when third button is released"""
    print("Down button released")
    send(b'down_up')

button3.when_pressed = on_press3
button3.when_released = on_release3

# Set up fourth button on GPIO 6 for 'right'
button4 = Button(6, pull_up=True)

def on_press4():
    """Function called when fourth button is pressed"""
    print("Right button pressed")
    send(b'right_down')

def on_release4():
    """Function called when fourth button is released"""
    print("Right button released")
    send(b'right_up')

button4.when_pressed  = on_press4
button4.when_released = on_release4

button5 = Button(14, pull_up=True)

def on_press5():
    """Function called when fifth button is pressed"""
    print("Space button pressed")
    send(b'space_down')

def on_release5():
    """Function called when fifth button is released"""
    print("Space button released")
    send(b'space_up')

button5.when_pressed  = on_press5
button5.when_released = on_release5

print("Ready — hold the button on GPIO 26 to move forward, GPIO 16 to move left, GPIO 13 to move down, GPIO 6 to move right, GPIO 19 for SPACE")
signal.pause()
