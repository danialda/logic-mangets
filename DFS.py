from base_algorithm import BaseAgorithm
class DFS(BaseAgorithm):
    def __init__(self,initNode):
        self.stack=[initNode]
        self.currentNode=None
        self.visitedNode=[initNode.hash]
    def run(self):
        i=0
        while True:
            i=i+1
            print(i)
            self.currentNode=self.stack.pop()
            if self.currentNode.isEnd():
                break
            nextNodes=self.currentNode.nextNodes()
            for son in nextNodes:
                if not self.isVisited(son):
                    self.visitedNode.append(son.hash)
                    self.stack.append(son)
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
        for visited in self.visitedNode:
            if visited == node.hash:
                return True
        return False