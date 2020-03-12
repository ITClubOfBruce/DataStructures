'''
    列表表示
'''
# myTree = ['a',['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]

# print('左树：',myTree[1])
# print('根节点：',myTree[0])
# print("右树：",myTree[2])


'''
    抽象数据类型  ADT或者节点表示方式
'''

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        # 新树的根节点
        self.leftChild = None
        self.rightChild = None
    
    # 插入左树
    def insertLeft(self,newMode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newMode)
        else:
            temp = BinaryTree(newMode)
            temp.leftChild = self.leftChild
            self.leftChild = temp 

    # 插入右树
    def insertRight(self,newMode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newMode)
        else:
            temp = BinaryTree(newMode)
            temp.rightChild = self.rightChild
            self.rightChild = temp 


    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())