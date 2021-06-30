
class Node:
    def __init__(self,value):
        self._value=value
        self._location=None
        
    def nxt(self):
        return self._location
        
class LinkedList:
    def __init__(self):
        self._headval=None
        
    def printList(self):
        val=self._headval
        while val is not None:
            print(val._value)
            
            
            val=val._location
        
    def newHead(self,new):
        newNode= Node(new)
        newNode._location=self._headval
        self._headval=newNode
        
    def head(self):
        return self._headval

    
def nodeTrav(nod,i=0):
    if nod._value is not None:
        i=i+1
        nodeTrav(nod._location,i)
    else:
        return i
    
def listLen(lnklst):
    man=lnklst.head
    return nodeTrav(man)

            
 


        
    
        
list1=LinkedList()
list1._headval= Node(53)
list2= Node(45)
list3= Node(22)
list1._headval._location= list2
list2._location=list3
list1.printList()


list1.newHead(44)
list1.printList()
listLen(list1)


    
    

