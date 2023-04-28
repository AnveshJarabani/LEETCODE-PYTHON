class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = None
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None    
    def append(self,data):
        new_node=Node(data,self.head)
        self.head=Node

        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list=LinkedList()
my_list.display()












# llist=LinkedList()
# first_node=Node('a')
# llist.head=first_node
# second_node=Node('b')
# third_node=Node('c')
# first_node.next=second_node
# second_node.next=third_node
# llist