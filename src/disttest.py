#!usr/bin/env python
#list
name = ['macel','zhangkai','zkorangesun']


#dist
d = {"macel":95,"zhangkai":84,"zkorangesun":93}
print d['macel']

print name[0]
print d.get('zk')
if 'zk' in d:
	print 'y'
else:
	print 'n'


print abs(-100)

def my_abs(arg):
	return abs(arg)

print my_abs(-101)
print "hello"