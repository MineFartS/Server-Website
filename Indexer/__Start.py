from __init__ import root, IndexRegistry, PIDstore
from os import getpid

PIDstore.save(getpid())

registries: list[IndexRegistry] = []

# Append the root registry
registries += [IndexRegistry(root)]

# Iter through all subfolders of root
for p in root.descendants():
    if p.isdir():
        # Append the folder as a registry
        registries += [IndexRegistry(p)]

# Iter through the registries
for r in registries:

    # Iter through all items in the registry
    for i in r.items():
        
        # Update the registry item
        i.Update()

    print('Building Registry:', r.dir)

    # Build the registry
    r.build()
