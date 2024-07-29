#
from typing import Callable


class CellParams:
    name = 'cell_name'
    action = print

class Cell:
    
    def __init__(self, params: CellParams):
        self.name = params.name
        self.action = params.action
        self.action_arg = self.name
        
    def do_action(self):
        self.action(self.action_arg)
        
    def set_name(self, new_name: str):
        self.name = new_name
        
    def set_action(self, new_action: Callable):
        self.action = new_action