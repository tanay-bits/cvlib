from Tkinter import *
import os

root = Tk(className = 'face_recognition_gui')
svalue = StringVar() # defines the widget state as string

w = Entry(root,textvariable=svalue) # adds a textarea widget
w.pack()


def train_btn_load():
    name = svalue.get()
    os.system('python face_train_eigen.py %s'%name)

def recog_btn_load():
    os.system('python face_recog_eigen.py')

train_btn = Button(root,text="Train EigenFaces", command=train_btn_load)
train_btn.pack()

recog_btn = Button(root,text="Recognize", command=recog_btn_load)
recog_btn.pack()

root.mainloop()