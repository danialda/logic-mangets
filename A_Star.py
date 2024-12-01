from queue import PriorityQueue
from copy import deepcopy
from draw_cells import DrawCells
from base_algorithm import BaseAgorithm
from my_enums import Algorithm
import datetime
import global_var
class A_Star(BaseAgorithm):
    draw =  DrawCells()
    def __init__(self,initNode):
        global_var.algorithm = Algorithm.aStar
        self.priorityQueue = PriorityQueue()
        self.startTime = None
        self.endTime = None
        self.priorityQueue.put((initNode.cost + initNode.heuristic,initNode))
        self.currentNode=None
        self.visitedNodes=[initNode.hash]

    def run(self):
        self.startTime= datetime.datetime.now()
        while True:
            current = self.priorityQueue.get()
            self.currentNode = deepcopy(current[1])
            if self.currentNode.isEnd():
                break
            nextNodes=self.currentNode.nextNodes()
            for son in nextNodes:
                if not self.isVisited(son):
                    self.visitedNodes.append(son.hash)
                    self.priorityQueue.put((son.cost + son.heuristic,son))
            if (self.priorityQueue.empty()): break
        self.endTime= datetime.datetime.now()
    def printResult(self):
        path=[]
        iter=self.currentNode
        while iter!=None:
            path.append(iter)
            iter=iter.parent
        path.reverse()
        for node in path:
            print(f"cost : {node.cost + node.heuristic}")
            node.print()
            print('-------------------')
    
    def isVisited(self,node):
        for visited in self.visitedNodes:
            if visited == node.hash:
                return True
        return False
    def printTime(self):
        print(self.endTime - self.startTime)