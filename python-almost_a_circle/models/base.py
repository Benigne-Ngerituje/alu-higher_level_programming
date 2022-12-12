#!/usr/bin/python3

"""A base class"""

class Base: 

    """A base class"""

    __nb_objects = 0 #variable 

    def __init__(self, id=None): #function with id as parameter
        """Initialize a new id"""
        if id is not None: #conditional to check if ID is equal to none
            self.id = id #make self.id equal to id
        else: #if id is none
            Base.__nb_objects += 1 #increment the value of base
            self.id = Base.__nb_objects #equate base to self.id
