def order_food(lst): 
    standard=0
    vegetarian =0
    vegan =0 
    diabetic =0
    gluten_intolerant=0
    for i in lst:
        for key in i.keys():
            if key == 'meal':
                if i[key]=='standard':
                   standard=standard+1
                elif i[key]=='vegetarian':
                   vegetarian=vegetarian+1
                elif i[key]=='vegan':
                   vegan=vegan+1
                elif i[key]=='diabetic':
                   diabetic=diabetic+1
                else:
                   gluten_intolerant=gluten_intolerant+1
    dictory=dict()                
    if standard !=0:
       dictory['standard']=standard
    if vegetarian !=0:
       dictory['vegetarian']=vegetarian
    if vegan !=0:
       dictory['vegan']=vegan
    if  diabetic !=0:
       dictory['diabetic']=diabetic
    if gluten_intolerant !=0:
       dictory['gluten-intolerant']=gluten_intolerant   
    return dictory