from philh_myftp_biz.web import URL

class Blender:

    class Windows:
        url  = URL('https://mirrors.iu13.net/blender/release/Blender3.6/blender-3.6.23-windows-x64.msi')
        ext = 'msi'

class DiskDrill:

    class Windows:
        url = URL("https://win.cleverfiles.com/disk-drill-win.exe")
        ext = "exe"

class disk2vhd:
    
    class Windows:
        url = URL("https://live.sysinternals.com/disk2vhd64.exe")
        ext = "exe"

class GithubDesktop:

    class Windows:
        url = URL("https://central.github.com/deployments/desktop/desktop/latest/win32")
        ext = "exe"

class htTrack:

    class Windows:
        url = URL("https://download.httrack.com/cserv.php3?File=httrack_x64.exe")
        ext = "exe"

class IIS_Rewrite:

    class Windows:
        url = URL("https://download.microsoft.com/download/1/2/8/128E2E22-C1B9-44A4-BE2A-5859ED1D4592/rewrite_amd64_en-US.msi")
        ext = "msi"

class LTspice:

    class Windows:
        url = URL("https://ltspice.analog.com/software/LTspice64.msi")
        ext = "msi"
