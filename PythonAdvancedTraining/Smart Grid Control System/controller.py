# controller.py
"""This is the program that handles energy dispatch"""
 # W0611: sys is unused
from utils import calcLoad  # C0103: function names don't match PEP-8

class GridController:  # C0103: class name should use CapWords
    '''This class controls the logic for the grids'''
    def __init__(self,controller_id,name):
        '''Initialising the parameters'''
        self.controller_id = controller_id
        self.name = name

    def dispatch(self,load):
        '''Logic for dispatching the load is written here'''
        x = calcLoad(load)
        print("Dispatching:", x)
        return x
