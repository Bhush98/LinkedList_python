# Singly Linked List

# Defining the Class Node having Fields data and next 
# Data = for storing the data 
# Next = to point to the next node in the List

# if we visualize this the Node class can be represented as 

# class Node :
#              ------------
#             | data |next |
#              ------------

'''

class LinkedList to mintain the list to perform operations on the list 

i.e Node is just a blueprint of what the boxes will look like in the list 

But we will make use of class Linkedlist to perform operations

suppose we create a object of class linkedlist so in memory it will be 

l1 ->    -------------      --------------
        | data | next | -> | data2 | next |
         -------------      --------------

l2 - >   -------------      --------------
        | data | next | -> | data2 | next |
         -------------      --------------

you can create as many Linked List you want using the class LinkedList
you just have to do is create a LinkedList object 
'''

#Initializing Class Node 
class Node: 

    def __init__(self):
        self.data = None
        self.next = None
#Initializing Class Linked list  
class linkedlist:

    def __init__(self):
        self.head = None

    # This function will insert a new_node at the Start of Linked List
    # Visualizing it 

    ''' 
                        -------------
                       | data | next | -> Current head
                        -------------

            When a new_node is inserted in Linked List it becomes the head and the 
            next part points to the previous node

                             -------------      -------------
                new_node -> | data | next | -> | data | next |
                             -------------      -------------
                                head
    
    '''
    def insertatstart(self):
        new_node = Node() #creating a new_node 
        # Getting data for new_node
        a = input("Enter the data you want to put in node :")
        # initializing new_node.data to data we get from user
        new_node.data = int(a)
        # please refer the above diagram to understand the process
        # making new_node.next to point to previous head
        new_node.next = self.head
        # making new_node as the current head
        self.head = new_node

    # function to print the Linked list
    def printlist(self):
        # we will initialize a variable temp assigning it the value as self.head
        temp = self.head
        # A while loop till temp is not null
        while(temp):
            # printing the data 
            print(temp.data)
            # The below step is necessary to keep the linked list going 
            # this step will assign the temp node to the next node
            temp = temp.next
        
    # This function will append the Linked List i.e it will add the new_node at the end
    def appendlist(self):
        #Initializing a new_node 
        new_node = Node()
        a = input("Enter the data for the Node : ")
        #initializing the new_node.data to the calue we accepted from the user
        new_node.data = int(a)
        # here I have initialized new_node.next = None because as it will be the last Node in the List
        # if we have a new_node coming we can then assign new_node.next to the next_node
        new_node.next = None

        # We check if head is null or not if it is then er declare new_node as head
        if(self.head == None):
            self.head = new_node
        
        # If not we traverse the list till the last 
        # Initializing last as head
        last = self.head
        # Traversing the list till the end 
        while(last.next != None):
            last = last.next
        
        # As we are at the last node in the list we initialize the last.next to point to the 
        # new_node
        last.next = new_node


    # This function will insert a node after the specified index or key value
    def insertafterkey(self,key):
        # Creating a new node 
        new_node = Node()
        a = input("Enter the data for Node : ")
        # initializing new_node.data with the data we got from user
        new_node.data = int(a)

        # Initializing the temp variable to head
        temp = self.head

        # Traversing the list till the node after which the node with our given key is present
        while(temp != None and temp.data!=key):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # This function will delete a specified node from the list 
    def deletedataNode(self,key):

        #Initializing temp with head so now temp is our head
        temp = self.head
        # We will create a prev variable of type Node i.e it is object of class Node
        prev = Node()

        # if temp i.e head ,if it empty that means the list is empty
        if(temp == None):
            print("The list is empty ")
            return
        
        # if we find the key at the first index we initialize self.head to the value that is present in 
        # it's next
        if(temp.data == key):
            self.head = temp.next
            return

        # We traverse till the node 
        if(temp!=None):
            while(temp.data!=key):
                # we store our temp in previous 
                prev = temp
                # we initialize our temp variable to it's next value
                temp = temp.next

        # we initialize our prev of next as temp.next i.e 
        '''
                         ------------------------
                        |                        |
             -------------    --------------     -------------
            | data | next |  | data | next |    | data | next |
             -------------    --------------     -------------
                prev         Node to be deleted    next node

        '''
        prev.next = temp.next
        return


    # Searching in our list for the particular 
    def search(self,key):
        temp = self.head
        index = 0
        while(temp!=None and temp.data!=key):
            index += 1
            temp = temp.next
        return index        
        
        
if __name__ == "__main__":
    l1 = linkedlist()
    choice = 0
    while(choice!=7):
        print("\n")
        print("1 : Insert Data at the start of Linked List ")
        print("2 : Append data to the List ")
        print("3 : Insert Data After a Particular Node  ")
        print("4 : Delete Data from the Linked List ")
        print("5 : Search Data from the Linked List  ")
        print("6 : Print the Linked list ")
        print("7 : Exit ")
        choice = int(input(" \nEnter you choice : "))
        if(choice == 1):
            print("\n") 
            b = input("Enter the Number of Nodes you want to insert :")
            for i in range(int(b)):
                l1.insertatstart() 
        elif(choice == 2):   
            print("\n") 
            b = input("Enter the Number of Nodes you want to insert :")
            for i in range(int(b)):
                l1.appendlist() 
        elif(choice ==3):
             b = input("Enter the key after which you want to add your data : ")
             l1.insertafterkey(int(b))  
        elif(choice == 4):
             b = input("Enter the key you want to delete from the node : ")  
             l1.deletedataNode(int(b))
        elif(choice == 5):
             b = input("Enter the data you want to find : ")
             index = l1.search(int(b))
             print("The key is at index " + str(index))
        elif(choice == 6) :  
            print("The following are the content of the List : ")
            l1.printlist()
        