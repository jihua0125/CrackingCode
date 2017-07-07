from linked_list import Node
import unittest

def remove_dups(node_head):
    current=node_head
    ## using hash table
    node_dict={}
    node_dict[current.data]=1 ##initialization
    while current.next!=None:
        if node_dict.get(current.next.data,None)!=None: ## found duplicate
            current.next=current.next.next
        else:
            node_dict[current.next.data]=1
            current=current.next

    return node_head

def main():
    head=Node('h')
    cur=head
    for i in range(5):
        node_new=Node(i)
        cur.next=node_new
        cur=cur.next
    cur.next=Node(4)
    cur=cur.next
    cur.next=Node(2)

    cur=head
    while cur.next!=None:
        print cur
        cur=cur.next
    print cur

    no_dup=remove_dups(head)
    cur=no_dup
    while cur.next!=None:
        print cur
        cur=cur.next
    print cur

if __name__=='__main__':
    main()
