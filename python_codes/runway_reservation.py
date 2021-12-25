class Node:
    
    def __init__(self,key):
        self.key=key
        self.height=1
        self.left=None
        self.right=None
        self.parent=None

class RTree:
    k=3
    
    def insert(n, key):
        if n is None:
            return Node(key)
        elif key<n.key and abs(n.key-key)>=RTree.k:
            n.left=RTree.insert(n.left,key)
            n.left.parent=n
        elif key>n.key and abs(n.key-key)>=RTree.k:
            n.right=RTree.insert(n.right,key)
            n.right.parent=n
        else:
            print("Sorry can't insert value ",key)
        n.height=max(RTree.getHeight(n.left),RTree.getHeight(n.right))+1
        n=RTree.rebalance(n)
        return n 
    
    def rebalance(n):
        balance=RTree.getBalance(n)
        if balance>1:
            if RTree.getHeight(n.left.left)>=RTree.getHeight(n.left.right):
                n=RTree.rightRotate(n)
            else:
                n.left=RTree.leftRotate(n.left)
                n=RTree.rightRotate(n)
        elif balance<-1:
            if RTree.getHeight(n.right.right)>=RTree.getHeight(n.right.left):
                n=RTree.leftRotate(n)
            else:
                n.right=RTree.rightRotate(n.right)
                n=RTree.leftRotate(n)
        return n

    def rightRotate(n):
        l=n.left
        r=n.left.right
        #performing rotation
        l.right=n
        n.left=r
        #updating parents
        l.parent=n.parent
        n.parent=l
        if r is not None:
            r.parent=n
        #updating height
        n.height=max(RTree.getHeight(n.left),RTree.getHeight(n.right))+1
        l.height=max(RTree.getHeight(l.left),RTree.getHeight(l.right))+1
        
        return l

    def leftRotate(n):
        r=n.right
        l=n.right.left
        #performing rotation
        r.left=n
        n.right=l
        #updating parents
        r.parent=n.parent
        n.parent=r
        if l is not None:
            l.parent=n
        #updating height
        n.height=max(RTree.getHeight(n.left),RTree.getHeight(n.right))+1
        r.height=max(RTree.getHeight(r.left),RTree.getHeight(r.right))+1
        
        return r
        
    def inorder(n):
        if(n is not None):
            RTree.inorder(n.left)
            print(n.key,end=" ")
            RTree.inorder(n.right)
    
    def getBalance(n):
        if n is not None:
            if n.left is not None:
                lh=n.left.height
            else:
                lh=0
            if n.right is not None:
                rh=n.right.height
            else:
                rh=0
            return lh-rh
    def getHeight(n):
        if n is not None:
            return n.height
        return 0
    
    def getMin(n):
        if n is None or n.left is None:
            return n
        else:
            return RTree.getMin(n.left)
    
    def delete(n,key):
        if not n:
            return n
        elif key<n.key:
            n.left=RTree.delete(n.left,key)
        elif key>n.key:
            n.right=RTree.delete(n.right,key)
        else:
            if n.left is None:
                temp=n.right
                if temp is not None:
                    temp.parent=n.parent
                n=None
                return temp
            elif n.right is None:
                temp=n.left
                if temp is not None:
                    temp.parent=n.parent
                n=None
                return temp
            temp=RTree.getMin(n.right)
            n.key=temp.key
            n.right=RTree.delete(n.right,temp.key)
        n.height=max(RTree.getHeight(n.left),RTree.getHeight(n.right))+1
        n=RTree.rebalance(n)
        return n

root=None
root=RTree.insert(root,10)
root=RTree.insert(root,50)
root=RTree.insert(root,20)
root=RTree.insert(root,60)
root=RTree.insert(root,30)
root=RTree.insert(root,40)
root=RTree.delete(root,50) 
RTree.inorder(root)
print()
print(RTree.getHeight(root))
print(RTree.getBalance(root))
print(root.key)

