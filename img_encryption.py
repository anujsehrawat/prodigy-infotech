from tkinter import Tk, Button, Text, END
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('JPG file', '*.jpg')])
    if file1 is not None:
        # Get file name
        file_name = file1.name
        
        # Get the key from the entry box, and strip any extra spaces or newlines
        key_str = entry1.get(1.0, END).strip()
        
        # Ensure the key is an integer, handle any exceptions
        try:
            key = int(key_str)
        except ValueError:
            print("Please enter a valid integer key.")
            return
        
        print("Selected file:", file_name)
        print("Entered key:", key)

        # Read the image file in binary mode
        with open(file_name, 'rb') as fi:
            image = fi.read()

        # Encrypt the image using XOR
        image = bytearray(image) 
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Write the encrypted image back to the file
        with open(file_name, 'wb') as fi1:
            fi1.write(image)

        print("Image encryption completed.")

b1 = Button(root, text="Encrypt/Decrypt", command=encrypt_image)
b1.place(x=50, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=55, y=50)

root.mainloop()
