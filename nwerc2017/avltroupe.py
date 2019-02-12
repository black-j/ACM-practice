class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
    def find(self,data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.val):
            return True
        elif(data < self.val):
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
# AVL tree class which supports insertion, 
# deletion operations 
class AVL_Tree(object): 
  
    def insert(self, root, key): 
          
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                          self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    # Recursive function to delete a node with 
    # given key from subtree with given root. 
    # It returns root of the modified subtree. 
    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left),  
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left),  
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                          self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                          self.getHeight(y.right)) 
  
        # Return the new root 
        return y
    
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right)
def findR(root,key, length):
    if root == None:
        return 0
    if key < root.val:
        if root.left == None:
            return root.val
        else:
            return max(root.val, findR(root.left,key,length))
    else:
        return findR(root.right,key,length)
    
def findL(root,key):
    if root ==None:
        return -1
    if key > root.val:
        if root.right == None:
            return root.val
        else:
            return max(root.val, findL(root.right,key))
    else:
        return findL(root.left,key)
if __name__ == "__main__":
    zero_set = set()
    troupe = []
    avl = AVL_Tree()
    index = 0
    for i in input().strip():
        troupe.append(int(i))
        if i == '0':
            zero_set.add(index)
        index += 1

    mytree = avl.insert(root = None,key = -1)
    mytree = avl.insert(mytree,len(troupe))
    for i in zero_set:
       mytree = avl.insert(mytree,i)
   
    
    for i in range(len(troupe)):
        x = troupe[i]
        troupe[i] = 1
        if x == 2:
            L = findL(mytree,i)
            R = findR(mytree,i,len(troupe))
            #print(L,R)
            #avl.preOrder(mytree)
            #print(L,R)
            if L != -1:
                mytree = avl.delete(mytree,L)
            if R != len(troupe):
                mytree = avl.delete(mytree,R)
            #print(L,R)
            if  troupe[L+R-i] != 2:
                mytree = avl.insert(mytree,L+R-i)
            else:
                troupe[L+R-i] = 1
        

    
    for i in range(len(troupe)):
        if mytree.find(i):
            print('0',end='')
        else:
            print('1',end ='')
