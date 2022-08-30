#imports
import tkinter as tk
import random
import time

#variables 
window = tk.Tk()
window.title("Hello wold")
window.geometry("300x100")

#functions
def joke():
  lol = random.randrange(1,6)
  if joke == 1:
    print("why is dark spelled with a k instead of a c")
    time.sleep(2)
    print("because you can't see in the dark")
  elif lol == 2:
    print("why was 6 afraid of 7")
    time.sleep(2)
    print("because 7 8 9")
  elif lol == 3:
    print("what do they call bigfoot in england")
    time.sleep(2)
    print("big meter")
  elif lol == 4:
    print("do they allow loud laughing in hawaii")
    time.sleep(2)
    print("or just a-lo-ha")
  elif lol == 5:
    print("I know a bunch of good jokes about umbrellas")
    time.sleep(2)
    print("but they usally go over people's head")
  print(" ")


#code
hello = tk.Label(text="Dad joke generator")
hello.pack()
warning = tk.Label(text="(May not Be Original Jokes)")
warning.pack()
button = tk.Button(window, text="Click me!", command=joke)
button.pack()

tk.mainloop()
