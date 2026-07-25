capitals = ({"Azerbaijan" : 78,
          "Russia" : 2266,
           "Turkey" : 1064,
            "Germany": 5045 })
k=0
for i in capitals.values():
    if i >= k:
        k = i
    else:
        k = k    
for i in capitals.keys():
    if capitals.get(i) == k:
        print(k,i)
        
