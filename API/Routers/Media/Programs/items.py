from philh_myftp_biz.web.driver import Driver

class Blender:

    class Windows:
        url  = 'https://mirrors.iu13.net/blender/release/Blender3.6/blender-3.6.23-windows-x64.msi'
        ext = 'msi'

class Disk_Drill:

    class Windows:
        url = "https://win.cleverfiles.com/disk-drill-win.exe"
        ext = "exe"

    class MacOS:
        url = "https://dl.cleverfiles.com/diskdrill.dmg"
        ext = 'dmg'

class disk2vhd:
    
    class Windows:
        url = "https://live.sysinternals.com/disk2vhd64.exe"
        ext = "exe"

class Github_Desktop:

    class Windows:
        url = "https://central.github.com/deployments/desktop/desktop/latest/win32"
        ext = "exe"

    class MacOS:
        url = "https://central.github.com/deployments/desktop/desktop/latest/darwin"
        ext = 'zip'

class htTrack:

    class Windows:
        url = "https://download.httrack.com/cserv.php3?File=httrack_x64.exe"
        ext = "exe"

class IIS_Rewrite:

    class Windows:
        url = "https://download.microsoft.com/download/1/2/8/128E2E22-C1B9-44A4-BE2A-5859ED1D4592/rewrite_amd64_en-US.msi"
        ext = "msi"

class LTspice:

    class Windows:
        url = "https://ltspice.analog.com/software/LTspice64.msi"
        ext = "msi"

class Make:

    class Windows:
        url = "https://gigenet.dl.sourceforge.net/project/gnuwin32/make/3.81/make-3.81.exe?viasf=1"
        ext = "exe"

class Remove_MS_Edge:

    class Windows:
        url = "https://github.com/ShadowWhisperer/Remove-MS-Edge/releases/latest/download/Remove-Edge.exe"
        ext = "exe"

class Rockstar_Games_Launcher:

    class Windows:
        url = "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe"
        ext = 'exe'

class Steam:

    class Windows:
        url = "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe"
        ext = 'exe'

class YouTube_DL:
    
    class Windows:
        url = "https://www.github.com/ytdl-org/ytdl-nightly/releases/latest/download/youtube-dl.exe"
        ext = 'exe'

class Wake_On_Lan:

    class Windows:
        url = "https://github.com/basildane/WakeOnLAN/releases/download/2.12.4/WakeOnLAN_2.12.4.0.exe"
        ext = 'exe'

class VS_Code:

    class Windows:
        url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"
        ext = 'exe'
        
class TeraCopy:

    class Windows:
        url = "https://www.codesector.com/files/teracopy.exe"
        ext = 'exe'

class SurfShark:

    class Windows:
        url = "https://downloads.surfshark.com/windows/latest/SurfsharkSetup.exe"
        ext = 'exe'

class Ollama:

    class Windows:
        url = "https://ollama.com/download/OllamaSetup.exe"
        ext = 'exe'

class Minecraft_Launcher:

    class Windows:
        url = "https://launcher.mojang.com/download/MinecraftInstaller.exe"
        ext = "exe"

class Discord:

    class Windows:
        url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
        ext = "exe"

class Android_Studio:

    class Windows:

        ext = 'exe'
        
        @property
        def url(self):
            
            with Driver() as d:

                d.open('https://developer.android.com/studio')

                d.element('xpath', '/html/body/section/section/main/devsite-content/article/div[2]/section[1]/div/div/div/div[2]/div/div/p[2]/button')[0].click()

                url = d.element('id', 'agree-button__studio_win_notools_exe_download')[0].href

            return url
