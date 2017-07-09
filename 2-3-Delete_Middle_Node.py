from linked_list import LinkedList

def delete_middle_node(middle_node):
    middle_node.data=middle_node.next.data
    middle_node.next=middle_node.next.next

def main():
    linked_list=LinkedList('a')
    for i in range(1,10):
        if i==5:
            middle_node=linked_list.append(chr(ord('a')+i))
        else:
            linked_list.append(chr(ord('a')+i))
    delete_middle_node(middle_node)
    print linked_list

if __name__=='__main__':
    main()
