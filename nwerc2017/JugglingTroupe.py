from math import floor
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data and self.leftChild != None:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data and self.rightChild != None:
            self.rightChild = self.rightChild.delete(data)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            if self.rightChild != None:
                self.rightChild = self.rightChild.delete(temp.data)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False



def inorder(root):
    if root is not None: 
        inorder(root.leftChild) 
        print(root.data) 
        inorder(root.rightChild)
        
def findR(root,key):
    if root == None:
        return 0
    if key < root.data:
        if root.leftChild == None:
            return root.data
        else:
            return max(root.data, findR(root.leftChild,key))
    else:
        return findR(root.rightChild,key)
    
def findL(root,key):
    if root ==None:
        return -1
    if key > root.data:
        if root.rightChild == None:
            return root.data
        else:
            return max(root.data, findL(root.rightChild,key))
    else:
        return findL(root.leftChild,key)
    
if __name__ == "__main__":
    zero_set = set()
    troupe = []
    mytree = Tree()
    index = 0
    for i in input().strip():
        troupe.append(int(i))
        if i == '0':
            zero_set.add(index)
        index += 1
    for i in zero_set:
        mytree.insert(i)
    mytree.insert(-1)
    mytree.insert(len(troupe))
    
    for i in range(len(troupe)):
        x = troupe[i]
        troupe[i] = 1
        if x == 2:
            L = findL(mytree.root,i)
            R = findR(mytree.root,i)
            if L != -1:
                mytree.delete(L)
            if R != len(troupe):
                mytree.delete(R)
            #print(L,R)
            if  troupe[L+R-i] != 2:
                mytree.insert(L+R-i)
            else:
                troupe[L+R-i] = 1
        

    
    for i in range(len(troupe)):
        if mytree.find(i):
            print('0',end='')
        else:
            print('1',end ='')
        
            
                
    #inorder(mytree.root)
