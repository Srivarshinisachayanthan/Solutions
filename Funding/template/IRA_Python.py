class Employee:
    def _init_(self,n,d,s,lb):
        self.name=n
        self.designation=d
        self.salary=s
        self.leavesbalance=lb
 
class Organization:
    def _init_(self,elist):
        self.employee_list=elist
 
    def display_leaves(self,name):
        for i in self.employee_list:
            if i.name==name:
                for a,b in i.leavesbalance.items():
                    print(a,":",b)
         
    def checkLeaveEligibility(self,ename,tl,nol):
        for i in self.employee_list:
            if i.name==ename:
                for a,b in i.leavesbalance.items():
                    if a==tl:
                        if b>=nol:
                        	i.leavesbalance[a]=b-nol
                        	return 'True'
                        else:
                            return 'False'
        return 'not found'
if __name__ == '_main_':
    elist=[]
    num=int(input())
    for i in range(num):
        leaves={}
        name=input()
        designation=input()
        salary=int(input())
        ltype=int(input())
        for i in range(ltype):
        	key=input()
        	value=int(input())
        	leaves[key]=value
        elist.append(Employee(name,designation,salary,leaves))
    obj=Organization(elist)
    empname=input()
    Itype=input()
    nol=int(input())
    if(obj.checkLeaveEligibility(empname,Itype,nol)=='True'):
    	print("leave granted")
    	obj.display_leaves(empname)
    elif(obj.checkLeaveEligibility(empname,Itype,nol)=='False'):
    	print("leave not granted")
    	obj.display_leaves(empname)
    elif(obj.checkLeaveEligibility(empname,Itype,nol)=='not found'):
    	print("leave not granted")
    	print("Employee not found") 
     