# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *
import puzzle
import aStar

SCALE = 0.7
window = Tk()

labels = [[None]*3]*3

solutionPath = []
solutionIndex = 0

hLabel = Label(window,text="00",font=('Arial',11),foreground='#D6E4E5',background="#404258")
hl = Label(window,text="heuristic=",font=('Arial',11),foreground='#D6E4E5',background="#404258")
levelLabel = Label(window,text="00",font=('Arial',11),foreground='#D6E4E5',background="#404258")
ll = Label(window,text="level=",font=('Arial',11),foreground='#D6E4E5',background="#404258")

hl.place(x=400*SCALE,y=(600+5)*SCALE)
ll.place(x=400*SCALE,y=(600+45)*SCALE)
hLabel.place(x=500*SCALE,y=(600+5)*SCALE)
levelLabel.place(x=500*SCALE,y=(600+45)*SCALE)

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




def goBack(event):
    global solutionIndex
    if solutionIndex < solutionPath.__len__()-1:
        solutionIndex += 1
        print("back")
        ShowPuzzle(solutionPath[solutionIndex])
    

def goForward(event):
    global solutionIndex
    if solutionIndex > 0:
        solutionIndex -= 1
        ShowPuzzle(solutionPath[solutionIndex])
        print("forward")

def printKeys(event):
    print(event.keysym+" key pressed")

def terminate(event):
    exit()

def ShowPuzzle(outputState):
    global hLabel
    global levelLabel
    for i in range(3):
            for j in range(3):
                if outputState.matrix[i][j] is None:
                    labels[i][j] = Label(window,text=f'   ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
                    labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
                    continue
                labels[i][j] = Label(window,text=f' {outputState.matrix[i][j]} ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
                labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
                # labels[i][j].bind("<Button-1>",drag_start)
                # labels[i][j].bind("<B1-Motion>",drag_motion)
    
    hLabel.config(text=f"{outputState.heuristic}")
    levelLabel.config(text=f"{outputState.level}")


def drawGrid():
    window.geometry(f"{int(SCALE*600)}x{int(SCALE*700)}")
    window.title("8-puzzle agent")
    window.config(background="#404258")
    window.resizable(False,False)
    
    canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background="#50577A")
    canvas.create_line(200*SCALE,0,200*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(400*SCALE,0,400*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(0,200*SCALE,600*SCALE,200*SCALE,width=5*SCALE)
    canvas.create_line(0,400*SCALE,600*SCALE,400*SCALE,width=5*SCALE)
    canvas.pack()


if __name__ == "__main__":

    
    drawGrid()

    startState=puzzle.PuzzleState([
        [1,      4          ,2],
        [6,      5          ,8],
        [7,      3          ,None]])

    
    targetState=puzzle.PuzzleState([
        [None,   1    ,2],
        [3,      4    ,5],
        [6,      7    ,8]])
    
    solutionTree = aStar.Tree(startState,targetState)
    solution = solutionTree.aStarTraverse()
    
    while solution is not None:
        solutionPath.append(solution)
        solution=solution.parent
    
    solutionIndex=solutionPath.__len__()-1
    ShowPuzzle(startState)
    

    arrowRightLabel= Label(window,text="to go 1 step forward press -> key",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    arrowRightLabel.place(x=20,y=(600+5)*SCALE)
    arrowLeftLabel= Label(window,text="to go 1 step back press <- key",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    arrowLeftLabel.place(x=20,y=(600+45)*SCALE)
    
    window.bind("<Left>",goBack)
    window.bind("<Right>",goForward)
    window.bind("<Escape>",terminate)
    window.bind("<Key>",printKeys)
    window.mainloop()