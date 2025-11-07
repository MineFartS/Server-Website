
from __init__ import root, IndexRegistry

registries: list[IndexRegistry] = []

for p in root.descendants():

    if p.isdir():

        registries += [IndexRegistry(p)]


for r in registries:

    for i in r.items():
        i.Update()

    print('Building Registry:', r.dir)

    r.build()
