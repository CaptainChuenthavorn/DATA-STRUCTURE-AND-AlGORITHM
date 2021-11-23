''' ↙ ↘
Tree คือ คล้ายกับ linkedlist ที่มี node หลายๆ node มาเชื่อมต่อ แต่แตกต่างกันที่วิธีการเชื่อมต่อ
- Definition Tree
    1.empty ไม่มี nodes เรียก null tree / emptytree
    2.ประกอบไปด้วย 
        1. root node ราก      ชื่อของ tree เรียกตาม root     e.g. Tree R     R 
        2. >=0 subtrees ส่วนประกอบของtree                            ↙     ↘
                                                                  A       B       C
                                                                 ↙  ↘       ↘     ↓
                                                                D    E       F    G
                                                              subtree A   ↙  ↓  ↘
                                                                         H   I   J
                                                                                 ↓
                                                                                 K
                                                                        subtree B 
                                                                 
                                                                 
                                                                 - root A
                                                                 - subtree D,E
โดย subtree ต้องเป็น tree ด้วย
เส้นเชื่อม เรียก edge(branch)
node ใน tree ต้อง disjoint กัน
ต้องไม่มีnode ร่วมกัน ใน root หรือใน subtree    I J 
                                         ↘ ↓
                                           K
                                        ไม่ใช่tree

- Binary Tree
มีลูกอย่างมากที่สุด 2 subtrees (0,1,2 subtrees)
ลูก ด้านซ้ายต้องน้อยกว่าตัวพ่อ
ลูก ด้านขวาต้องมากกว่าหรือเท่ากับตัวพ่อ
traversal การไปเยี่ยมชม
- breadth First จากroot ไปด้านข้างก่อน
หาลูกคนแรก คน2 คน3 ... จนครบทุกคน
- dep

มีการเรียกอย่างเดียว get... เรียก accessor
มีการแก้ไข set.. เรียก mutator
'''

# A Python class that represents an individual node
# in a Binary Tree



class BST:
  def __init__(self,data):
    self.data = data 
    self.left = None
    self.right = None
  def insert(self,data):
    if data == self.data:
      return
    if data<self.data:
      #add data in left subtree
      if self.left:
        #left node is not empty
        self.left.insert(data)
      else:
        #left node is empty
        self.left = BST(data)
    else:
      #add data in right subtree
      if self.right:
        #left node is not empty
        self.right.insert(data)
      else:
        #left node is empty
        self.right = BST(data)
  def in_order_traversal(self):
    ele=[]
    #visit left tree
    if self.left:
      ele+=self.left.in_order_traversal()
    #visit base node
    ele.append(self.data)
    if self.right:
      ele+=self.right.in_order_traversal()
    
    return ele
  def search(self,val):
    if self.data ==val:
      return True
    if val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False
    if val>self.data:
      if self.right:
        return self.right.search(val)
      else:
        return False
def build_tree(elements):
  root = BST(elements[0])

  for i in range(1,len(elements)):
    root.insert(elements[i])
  return root

numbers=[17,4,1,20,9,23,18,34]
numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(1))