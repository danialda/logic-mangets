from DFS import DFS
from BFS import BFS
from node import Node
from init_states_of_cells import InitStatesOfCells
from copy import deepcopy
from draw_cells import DrawCells
def main():
    init = InitStatesOfCells()
    state = Node(init.states[0])
    dfs=DFS(state)
    dfs.run()
    dfs.printResult()
    # bfs=BFS(state)
    # bfs.run()
    # bfs.printResult()

if __name__ == "__main__":
    main()