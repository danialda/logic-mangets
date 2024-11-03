from my_enums import Keys,Ball,Cell

class Logic:
    def hasBall(self,item):
        if(item[Keys.ball.value] != Ball.none.value): return True
        else: return False

    def isInsideList(self,list,row,column):
        if((row >= 0 and row < list.shape[0]) and (column >= 0 and column < list.shape[1])): return True
        else: return False

    def __pushUp(self,list,row,column):
        row -=1
        if(self.isInsideList(list,row,column)):
            newList = self.__pushUp(list,row,column)
            if((not self.hasBall(newList[row][column])) and self.hasBall(newList[row+1][column])):
                newList[row][column][Keys.ball.value] = newList[row+1][column][Keys.ball.value] 
                newList[row+1][column][Keys.ball.value] = Ball.none.value
            return newList
        else:
            return list
                
    def __pushDown(self,list,row,column):
        row +=1
        if(self.isInsideList(list,row,column)):
            newList = self.__pushDown(list,row,column)
            if((not self.hasBall(newList[row][column])) and self.hasBall(newList[row-1][column])):
                newList[row][column][Keys.ball.value] = newList[row-1][column][Keys.ball.value] 
                newList[row-1][column][Keys.ball.value] = Ball.none.value
            return newList
        else:
            return list
        
    def __pushRight(self,list,row,column):
        column +=1
        if(self.isInsideList(list,row,column)):
            newList = self.__pushRight(list,row,column)
            if((not self.hasBall(newList[row][column])) and self.hasBall(newList[row][column-1])):
                newList[row][column][Keys.ball.value] = newList[row][column-1][Keys.ball.value] 
                newList[row][column-1][Keys.ball.value] = Ball.none.value
            return newList
        else:
            return list
        
    def __pushLeft(self,list,row,column):
        column -=1
        if(self.isInsideList(list,row,column)):
            newList = self.__pushLeft(list,row,column)
            if((not self.hasBall(newList[row][column])) and self.hasBall(newList[row][column+1])):
                newList[row][column][Keys.ball.value] = newList[row][column+1][Keys.ball.value] 
                newList[row][column+1][Keys.ball.value] = Ball.none.value
            return newList
        else:
            return list

    def __pullUp(self,list,row,column):
        if(self.isInsideList(list,row-1,column)):
            if((not self.hasBall(list[row][column])) and self.hasBall(list[row-1][column])):
                list[row][column][Keys.ball.value] = list[row-1][column][Keys.ball.value] 
                list[row-1][column][Keys.ball.value] = Ball.none.value
            row -=1
            return self.__pullUp(list,row,column)
        else:
            return list
        
    def __pullDown(self,list,row,column):
        if(self.isInsideList(list,row+1,column)):
            if((not self.hasBall(list[row][column])) and self.hasBall(list[row+1][column])):
                list[row][column][Keys.ball.value] = list[row+1][column][Keys.ball.value] 
                list[row+1][column][Keys.ball.value] = Ball.none.value
            row +=1
            return self.__pullDown(list,row,column)
        else:
            return list

    def __pullRight(self,list,row,column):
        if(self.isInsideList(list,row,column+1)):
            if((not self.hasBall(list[row][column])) and self.hasBall(list[row][column+1])):
                list[row][column][Keys.ball.value] = list[row][column+1][Keys.ball.value] 
                list[row][column+1][Keys.ball.value] = Ball.none.value
            column +=1
            return self.__pullRight(list,row,column)
        else:
            return list

    def __pullLeft(self,list,row,column):
        if(self.isInsideList(list,row,column-1)):
            if((not self.hasBall(list[row][column])) and self.hasBall(list[row][column-1])):
                list[row][column][Keys.ball.value] = list[row][column-1][Keys.ball.value] 
                list[row][column-1][Keys.ball.value] = Ball.none.value
            column -=1
            return self.__pullLeft(list,row,column)
        else:
            return list

    def purpuleBallEffect(self,list,row,column):
        list = self.__pushUp(list,row-1,column)
        list = self.__pushDown(list,row+1,column)
        list = self.__pushLeft(list,row,column-1)
        list = self.__pushRight(list,row,column+1)
        return list 
    
    def redBallEffect(self,list,row,column):
        list = self.__pullUp(list,row-1,column)
        list = self.__pullDown(list,row+1,column)
        list = self.__pullLeft(list,row,column-1)
        list = self.__pullRight(list,row,column+1)
        return list 
                
