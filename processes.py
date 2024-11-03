from my_enums import Cell,Ball,Keys
from logic import Logic 
from draw_cells import DrawCells
from init_states_of_cells import InitStatesOfCells

class Processes:
    def getTargetCells(self,list):
        targetList=[]
        for i in range(list.shape[0]):
            for j in range(list.shape[1]):
                if(list[i][j][Keys.cell.value] == Cell.target.value): 
                    targetList.append({Keys.row.value: i ,Keys.column.value: j})
        return targetList

    def isFinalState(self,list,targetList):
        for i in range(len(targetList)):
            row =targetList[i][Keys.row.value]
            column =targetList[i][Keys.column.value]
            if(list[row][column][Keys.ball.value] == Ball.none.value): return False
        return True
    
    def previousCellValidator(self,list,row,column):
        logic= Logic()
        if(logic.isInsideList(list,row,column)):
            if(list[row][column][Keys.ball.value] == Ball.none.value): 
                print("it is not a ball")
                return False
            elif(list[row][column][Keys.ball.value] == Ball.grey.value): 
                print("you can't move this ball")
                return False
            else:
                return True
        else: 
            print("the position is out of board")
            return False
        
    def newCellValidator(self,list,row,column):
        logic= Logic()
        if(logic.isInsideList(list,row,column)):
            if(list[row][column][Keys.ball.value] == Ball.none.value): 
                return True
            else:
                print("this cell already has a ball")
                return False
        else: 
            print("the position is out of board")
            return False

    def run(self):
        logic= Logic()
        draw= DrawCells()
        init = InitStatesOfCells()
        for i in range(len(init.states)):
            print(f"{i} : ")
            draw.printBoard(init.selectState(i))
        print("select index of board you want : ")
        list = init.selectState(int(input()))
        targetList = self.getTargetCells(list)
        while(True):
            print("")
            draw.printBoard(list)
            if(self.isFinalState(list,targetList)): break
            print("previous cell")
            print("row : ")
            preRow = int(input())
            print("column : ")
            preColumn = int(input())
            if(self.previousCellValidator(list,preRow,preColumn)):
                print("new cell")
                print("row : ")
                newRow = int(input())
                print("column : ")
                newColumn = int(input())
                if(self.newCellValidator(list,newRow,newColumn)):
                    list[newRow][newColumn][Keys.ball.value] = list[preRow][preColumn][Keys.ball.value]
                    list[preRow][preColumn][Keys.ball.value] = Ball.none.value
                    if(list[newRow][newColumn][Keys.ball.value] == Ball.purpule.value):
                        logic.purpuleBallEffect(list,newRow,newColumn)
                    else:
                        logic.redBallEffect(list,newRow,newColumn)
        print("done ....")
    