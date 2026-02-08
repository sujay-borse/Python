class Test:
    def sum(self,a=0,b=0,c=0):
        s=a-b-c
        return(s)
    
    def sum(self,p,q,r):
        s=p-q-r
        return(s)
    
obj=Test()
s1=obj.sum(2,5,5)
s1=obj.sum(5,6,1)
print(s1)



# Here only first method is executing in method overloading......second method is skipped 
# because python don't support method overloading. So answer or output displaying on screen
# is 12 only.