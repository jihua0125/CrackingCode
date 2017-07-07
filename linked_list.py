class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

    def append(self,node_y):
        self.next=node_y
