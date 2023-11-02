# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *
import puzzle
import aStar
import solvable
import FinalBFS
import dfs
import time


SCALE = 0.7
window = Tk()

labels = [[None]*3]*3

solutionPath = []
solutionIndex = 0

algorithm = -1

tileIndex = 0

entrySet = set()

targetState=puzzle.PuzzleState([
        [None,   1    ,2],
        [3,      4    ,5],
        [6,      7    ,8]])


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
                if outputState.matrix[i][j] is None or outputState.matrix[i][j] == 0:
                    labels[i][j] = Label(window,text=f'   ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
                    labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
                    continue
                labels[i][j] = Label(window,text=f' {outputState.matrix[i][j]} ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
                labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
                # labels[i][j].bind("<Button-1>",drag_start)
                # labels[i][j].bind("<B1-Motion>",drag_motion)
    if isinstance(outputState,puzzle.PuzzleState):
        hLabel.config(text=f"{outputState.heuristic}")
    else:
        hLabel.config(text="no h for this algorithm")
    levelLabel.config(text=f"{outputState.level}")


def drawGrid():
    window.geometry(f"{int(SCALE*900)}x{int(SCALE*700)}")
    window.title("8-puzzle agent")
    window.config(background="#404258")
    window.resizable(False,False)
    
    canvas = Canvas(window,height=600*SCALE,width=600*SCALE,background="#50577A")
    canvas.create_line(200*SCALE,0,200*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(400*SCALE,0,400*SCALE,600*SCALE,width=5*SCALE)
    canvas.create_line(0,200*SCALE,600*SCALE,200*SCALE,width=5*SCALE)
    canvas.create_line(0,400*SCALE,600*SCALE,400*SCALE,width=5*SCALE)
    canvas.place(x=0,y=0)

def bfsSelector():
    global algorithm
    algorithm = 0
    print(algorithm)

def dfsSelector():
    global algorithm
    algorithm = 1
    print(algorithm)

def a_euclidian():
    global algorithm
    algorithm = 2
    print(algorithm)

def a_manhattan():
    global algorithm
    algorithm = 3
    print(algorithm)

def buildTile(num):
    
    global tileIndex,entrySet,startState
    if tileIndex < 9 :
        if num not in entrySet:
            entrySet.add(num)
            i=tileIndex//3
            j=tileIndex%3

            if num is not None:
                startState.matrix[i][j] = int(num)
            else:
                startState.matrix[i][j] = None
            ShowPuzzle(startState)
            tileIndex += 1
        else:
            print("number entered before")
    if entrySet.__len__()==9:
        startButton = Button(window,foreground='#D6E4E5',background="#50577A",text='start',command=startSolve,font=('arial',18))
        startButton.place(x=SCALE*700,y=SCALE*(300))
        
        
# =================___edit here___================= 
def startSolve():
    global startState,targetState,algorithm,solutionIndex,solution,solutionPath
    print(startState)
    print('checking wether its solvable or not ...')
    if not solvable.isSolvable(startState.matrix):
        print("this puzzle can't be solved because number of inversions is odd")
        return
    
    print('puzzle is solvable')
    print('solving the puzzle ...')
    print(f'algorithm = {algorithm}')
    # bfs
    if algorithm == 0:
        initial = startState.matrix
        final = targetState.matrix
        solution = FinalBFS.solve_BFS(initial, FinalBFS.findZero(initial), final)
    # dfs
    elif algorithm == 1:

        mat = startState.matrix
        for i in range(3):
            for j in range(3):
                if mat[i][j] == None:
                    mat[i][j] = 0

        initial_state = dfs.State(mat)
        start = time.time()

        solution = dfs.dfs_search(initial_state)
        end = time.time()
        print("The time of execution of DFS :",
            (end - start) * 10 ** 3, "ms")
    # euclidean a*
    elif algorithm == 2:
        solutionTree = aStar.Tree(startState,targetState)
        solution = solutionTree.aStarTraverse('E')
    # manhattan a*
    elif algorithm == 3:
        solutionTree = aStar.Tree(startState,targetState)
        solution = solutionTree.aStarTraverse('M')
        
    else:
        print('choose the algorithm')
        return
    print('puzzle solved successfully')
    while solution is not None:
        solutionPath.append(solution)
        solution=solution.parent
    
    solutionIndex=solutionPath.__len__()-1
        # ShowPuzzle(startState)
        

def keyPressed(event):
    print(event.keysym)
    num = event.keysym
    arr = ["1","2","3","4","5","6","7","8","space","0"]

    if num in arr:
        if event.keysym == "space" or event.keysym == "0":
            num = None
        print("available key")
        buildTile(num)

def buildRadioButtons():
    #  radio buttons

    v = StringVar(window, "1") 
    
    # values = {"BFS" : "1", 
    #         "DFS" : "2", 
    #         "A* EUCLIDIAN" : "3", 
    #         "A* MANHATTAN" : "4",} 
    
    Radiobutton(window, text = "BFS", variable = v, 
        value = "1", font=('arial',11),foreground='#D6E4E5',background="#404258",command=bfsSelector).place(x=SCALE*620,y=SCALE*(50),) 
    Radiobutton(window, text = "DFS", variable = v, 
        value = "2", font=('arial',11),foreground='#D6E4E5',background="#404258",command=dfsSelector).place(x=SCALE*620,y=SCALE*(100),) 
    Radiobutton(window, text = "A* EUCLIDIAN", variable = v, 
        value = "3", font=('arial',11),foreground='#D6E4E5',background="#404258",command=a_euclidian).place(x=SCALE*620,y=SCALE*(150),) 
    Radiobutton(window, text = "A* MANHATTAN", variable = v, 
        value = "4", font=('arial',11),foreground='#D6E4E5',background="#404258",command=a_manhattan).place(x=SCALE*620,y=SCALE*(200),) 
       
if __name__ == "__main__":

    startState=puzzle.PuzzleState([
        [None,   None    ,None],
        [None,   None    ,None],
        [None,   None    ,None]])
    
    buildRadioButtons()
    
    drawGrid()

    
    

    arrowRightLabel= Label(window,text="to go 1 step forward press -> key",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    arrowRightLabel.place(x=20,y=(600+5)*SCALE)
    arrowLeftLabel= Label(window,text="to go 1 step back press <- key",font=('Arial',11),foreground='#D6E4E5',background="#404258")
    arrowLeftLabel.place(x=20,y=(600+45)*SCALE)
    
    window.bind("<Left>",goBack)
    window.bind("<Right>",goForward)
    window.bind("<Escape>",terminate)
    # window.bind("<Key>",printKeys)


    # keys to input the puzzle to be solved
    window.bind("<Key>",keyPressed)
    
    window.mainloop()