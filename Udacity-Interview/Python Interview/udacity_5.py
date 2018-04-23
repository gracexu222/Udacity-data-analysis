"""
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from the
end". You should copy/paste the Node class below to use as a representation of
a node in the linked list. Return the value of the node at that position.

e.g. 10->20->30->40->50
"""
head = None

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# Function to insert a new node at the beginning
def push(new_data):
    global head
    new_node = Node(new_data)
    new_node.next = head
    head = new_node

def question5(head, n):
    main_ptr = head
    ref_ptr = head
    count  = 0

    if(head is not None):
        while(count < n ):
            if(ref_ptr is None):
                print "%d is greater than the no. of nodes in list" %(n)
                return

            ref_ptr = ref_ptr.next
            count += 1

    while(ref_ptr is not None):
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.data


# Main program
def main():
    global head
    # Make linked list 10->20->30->40->50
    push(50)
    push(40)
    push(30)
    push(20)
    push(10)
    print question5(head, 4)

if __name__ == '__main__':
    main()
