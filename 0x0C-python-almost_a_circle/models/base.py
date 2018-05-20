#!/usr/bin/python3
"""This class is the base class"""
import json


class Base:
    """Base class for all other modules
    Attributes:
        __nb_objects: private attribute to count objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class
        Args:
            id: input id
        Attributes:
            id: public instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json representation of the list_dictionary
        Args:
            list_dictionaries: input list of dictionary
        Returns:
            Json representation of the dictionary or empty when
            dictionary doesn't exist
        """
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes Json representaiton to file
        Args:
            list_objs: input object to turn to json
        """
        new_list = []
        if list_objs != None:
            new_list = [obs.to_dictionary() for obs in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns list represented by json
        Args:
            json_string: input json string
        Returns:
            list representation fo json
        """
        if json_string == None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute set
        Args:
            dictionary: dictionary inputed
        Return:
            isntance with all the set attributes
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        else:
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                return [cls.create(**obj) for obj in
                        cls.from_json_string(f.read())]
        except Exception:
            return []
