from tkinter import *
import main
root=Tk()
def retrieve_input():
    output = main.moy(root.clipboard_get())
    outBox.config(state=NORMAL)
    outBox.delete("1.0","end")
    for x in output:
        outBox.insert(END, f"{39*'-'}\n{x} : {output[x]}\n")
    outBox.config(state=DISABLED)

def clear():
    outBox.config(state=NORMAL)
    outBox.delete("1.0","end")
    outBox.config(state=DISABLED)

root.title("laviescolaire moyenne")
upFrame = Frame(root)
downFrame= Frame(root)
textBox=Text(root,width=50,height=10)
outBox=Text(root,state=DISABLED)
clearButton=Button(root, text="Clear", command=clear)
buttonCommit=Button(root, text="Commit", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
clearButton.pack()
outBox.pack()

mainloop()
