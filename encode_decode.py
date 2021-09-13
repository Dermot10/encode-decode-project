from tkinter import *
import base64

window = Tk()

window.geometry('500x300')
window.resizable(0, 0)
window.title("Dermot's Encryption Program")

Label(window, text='ENCODE DECODE', font='Times_New_Roman 20 bold ').pack()
Label(window, text='Dermot', font='Times_New_Roman 20 bold').pack(side=BOTTOM)


Text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

# function to encode


def encode(key, message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# function to decode
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


# function to set mode
def mode():
    if(mode.get() == 'e'):
        result.set(encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        result.set(decode(private_key.get(), Text.get()))
    else:
        result.set('Invalid Mode')

# Function to exit the window


def exit():
    window.destroy()

# Function to reset window


def reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    result.set("")


window.mainloop()
