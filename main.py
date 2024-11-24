from DFS import DFS
from BFS import BFS
from UCS import UCS
from node import Node
from init_states_of_cells import InitStatesOfCells
from copy import deepcopy
from draw_cells import DrawCells
from queue import PriorityQueue,Queue 

#     print("Queue : ")
#     q = Queue()
#     q.put(20)
#     q.put(10)
#     q.put(15)
#     print(q.get())
#     print(q.get())
#     print(q.get())
#
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
    hillClimbing=(state)
    hillClimbing.run()
    hillClimbing.printResult()

if __name__ == "__main__":
    main()