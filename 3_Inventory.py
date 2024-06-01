#! python3
playerinventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addtoinventory(playerinventory, loot):
    for item in loot:
        playerinventory.setdefault(item, 0)
        playerinventory[item] += 1
    print(playerinventory)

addtoinventory(playerinventory, dragonloot)