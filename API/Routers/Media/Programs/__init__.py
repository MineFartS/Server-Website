from philh_myftp_biz.pc import Path, loc
from philh_myftp_biz.web import URL

def cache(
    url: URL | str,
    name: str
) -> Path:
    
    if isinstance(url, str):
        url = URL(url)

    tfile = loc.temp.child(name)

    url.cache(tfile)

    return tfile

