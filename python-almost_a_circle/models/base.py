#!/usr/bin/python3
# models/base.py


# class Base:
#     __nb_objects = 0

#     def __init__(self, id=None):
#         if id is not None:
#             self.id = id
#         else:
#             Base.__nb_objects += 1
#             self.id = Base.__nb_objects

class Base: #the class base
    """Base class for managing object ids.

    This class provides a consistent way to manage the id attribute of objects
    in a project. The id attribute is initialized to a unique integer value
    when an object is created, unless a specific id value is provided.

    Attributes:
        __nb_objects (int): Private class attribute used to keep track of the
            number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None): #function with id as parameter
        """Initializes the object with a unique id value.

        Args:
            id (int, optional): If provided, this value will be used as the
                id of the object. If not provided, a unique id value will be
                generated for the object.

        Raises:
            TypeError: If the id argument is provided but is not an integer.
        """
        if id is not None: #conditional to check if ID is equal to none
            self.id = id #make self.id equal to id
        else: #if id is none
            Base.__nb_objects += 1 #increment the value of base
            self.id = Base.__nb_objects #equate base to self.id
