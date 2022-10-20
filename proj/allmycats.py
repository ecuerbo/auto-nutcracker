from xml.dom.minidom import NamedNodeMap


catNames = []
while True:
    print('Enter the nmae of cat ' + str(len(catNames)+ 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatebnation
print('The cat names are:')
for name in catNames:
    print(' ' + name)