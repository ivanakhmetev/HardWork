#
from functools import reduce
import random
from Way import Way
from glovals import NXIST, MAXVERT, MINVERT


class LandParams:
        
    random.seed()
    num_vertix = random.randint(MINVERT, MAXVERT)
    num_ways = random.randint(MINVERT, MAXVERT)
    

class Land:
    
    def __init__(self, params: LandParams):
        self.schedule = [[NXIST] * params.num_vertix for _ in range(params.num_vertix)] # top - right diagonal

    def replace_way(self, way: Way, start: int, end: int):
        assert start < end 
        self.schedule[start][end] = way
        
    def calculate_ways(self):
        
        def count_if_way(acc: int, w: Way | int):
            if type(w) is Way:
                return acc + 1
            return acc
        
        def _in_schedule(acc: int, schedule: list):
            _acc = reduce(count_if_way, schedule)
            if _acc != 0:
                return _acc + acc
            return acc

        return reduce(_in_schedule, self.schedule, 0)
    
    # def view():
    #     pass

    def test_generate_land(self, params: LandParams):
        starts = [random.randint()]
        
        
class RatEnv:
    
    def __init__(self, land: Land, current: int, target: int):
        self.land = land
        self.current = current
        self.target = target
