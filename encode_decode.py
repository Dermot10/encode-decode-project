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
Result = StringVar()

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
def Mode():
    if(mode.get() == 'e'):
        Result.set(encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

# Function to exit the window


def Exit():
    window.destroy()

# Function to reset window


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# optimise controls for the window
# Message
Label(window, font='Times_New_Roman 12 bold ',
      text='MESSAGE').place(x=60, y=60)
Entry(window, font='Times_New_Roman 10 ', textvariable=Text,
      bg='ghost white') .place(x=290, y=60)

# Key
Label(window, font='Times_New_Roman 12 bold', text='Key').place(x=60, y=90)
Entry(window, font='Times_New_Roman 10 ', textvariable=private_key,
      bg='ghost white') .place(x=290, y=90)

# Encode/Decode Mode
Label(window, font='Times_New_Roman 12 bold',
      text='MODE (e-encode, d-decode)').place(x=60, y=120)
Entry(window, font='Times_New_Roman 10 ', textvariable=mode,
      bg='ghost white') .place(x=290, y=120)

# Results
Entry(window, font='Times_New_Roman 10 bold',
      textvariable=Result, bg='ghost white') .place(x=290, y=150)

# Buttons for the window's interface
Button(window, font='Times_New_Roman 10 bold', text='RESULT',
       padx=2, bg='LightGray', command=Mode).place(x=60, y=150)
Button(window, font='Times_New_Roman 10 bold', text='RESET', width=6,
       padx=2, command=Reset, bg='LimeGreen', ).place(x=80, y=190)
Button(window, font='Times_New_Roman 10 bold', text='EXIT', width=6,
       padx=2, command=Exit, bg='OrangeRed') .place(x=180, y=190)


window.mainloop()
