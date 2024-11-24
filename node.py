from draw_cells import DrawCells
from my_enums import Cell,Keys,Ball
from logic import Logic
from copy import deepcopy
class Node:
    logic = Logic()
    draw = DrawCells()
    def __init__(self,board):
        self.parent=None   
        self.cost = 0
        self.board = deepcopy(board)
        self.heuristic=0
        self.__get_T_E_Cells_M_N_Balls()
    
    def __lt__(self, other):
        if(self.cost < other.cost):
            return self.cost 
        
    def __gt__(self, other):
        if(self.cost < other.cost):
            return other.cost 

    def copy(self): 
        node=Node(self.board)
        node.parent=self
        node.cost = deepcopy(self.cost) + 1
        return node

    def print(self):
        self.draw.printBoard(self.board)
    

    def isEnd(self):
        for cell in self.targetCells:
            if self.board[cell[Keys.row.value]][cell[Keys.column.value]][Keys.ball.value]==Ball.none.value:
                return False
            
        return True

    def isEqual(self,node):
        for item in self.magnetBalls:
            row = item[Keys.row.value]
            col = item[Keys.column.value]
            if not self.isCellEqual(self.board[row][col],node.board[row][col]):
                return False
        for item in self.normalBalls:
            row = item[Keys.row.value]
            col = item[Keys.column.value]
            if not self.isCellEqual(self.board[row][col],node.board[row][col]):
                return False
        return True
    
    def isCellEqual(self,cell1,cell2):
        return cell1[Keys.ball.value]==cell2[Keys.ball.value]

    def __get_T_E_Cells_M_N_Balls(self):
        self.hash=""
        list = deepcopy(self.board)
        self.targetCells=[]
        self.emptyCells=[]
        self.magnetBalls=[]
        self.normalBalls=[]
        for i in range(list.shape[0]):
            for j in range(list.shape[1]):
                self.hash += list[i][j][Keys.ball.value]
                if(list[i][j][Keys.cell.value] == Cell.target.value): 
                    self.targetCells.append({Keys.row.value: i ,Keys.column.value: j})
                if(list[i][j][Keys.ball.value] != Ball.none.value):
                    if(list[i][j][Keys.ball.value] == Ball.grey.value):
                        self.normalBalls.append({Keys.row.value: i ,Keys.column.value: j})
                    else:
                        self.magnetBalls.append({Keys.row.value: i ,Keys.column.value: j})
                else:
                    self.emptyCells.append({Keys.row.value: i ,Keys.column.value: j})
    

    def changePositionWithPurpule(self,magnetPosition):
        preRow = magnetPosition[Keys.row.value]
        preColumn = magnetPosition[Keys.column.value]
        for emptyCell in self.emptyCells:
            newBoard=deepcopy(self.board)
            newRow = emptyCell[Keys.row.value]
            newColumn = emptyCell[Keys.column.value]
            newBoard[newRow][newColumn][Keys.ball.value] = Ball.purpule.value
            newBoard[preRow][preColumn][Keys.ball.value] = Ball.none.value
            newBoard = self.logic.purpuleBallEffect(newBoard,newRow,newColumn)
            if(not self.isVisited(newBoard)):
                self.nextStates.append(Node(newBoard,self))

    def changePositionWithRed(self,magnetPosition):
        preRow = magnetPosition[Keys.row.value]
        preColumn = magnetPosition[Keys.column.value]
        for emptyCell in self.emptyCells:
            newBoard=deepcopy(self.board)
            newRow = emptyCell[Keys.row.value]
            newColumn = emptyCell[Keys.column.value]
            newBoard[newRow][newColumn][Keys.ball.value] = Ball.red.value
            newBoard[preRow][preColumn][Keys.ball.value] = Ball.none.value
            newBoard = self.logic.redBallEffect(newBoard,newRow,newColumn)
            if(not self.isVisited(newBoard)):
                self.nextStates.append(Node(newBoard,self))

    def checkMove(self,i,j):
        return self.board[i][j][Keys.ball.value] == Ball.none.value
    
    def move(self,oldPosition,i,j):
        row = oldPosition[Keys.row.value]
        col = oldPosition[Keys.column.value]
        self.board[i][j][Keys.ball.value] = self.board[row][col][Keys.ball.value]
        self.board[row][col][Keys.ball.value] = Ball.none.value
        if(self.board[i][j][Keys.ball.value] == Ball.purpule.value):
            self.board=self.logic.purpuleBallEffect(self.board,i,j)
        else:    
            self.board=self.logic.redBallEffect(self.board,i,j)
        self.__get_T_E_Cells_M_N_Balls()
        
    def getHeuristic(self):
        for targetCell in self.targetCells:
            row = targetCell[Keys.row.value]
            column = targetCell[Keys.column.value]
            if(self.board[row][column][Keys.ball.value] == Ball.none.value):
                self.heuristic += 1

    def nextNodes(self):
        nextNodesResult=[]
        for magnetBall in self.magnetBalls:
            for item in self.emptyCells:
                row = item[Keys.row.value]
                col = item[Keys.column.value]
                node =self.copy()
                node.move(magnetBall,row,col)
                nextNodesResult.append(node)
        return nextNodesResult
        
