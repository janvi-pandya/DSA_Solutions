#
# PROBLEM EXPLANATION
# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. 
# Either head pointer may be null meaning that the corresponding list is empty.
# 

#!/bin/python3

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data),end=sep)

        node = node.next

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    # Check if either head1 or head2 is None
    if not head1:
        return head2
    if not head2:
        return head1
    
    # Initialize the merged head and tail
    if head1.data < head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next
    merged_tail = merged_head
    
    # Merge the remaining nodes
    while head1 and head2:
        if head1.data < head2.data:
            merged_tail.next = head1
            head1 = head1.next
        else:
            merged_tail.next = head2
            head2 = head2.next
        merged_tail = merged_tail.next
    
    # Append the remaining nodes (if any)
    if head1:
        merged_tail.next = head1
    else:
        merged_tail.next = head2
    
    return merged_head

if __name__ == '__main__':
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

        print_singly_linked_list(llist3, ' ')
        print('\n')
