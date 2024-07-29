#
from __future__ import annotations
from Cell import Cell, CellParams


class WayParams:
    length = 10
    initial_cell = Cell


class Way:

    def init_way(self, length: int, initial_cell: Cell):
        self.way = []
        list(map(lambda x: self.way.append(initial_cell(CellParams)), range(length)))
        
    def test_insert_cell(self, position: int, c: Cell):
        self.insert_cell(c, position)
        assert self.way[position].name == c.name
        assert self.way[position].action == c.action
        
    def test_delete_cell(self, position: int):
        len_before = self.__len__()
        self.delete_cell(position)
        len_after = self.__len__()
        assert len_after == len_before + 1
        
    def insert_cell(self, position: int, c: Cell):
        self.way.insert(position, c)
        
    def delete_cell(self, position: int):
        self.way.pop(position)
        
    def __len__(self):
        return len(self.way)
        
    def __init__(self, params):
        self.init_way(params.length, params.initial_cell)