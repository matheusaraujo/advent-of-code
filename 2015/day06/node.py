import json

class Node:
    def __init__(self, begin, end, value, left, right):
        self.begin = begin
        self.end = end
        self.value = value
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def __str__(self):
        return self.toJSON()