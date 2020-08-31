board =  {'0h': 'bking', '6c': 'bking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

for k, v in board:
    if k not in '12345678':
        print(k+v,'number out of range')
    if v not in 'abcdefgh':
        print(k+v,'letter out of range')

for k,v in board.items():
    count = 0
    for i, j in board.items():
        if v == j:
            count += 1
    if count > 1:
        print('exception, double piece', v, 'at', k)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printInv(inventory):
    count = 0
    for k, v in inventory.items():
        print(v, k)
        count += v

    print(count, 'items')

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

for i in loot:
    copy = inventory.copy()
    for k, v in inventory.items():
        if k == i:
            copy[k] += 1
        else:
            copy.setdefault(i,1)
    inventory = copy.copy()

printInv(inventory)





