from __init__ import root, IndexRegistry, PIDstore
from os import getpid
from re import sub

PIDstore.save(getpid())

mediaEXTs: list[str] = []

registries: list[IndexRegistry] = []

# ==========================================================

# Append the root registry
registries += [IndexRegistry(root)]

# Iter through all subfolders of root
for p in root.descendants():
    
    if p.isdir():
        # Append the folder as a registry
        registries += [IndexRegistry(p)]
    
    elif p.type() in ['image', 'video', 'audio']:
        
        if p.ext() not in mediaEXTs:
            mediaEXTs  += [p.ext()]

# Iter through the registries
for r in registries:

    # Iter through all items in the registry
    for i in r.items():
        
        # Update the registry item
        i.Update()

    print('Building Registry:', r.dir)

    # Build the registry
    r.build()

# ==========================================================

config = root.child('web.config')

rules = '<rules>'

for ext in mediaEXTs:

    rules += f"""
                <rule name="Open '{ext.upper()}' in Media Viewer" stopProcessing="true">
                    <match url="^(.+)\\.{ext}$" />
                    <action type="Rewrite" url="/_/Media/" appendQueryString="false" />
                    <conditions>
                        <add input="{{QUERY_STRING}}" pattern="raw=true" negate="true" />
                    </conditions>
                </rule>
"""

rules += '            </rules>'

mcode = sub(
    pattern = r'<rules>(.|\n)*<\/rules>', 
    repl    = rules, 
    string  = config.open().read()
)

config.open('w').write(mcode)