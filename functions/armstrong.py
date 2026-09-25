for i in range(100,1000):
    s=0
    i_str=str(i)
    for a in i_str:
        s=s+int(a)**3
    if s==i:
        print(i)    
