d={}
while True:
    storenum=input('enter the store along with its number :\n')
    d[storenum]={}
    storename=  input('enter store name : \n')
    d[storenum]['name']=storename
    d[storenum]['item']=[]
    i=0
    while True:
        itmname=input('enter item name :\n')
        itmqnty = eval(input('enter the item quantity : \n'))
        d[storenum]['item'].append({})
        d[storenum]['item'][i][itmname]=itmqnty
        print('item entered successfully')
        i+=1
        value=input('do you want to enter more such items ,pls enter [yes|no] :\n').lower().strip()
        t=['yes','no','n','y']
        while value not in t:
            value=input('wrong input for inputting items ,pls enter [yes|no] :\n')
        if value=='no':
            break
    print('details of',storenum,'entered successfully')
    value=input('do you want to enter more such stores details ,pls enter [yes|no] :\n').lower().strip()
    t=('yes','no','n','y')
    while value not in t:
        value=input('wrong input for inputting items ,pls enter [yes|no] :\n')
    if value=='no':
        break
print('details of supermarket saved successfully')
print(d)
            
        
    