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


SCALE = 0.7
if __name__ == "__main__":
    window = Tk()

    window.geometry(f"{int(SCALE*600)}x{int(SCALE*700)}")
    window.title("8-puzzle agent")
    window.config(background="#404258")
    window.resizable(False,False)


    # label = Label(window,image=myimage)
    # label.bind("<Button-1>",drag_start)
    # label.bind("<B1-Motion>",drag_motion)
    # label.place(x=0,y=0)
    # label2 = Label(window,image=myimage)
    # label2.bind("<Button-1>",drag_start)
    # label2.bind("<B1-Motion>",drag_motion)
    # label2.place(x=200,y=200)
    
    canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background="#50577A")
    canvas.create_line(200*SCALE,0,200*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(400*SCALE,0,400*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(0,200*SCALE,600*SCALE,200*SCALE,width=5*SCALE)
    canvas.create_line(0,400*SCALE,600*SCALE,400*SCALE,width=5*SCALE)
    canvas.pack()


    startState = puzzle.PuzzleState([
            [None,   1    ,2],
            [3,      4    ,5],
            [6,      7    ,8]])

    # ________________________________________puzzle sequence
    outPutSequence = startState.matrix

    for i in range(3):
        for j in range(3):
            if outPutSequence[i][j] is not None:
                outPutSequence[i][j] = Label(window,text=f' {outPutSequence[i][j]} ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
                outPutSequence[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
                outPutSequence[i][j].bind("<Button-1>",drag_start)
                outPutSequence[i][j].bind("<B1-Motion>",drag_motion)

    arrowRightLabel= Label(window,text="to go 1 step forward press -> key",font=('Arial',14),foreground='#D6E4E5',background="#404258")
    arrowRightLabel.place(x=20,y=(600+5)*SCALE)
    arrowLeftLabel= Label(window,text="to go 1 step back press <- key",font=('Arial',14),foreground='#D6E4E5',background="#404258")
    arrowLeftLabel.place(x=20,y=(600+45)*SCALE)
    window.mainloop()