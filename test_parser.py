#!/usr/bin/env python
import parser
import ast
import pprint

src = """
def fact(n):
 return n
fact(1000000000000)
"""
ast1 = parser.suite(src)
a = ast1.compile()
#aa = ast1.compile()
eval(a)
tup = ast1.totuple()
pprint.pprint(tup)

node = ast.UnaryOp()
node.op = ast.USub()
node.operand = ast.Num()
node.operand.n = 5
node.operand.lineno = 0
node.operand.col_offset = 0
node.lineno = 0
node.col_offset = 0

print tup
print node
print ast1
print ast
ast2 = ast.parse("fact(1)")
print ast.dump(ast2)
print ast2

print ast.iter_fields(ast2)
pprint.pprint(ast2)

print fact(5)

ast2 = ast.parse("a.b.c(d(100))")
print ast.dump(ast2)
ast3 = ast.parse("print 3**3")
print ast.dump(ast3)
ast4 = ast.parse("A[1](2)")
print ast.dump(ast4)

print 1*2*-5

print 3**3

def f1():
	global v1
	v1 = 1

i = (1,2)
print i
print type(i)
print id(i)
i = '6'
if i == '6':
  print i
  print type(i)
  print id(i)
  i = '7'
  print i
  print type(i)
  j = '8'
print j
f1()
print v1
