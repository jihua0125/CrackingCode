from linked_list import LinkedList
import numpy as np
def partition(ll,value):
    current=ll.tail=ll.head
    while current:
        next_node=current.next
        if current.data<value:
            current.next=ll.head
            ll.head=current
        else:
            ll.tail.next=current
            ll.tail=current
        current=next_node

    if ll.tail.next !=None:
        ll.tail.next = None



def main():
    linked_list=LinkedList()
    random_list=np.random.permutation([1,2,3,4,5,6,7,8,9,10])
    for i in random_list:
        linked_list.append(i)
    print linked_list
    partition(linked_list,7)
    print linked_list


if __name__=='__main__':
    main()
