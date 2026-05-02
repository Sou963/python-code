class myClass:
    name='' 
    roll=0

obj=myClass()
obj.name='John'
obj.roll=101

print(f'name:{obj.name},roll:{obj.roll}')

newObj=myClass()
newObj.name='Jane'
newObj.roll=102
print(f'name:{newObj.name},roll:{newObj.roll}')