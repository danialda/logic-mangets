from my_enums import Keys,Ball,Cell
class DrawCells: 
    def printBoard(self,list):
        for i in range(list.shape[0]):
            row_items = []
            for j in range(list.shape[1]):
                if(list[i][j][Keys.ball.value] != Ball.none.value and list[i][j][Keys.cell.value] == Cell.target.value):
                    row_items.append(list[i][j][Keys.ball.value] + "_")  
                elif(list[i][j][Keys.ball.value] != Ball.none.value):
                    row_items.append(list[i][j][Keys.ball.value])  
                else:
                    row_items.append(list[i][j][Keys.cell.value])  
            print(row_items)
            