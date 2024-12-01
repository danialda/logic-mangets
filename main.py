from DFS import DFS
from BFS import BFS
from UCS import UCS
from A_Star import A_Star
from node import Node
from init_states_of_cells import InitStatesOfCells
from copy import deepcopy
from draw_cells import DrawCells
from queue import PriorityQueue,Queue
from hill_climbing import HillClimbing

def main():
    init = InitStatesOfCells()
    state = Node(init.states[8])

    # dfs=DFS(state)
    # dfs.run()
    # dfs.printResult()
    # dfs.printTime()


    # bfs=BFS(state)
    # bfs.run()
    # bfs.printResult()
    # bfs.printTime()


    # ucs=UCS(state)    
    # ucs.run()
    # ucs.printResult()
    # ucs.printTime()


    # hillClimbing=HillClimbing(state)
    # hillClimbing.run()
    # hillClimbing.printResult()
    # hillClimbing.printTime()
    

    # a_Star=A_Star(state)
    # a_Star.run()
    # a_Star.printResult()
    # a_Star.printTime()


if __name__ == "__main__":
    main()