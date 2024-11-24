from queue import PriorityQueue
from copy import deepcopy

class HillClimbing:
    def __init__(self,initNode):
        self.priorityQueue = PriorityQueue()
        self.priorityQueue.put((initNode.heuristic,initNode))
        self.currentNode=None
        self.visitedNodes=[initNode.hash]
    def run(self):
        while True:
            current = self.priorityQueue.get()
            self.currentNode = deepcopy(current[1])
            if self.currentNode.isEnd():
                break
            nextNodes=self.currentNode.nextNodes()
            for son in nextNodes:
                if not self.isVisited(son):
                    self.visitedNodes.append(son.hash)
                    self.priorityQueue.put((son.heuristic,son))
            if (self.priorityQueue.empty()): break
    def printResult(self):
        path=[]
        iter=self.currentNode
        while iter!=None:
            path.append(iter)
            iter=iter.parent
        path.reverse()
        for node in path:
            print(f"heuristic : {node.heuristic}")
            node.print()
            print('-------------------')
    
    def isVisited(self,node):
        for visited in self.visitedNodes:
            if visited == node.hash:
                return True
        return False
    