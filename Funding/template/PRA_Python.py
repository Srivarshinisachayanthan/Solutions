class Person:
	def __init__(self,n,h,w):
		self.name=n
		self.height=h
		self.weight=w
 
class Society:
	def __init__(self,plist):
		self.personslist=plist
 
	def findAverageheight(self):
		result=[]
		for i in self.personslist:
			result.append(i.height)
		return sum(result)/len(result)
 
	def findTallerThanAverageperson(self):
		result=[]
		avg_height=self.findAverageheight()
		for i in self.personslist:
			if(avg_height<i.height):
				result.append(i.name)
		return result
 
if __name__ == "__main__":
	num=int(input())
	plist=[]
	for i in range(num):
		n=input()
		h=int(input())
		w=int(input())
		plist.append(Person(n,h,w))
	obj=Society(plist)
	print("The Average height is",round(obj.findAverageheight(),1))
	result=obj.findTallerThanAverageperson()
	print("Persons taller than the Average height")
	for i in result:
		print(i)
  