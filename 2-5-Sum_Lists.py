from linked_list import LinkedList
## sum of reversed list
# def sum_lists(ll1,ll2):
#     result=0
#
#     pointer=ll1.head
#     counter=0
#     while pointer:
#         result+=pointer.data*(10**counter)
#         pointer=pointer.next
#         counter+=1
#
#     pointer=ll2.head
#     counter=0
#     while pointer:
#         result+=pointer.data*(10**counter)
#         pointer=pointer.next
#         counter+=1
#
#     ll_sum=LinkedList()
#     while result:
#         digit=result%10
#         ll_sum.append(digit)
#         result //=10
#
#     return ll_sum

## forward version
def sum_lists(ll1,ll2):
    value1=value2=0

    pointer=ll1.head
    while pointer:
        value1=value1*10+pointer.data
        pointer=pointer.next

    pointer=ll2.head
    while pointer:
        value2=value2*10+pointer.data
        pointer=pointer.next

    result=value1+value2
    print value1,value2,result
    ll_sum=LinkedList()
    divider=10**(len(str(result))-1)
    while result:
        digit=result//divider
        ll_sum.append(digit)
        result=result%divider
        divider/=10

    #ll_sum.append(result)

    return ll_sum


def main():
    ll1=LinkedList()
    ll2=LinkedList()

    ll1.add_multiple([2,1,5])
    ll2.add_multiple([4,4,3,8])

    print ll1,ll2
    ll_sum=sum_lists(ll1,ll2)
    print ll_sum


if __name__=='__main__':
    main()
