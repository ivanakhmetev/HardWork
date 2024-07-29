#
import time
from Land import RatEnv
from Cell import Cell
from glovals import NXIST, SECCEL

class RatParams:
    
    speed = 10

class Rat:
    
    def __init__(self, params: RatParams, env: RatEnv):
        self.params = params
        self.env = env
    
    def set_target_vertix(self, vertix: int):
        self.env.target = vertix
    
    def get_possible_target(self):
        vertix = self.env.land.schedule[self.env.current]
        return [i for i in range(len(vertix)) if vertix[i] != NXIST]
    
    # def event_change_target(self, ):
    #     pass
    
    def walk(self):
        way = self.env.land.schedule[self.env.current][self.env.target]
        list(map(self.inspect, way.way))
        
    def enter(self, cell: Cell):
        pass
    
    def leave(self, cell: Cell):
        pass
    
    def consume_time(self):
        time.sleep(SECCEL / self.params.speed)
    
    def inspect(self, cell: Cell):
        self.enter(cell)
        cell.do_action()
        self.consume_time()
        self.leave(cell)
        