# STEP 1 : Import libraries

from PIL import Images, ImageTk
import tkinter



#STEP 2 : Create Interface of the Dice Rolling Simulation

root = tkinter.Tk()
root.geometry('450x450')
root.title('Roll the Dice')
root.configure(bg='#B9C6C9')


#STEP 3 : 
    #1 Adding Label to our window 

l0 = tkinter.Label(root, text="")
l0.pack()

    #2 Adding labels with Different font and formatting
l1 = tkinter.Label(root, text="Hello There...", 
                   fg='black', bg= '#B9C6C9',
                   font="Helvetica 20 bold italic", border=5)
l1.pack()



#STEP 4 : Inserting the images 

dice = ['Dice1.jpg,'Dice2.jpg','Dice3.jpg','Dice4.jpg','Dice5.jpg','Dice6.jpg']

#Simulating the dice with random 1 to 6 

image2 = ImageTk.PhotoImage(file= 'dice.jpg')

label1 = tkinter.Label(root, image=image2)
label1.image = image2


#Packing widget with Parent widget
label1.pack(expand=True)







root.mainloop()