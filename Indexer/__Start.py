from IndexTypes import IndexRegistry, IndexEntry, Search
from philh_myftp_biz.terminal import Log
from __init__ import root
from re import sub

# ==========================================================
# BUILD REGISTRIES

# Clear the search registry
Search.save([])

# Iter through all descendants of root
for p in root.descendants():
    
    # If the path is a directory 
    if p.isdir():

        registry = IndexRegistry(p)

        Log.INFO(f'Building Registry: {registry}')

        # Clear the directory registry
        registry.save([])

        # Iter through all items in the registry
        for child in registry.children():

            entry = IndexEntry(child)
            
            Log.VERB(f'Adding Entry: {entry}')

            # Append the entry to the directory registry
            registry += entry.JSON

            # Append the entry to the search registry
            Search += entry.JSON

exit()

# ==========================================================
#

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