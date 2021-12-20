def mergeLists(head1, head2):
    
    temp=dummy=SinglyLinkedListNode(0)
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    while(head1 and head2):
        if head1.data<head2.data:
            temp.next=head1
            head1=head1.next
        else:
            temp.next=head2
            head2=head2.next
        temp=temp.next
    if head1:
        temp.next=head1
    if head2:
        temp.next=head2
    return(dummy.next)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
