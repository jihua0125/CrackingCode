from linked_list import LinkedList

def palindrome(ll):
    fast_pointer=slow_pointer=ll.head

    stack=[]

    while fast_pointer and fast_pointer.next:
        stack.append(slow_pointer.data)
        fast_pointer=fast_pointer.next.next
        slow_pointer=slow_pointer.next

    if fast_pointer:
        stack.append(slow_pointer.data)

    while slow_pointer:
        value=stack.pop()
        if value!=slow_pointer.data:
            return False
        slow_pointer=slow_pointer.next

    return True

def main():
    true_palindrome=LinkedList()
    true_palindrome.add_multiple([1])
    print palindrome(true_palindrome)

    false_palindrome=LinkedList()
    false_palindrome.add_multiple([1,2,2,1])
    print palindrome(false_palindrome)


if __name__=='__main__':
    main()
