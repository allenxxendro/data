#Huffman code 
string= "BCAADDDCCACACAC"
class NodeTree(object):
def__init__(self,left=None,right=None):
 self.left=left
 self.right=right
def children(self):
 return(self.left,self.right)
def nodes(self):
 return(self.left,self.right)
def__str__(self):
 return"%S__%S"S"%(self.left,self.right)

def huffman_code_tree(node.left=True,binString=" "):
 if type(node)is str:
 return { node:binString}
 (l,r) = node.children()
d = dict()
d.update(huffman_code_tree(l,True, binString + "0"))
d.update(huffman_code_tree(r,True, binString + "1"))
return d
Freq = { }
for c in String:
 if c in freq:
 freq [c] += 1
 else:
  freq[c] = 1
freq = sorted (freq.items(),key=lambda x:x[1] reverse= True)
nodes = freq
while len(nodes)>1:
(key 1,c1) = nodes[-1]
(key 2,c2) = nodes[-2]
node.append(nodes,key=lambda x:x[1] reverse= True)
Huffmancode = huffman_code_tree(node[0][0])
print("char | HuffmanCode ")
for (char, frequency);in freq:
 print (% -ur / % 125"(char, huffmancode[char])
    