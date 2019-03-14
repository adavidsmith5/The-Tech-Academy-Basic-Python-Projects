fName = 'Tony'
mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        lst.append("{0} {1} {2}".format(name, mySentence, i))
    return lst



lst = color_function(fName)
for i in lst:
    print(i)
