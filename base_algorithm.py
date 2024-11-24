from abc import ABC, abstractmethod
class BaseAgorithm(ABC): 
    @abstractmethod
    def run():
        pass 
    @abstractmethod
    def printResult():
        pass 
    @abstractmethod
    def isVisited():
        pass