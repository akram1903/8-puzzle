# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX=event.x
    widget.startY=event.y
    widget.place(x=widget.winfo_x()+100)

# def drag_motion(event):
#     widget = event.widget
#     x=widget.winfo_x() - widget.startX + event.x
#     y=widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)


window = Tk()

window.geometry("500x500")
myimage= PhotoImage(file="ball.png")
label = Label(window,image=myimage,bg="red")
label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
label.place(x=0,y=0)
label2 = Label(window,image=myimage,bg="red")
label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
label2.place(x=200,y=200)
window.mainloop()