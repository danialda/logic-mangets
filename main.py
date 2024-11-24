from DFS import DFS
from BFS import BFS
from UCS import UCS
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
    # bfs=BFS(state)
    # bfs.run()
    # bfs.printResult()
    # ucs=UCS(state)    
    # ucs.run()
    # ucs.printResult()
    hillClimbing=HillClimbing(state)
    hillClimbing.run()
    hillClimbing.printResult()

if __name__ == "__main__":
    main()