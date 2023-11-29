import tkinter as tk
import initialization as init
from PIL import ImageTk, Image
import pygame

window = tk.Tk()
window.title('Endless Darkness')

window.geometry('1920x1080')

pygame.mixer.init()

frame = tk.Frame(window, width=1536, height=1170)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open('Images/monster_picture.jpg'))

label = tk.Label(frame, image=img)
label.pack()
pygame.mixer.music.load('Sounds/ambience_monster_alerted.mp3')
pygame.mixer.music.play(0)

window.mainloop()
