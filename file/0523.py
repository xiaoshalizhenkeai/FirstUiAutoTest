# -*- coding:utf-8 -*-
x = "0523"
print(x)
class Base:
  
    def __init__(self,path=None):
	if path == None:
	    self.path = "/opt/python3"
	else:
	    self.path = path
    
    def get_driver(self):
	driver = "xxx"
	return driver


	
