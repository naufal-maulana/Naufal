import tkinter
import os

main_window = tkinter.Tk()


def event_tekan():
    labek = tkinter.Label(main_window, text="MANTAP")
    labek.pack()
    os.system("shutdown -l")


label = tkinter.Label(main_window, text="HALLO NAMA SAYA NAUFAL \n")
tombol = tkinter.Button(main_window, text="\n Klik", command=event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()
