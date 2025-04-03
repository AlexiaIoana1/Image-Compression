import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image, ImageTk

def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        # re-sizing the app window in order to fit picture and buttom
        app.geometry("560x300")

        label.pack_forget()

        label1 = tk.Label(app, text="Now,choose one compression technique!")
        label1.pack(pady=10)

        image_label = tk.Label(app,image=pic)
        image_label.image = pic
        image_label.pack(pady=5)

    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")


def compressionDTC():
    pass

def compressionDWT():
    pass

def compressionIWT():
    pass

# Main method
if __name__ == "__main__":

    # defining tkinter object
    app = tk.Tk()

    # setting title and basic size to our App
    app.title("Image Compressor")
    app.geometry("560x270")

    # adding background color to our upload button
    app.option_add("*Button*Background", "lightgreen")

    label = tk.Label(app, text="Please upload an image!")
    label.pack(pady=10)

    # defining our upload buttom
    uploadButton = tk.Button(app, text="Upload", command=imageUploader)
    uploadButton.place(x=10, y=10)

    DCTButton = tk.Button(app, text="DCT", command=compressionDTC)
    DCTButton.place(x=10, y=40)

    DWTButton = tk.Button(app, text="DWT", command=compressionDWT())
    DWTButton.place(x=10, y=70)

    IWTButton = tk.Button(app, text="IWT", command=imageUploader)
    IWTButton.place(x=10, y=100)

    app.mainloop()


