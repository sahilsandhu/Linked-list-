class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None
class Linkedlist(object):
    def __init__(self):
        self.count=0
        self.head=None
    def addinstart(self,data):
        self.count=self.count+1 
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode
#in the end this is the entering the item oin the last of the list
    def addinend(self,data):
        self.count=self.count+1 
        creatednode=Node(data)
        actualnode=self.head
        while actualnode.nextnode is not None:
            actualnode=actualnode.nextnode
        actualnode.nextnode=creatednode
    def remove(self,data):
        self.count=selfcount-1
        currentnode=self.head
        previousnode=None
        while currentnode.data!=data:
            previousnode=currentnode
            currentnode=currentnode.nextnode
            if previosnode is None:
                self.head=currentnode.nextnode
            else:
                previousnode.nextnode=currentnode.nextnode
print('hello,friends chai pee looo')

num=True
while num:
    name=input('now tell me would you enter the data in starting or ending of the list')
    data=int(input('enter first data'))
    linked=Linkedlist()
    if name=='starting':
        print(linked.addinstart(data))
    else:
        print(linked.addinend(data))
    j=input('want to enter more')
    if j!='y':
        num=False
k=input('wnat to delete item form the list')
if k=='j':
   data=int(input('enter the element'))
   print(linked.remove(data))
    
        
        
    
            

            
        
    
