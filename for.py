
for i in range(1,10,2):
	print i

a = {1:'a', 2:'b'}
for k,v in a.items():
	print k, v

a = {1:'a', 2:'b'}
for k,v in a.iteritems():
	print k, v

print type(a), type(a.iteritems())

def walk_tree(node):
	if not node:
	    return
	if node.leftnode:
	    for i in walk_tree(node.leftnode):
		yield i
	yield node
	if node.rightnode:
	    for i in walk_tree(node.rightnode):
	       yield i

for node in wald_tree(root):
	process(node)
