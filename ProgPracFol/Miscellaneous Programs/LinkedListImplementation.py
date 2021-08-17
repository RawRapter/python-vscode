"""
Here We will create linkedlist data structure using class and will define reverse method
"""
#Creating Class Node
class node:
    #function initializing node
    def __init__(self,data):
        self.data = data
        self.next= None

#Creating linkedlist class
class linkedlist:
    #function intializing head
    def __init__(self):
        self.head = None
    
    #function reversing a linked list
    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
    
    #Pushing in beginning
    def pushbegin(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #Pushing in End
    def pushend(self,new_data):
        new_node = node(new_data)
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        temp.next = new_node

    #Deleting a node
    def delete(self,key):
        temp = self.head
        #Node to be deleted is first node
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        #If key is at other location
        while(temp is not None):
            if(temp.data == key):
                break
            #Using previous pin point to remember preivous node
            previous = temp
            temp = temp.next
        
        #if key is not present
        if(temp == None):
            return

        #unlinking the key and joining it's next with previous one
        previous.next = temp.next
        #freeing temp
        temp = None


    #Printing
    def printlinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=",")
            temp = temp.next

#Driver program
Llist = linkedlist()
Llist.pushbegin(5)
Llist.pushbegin(4)
Llist.pushend(3)
Llist.pushbegin(2)
Llist.pushbegin(1)
print("Without Reversed")
Llist.printlinkedlist()
print()
Llist.reverse()
print("Reversed")
Llist.printlinkedlist()
print()
print("Deleting 4")
Llist.delete(4)
Llist.printlinkedlist()