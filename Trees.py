
class QNode :
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return (self.head == None)

    def length_(self):
        return self.size 

    def enqueue(self, data):

        newQueueNode = QNode(data)
        
        if self.head == None:
            self.head = newQueueNode
            self.tail = newQueueNode
            self.size +=1
            
        else:
            self.tail.next = newQueueNode
            self.tail = newQueueNode
            self.size +=1

    def dequeue(self):
        assert self.tail != None, " Cannot dequeue from empty Queue :-( "
        data = self.head.data
        self.head = self.head.next
        self.size -=1
        return data



class TreeNode():
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None

    def Lchild(self, data):
        self.left = data
    
    def Rchild(self, data):
        self.right = data
    
    def printTree(self):
        print(self.data, end=" ")
        if (self.left):
            self.left.printTree()
        if(self.right):
            self.right.printTree()

def BFS(root,n):
    if root is None:
        return
    else:
        flag = -1
        bfs = Queue()
        bfs.enqueue(root)
        while not bfs.isEmpty():
            ch = bfs.dequeue()
            if(ch.data == n):
                flag = 0
                return True
            else:
                if ch.left != None:
                    bfs.enqueue(ch.left)
                if ch.right != None:
                    bfs.enqueue(ch.right)
        if (flag == -1):
            return False



l = TreeNode(5)
l1 = TreeNode(6)
l2 = TreeNode(3)
l3 = TreeNode(8)
l4 = TreeNode(9)
l5 = TreeNode(2)
l.Lchild(l1)
l.Rchild(l2)
l1.Lchild(l3)
l1.Rchild(l4)
l2.Lchild(l5)
print("Tree : ")
l.printTree()
print("\n")

print("Searching for 5  : ",BFS(l,5))
print("Searching for 9  : ",BFS(l,9))
print("Searching for 15 : ",BFS(l,15))
print("Searching for 0  : ",BFS(l,0))


# Tree : 
# 5 6 8 9 3 2 

# Searching for 5  :  True
# Searching for 9  :  True
# Searching for 15 :  False
# Searching for 0  :  False
