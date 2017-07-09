from linked_list import *

def return_kth_to_last(head,k):
    counter=k-1
    pointer=head
    while counter>0:
        pointer=pointer.next
        counter-=1

    ele_list=[]
    while pointer.next!=None:
        ele_list.append(pointer.data)
        pointer=pointer.next
    ele_list.append(pointer.data)

    return ' '.join(ele_list)

def main():
    linked_list=LinkedList('a')
    for i in range(1,26):
        linked_list.append(chr(ord('a')+i))
    print return_kth_to_last(linked_list.head,26)

if __name__=='__main__':
    main()
