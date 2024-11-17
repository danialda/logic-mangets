class BFS:
    def __init__(self,initNode):
        self.queue=[initNode]
        self.currentNode=None
        self.visitedNodes=[initNode.hash]
    def run(self):
        i=0
        while True:
            i=i+1
            print(i)
            self.currentNode=self.queue.pop(0)
            if self.currentNode.isEnd():
                self.currentNode.print()
            nextNodes=self.currentNode.nextNodes()
            for son in nextNodes:
                if not self.isVisited(son):
                    self.visitedNodes.append(son.hash)
                    self.queue.append(son)
            if (len(self.queue) == 0): break
    def printResult(self):
        path=[]
        iter=self.currentNode
        while iter!=None:
            path.append(iter)
            iter=iter.parent
        path.reverse()
        for node in path:
            node.print()
            print('-------------------')
    
    def isVisited(self,node):
        for visited in self.visitedNodes:
            if visited == node.hash:
                return True
        return False