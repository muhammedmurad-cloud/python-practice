students ={"Ali" : 78,
           "Murad" : 95,
           "Aysel": 82,
           "Nigar" : 67,
           "Kamran" : 91}
for i in students.keys():
    if students.get(i) >= 90:
        print(i,students.get(i))