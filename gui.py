# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *
import puzzle



def drag_start(event):
    widget = event.widget
    widget.startX=event.x
    widget.startY=event.y
    widget.place(x=widget.winfo_x())
    

def drag_motion(event):
    widget = event.widget
    x=widget.winfo_x() - widget.startX + event.x
    y=widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


window = Tk()

window.geometry("600x600")
window.title("8-puzzle agent")
window.config(background="#687a7d")
window.resizable(False,False)


# label = Label(window,image=myimage)
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
# label.place(x=0,y=0)
# label2 = Label(window,image=myimage)
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
# label2.place(x=200,y=200)

canvas = Canvas(window,height=600,width=600,background="#687a7d")
canvas.create_line(200,0,200,600,width=5)
canvas.create_line(400,0,400,600,width=5)
canvas.create_line(0,200,600,200,width=5)
canvas.create_line(0,400,600,400,width=5)
canvas.pack()


startState = puzzle.PuzzleState([[3,2,1],[6,5,4],[8,7,None]])

# ________________________________________puzzle sequence
outPutSequence = startState.matrix

for i in range(3):
    for j in range(3):
        if outPutSequence[i][j] is not None:
            outPutSequence[i][j] = Label(window,text=f' {outPutSequence[i][j]} ',font=('Arial',120),foreground='black',background="#687a7d")
            outPutSequence[i][j].place(x=5+200*j,y=5+200*i)
            outPutSequence[i][j].bind("<Button-1>",drag_start)
            outPutSequence[i][j].bind("<B1-Motion>",drag_motion)

window.mainloop()