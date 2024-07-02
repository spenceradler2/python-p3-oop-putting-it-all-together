#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size

    def get_brand(self):
        return self._brand
    
    def get_size(self):
        return self._size
    
    def set_brand(self,brand):
        self._brand = brand
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        