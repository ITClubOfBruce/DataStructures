''' 
    id
    字典：connectedTo
    addNeighbor方法用于从这个顶点添加一个连接到另个一顶点，构造字典
    getConnections方法返回邻接表中的所有的点
    getWeight方法返回权重
'''

# 顶点
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]



# 图
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def addEdge(self,fromVert,toVert,weight=0):
        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertList:
            nv = self.addVertex(toVert)
        
        self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight)
    
    def getVertices(self):
        return self.vertList.keys()
    
    
    


