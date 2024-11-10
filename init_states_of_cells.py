import numpy as np
from my_enums import Cell,Ball,Keys
class InitStatesOfCells:

    def init_B_C(ball,isTarget=False):
        return {
            Keys.ball.value: ball.value,
            Keys.cell.value: Cell.target.value if isTarget else Cell.path.value
        }    
    states=[
        np.array([
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.grey),init_B_C(Ball.none,True)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
    ]),
        np.array([
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none,True),init_B_C(Ball.grey),init_B_C(Ball.none,True),init_B_C(Ball.grey),init_B_C(Ball.none,True)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none)]
    ]),
        np.array([
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none,True)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none,True)],
    ]),  
        np.array([
        [init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none,True)],
        [init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.none)],
    ]),  
        np.array([
        [init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none,True)],
        [init_B_C(Ball.grey,True),init_B_C(Ball.none),init_B_C(Ball.grey,True)],
        [init_B_C(Ball.grey),init_B_C(Ball.none),init_B_C(Ball.grey)],
        [init_B_C(Ball.none,True),init_B_C(Ball.purpule),init_B_C(Ball.none)],  
    ]),  
        np.array([
        [init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.grey,True),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.grey),init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none,True)],
        [init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.grey,True),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none,True)], 
    ]),  
        np.array([
        [init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.none)],
    ]),  
        np.array([
        [init_B_C(Ball.grey,True),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.red,True)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.none,True),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.grey),init_B_C(Ball.none)],
        [init_B_C(Ball.purpule,True),init_B_C(Ball.none,True),init_B_C(Ball.none,True),init_B_C(Ball.grey)],
    ])    

    
    ]


    def selectState(self,index):
        return self.states[index]