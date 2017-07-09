class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

    # def append(self,node_y):
    #     self.next=node_y


class LinkedList:
    def __init__(self,data=None):
        ## set head
        self.head=Node(data)
        self.head.next=None

        ## set current pointer position
        self.current=self.head

        ## set counter
        self.counter=1

    def __str__(self):
        temp_list=[] ## list of nodes
        pointer=self.head
        while pointer.next!=None:
            temp_list.append(pointer.data)
            pointer=pointer.next
        temp_list.append(pointer.data)

        return ','.join(temp_list)


    def append(self,data):
        self.current.next=Node(data)
        self.current=self.current.next
        self.counter+=1
