from philh_myftp_biz.web.driver import Driver

class Blender:
    
    Windows  = 'https://mirrors.iu13.net/blender/release/Blender3.6/blender-3.6.23-windows-x64.msi' # TODO Make Dynamic

class Disk_Drill:

    Windows = "https://win.cleverfiles.com/disk-drill-win.exe"

    MacOS = "https://dl.cleverfiles.com/diskdrill.dmg"

class disk2vhd:
    
    Windows = "https://live.sysinternals.com/disk2vhd64.exe"

class Github_Desktop:

    Windows = "https://central.github.com/deployments/desktop/desktop/latest/win32"

    MacOS = "https://central.github.com/deployments/desktop/desktop/latest/darwin"

class htTrack:

    Windows = "https://download.httrack.com/cserv.php3?File=httrack_x64.exe"

class IIS_Rewrite:

    Windows = "https://download.microsoft.com/download/1/2/8/128E2E22-C1B9-44A4-BE2A-5859ED1D4592/rewrite_amd64_en-US.msi"

class LTspice:

    Windows = "https://ltspice.analog.com/software/LTspice64.msi"

class Make:

    Windows = "https://gigenet.dl.sourceforge.net/project/gnuwin32/make/3.81/make-3.81.exe?viasf=1"

class Remove_MS_Edge:

    Windows = "https://github.com/ShadowWhisperer/Remove-MS-Edge/releases/latest/download/Remove-Edge.exe"

class Rockstar_Games_Launcher:

    Windows = "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe"

class Steam:

    Windows = "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe"

class YouTube_DL:
    
    Windows = "https://www.github.com/ytdl-org/ytdl-nightly/releases/latest/download/youtube-dl.exe"

class Wake_On_Lan:

    Windows = "https://github.com/basildane/WakeOnLAN/releases/download/2.12.4/WakeOnLAN_2.12.4.0.exe"

class VS_Code:

    Windows = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"
        
class TeraCopy:

    Windows = "https://www.codesector.com/files/teracopy.exe"

class SurfShark:

    Windows = "https://downloads.surfshark.com/windows/latest/SurfsharkSetup.exe"

class Ollama:

    Windows = "https://ollama.com/download/OllamaSetup.exe"

class Minecraft_Launcher:

    Windows = "https://launcher.mojang.com/download/MinecraftInstaller.exe"

class Discord:

    Windows = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"

class Android_Studio:
 
    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://developer.android.com/studio')

            d.element('xpath', '/html/body/section/section/main/devsite-content/article/div[2]/section[1]/div/div/div/div[2]/div/div/p[2]/button')[0].click()

            return d.element('id', 'agree-button__studio_win_notools_exe_download')[0].href

class Balena_Etcher:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://etcher.balena.io/#download-etcher')

            return d.element('class', 'download-link-wrapper')[0].children[0].href

class Git:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://git-scm.com/install/windows#:~:text=Windows/x64')

            return d.element('xpath', '/html/body/div[2]/div/div[2]/div/div/div[2]/p[2]/strong/a')[0].href

class HandBrake:

    @property
    def Windows(self):
        with Driver() as d:
            
            d.open('https://handbrake.fr/downloads.php')

            return d.element('xpath', '/html/body/section/div[2]/a[1]')[0].href

class Plex_Media_Server:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://www.plex.tv/media-server-downloads/?cat=computer&plat=windows')

            return d.element('class', 'release-link')[0].href

class Rufus:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://rufus.ie/en/')

            return d.element('xpath', '/html/body/div[2]/section[5]/table[1]/tbody/tr[2]/td[1]/a')[0].href

class WinTV_10:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://www.hauppauge.com/pages/support/support_wintv10.html')

            return d.element('xpath', '/html/body/main/article/section/div/div/div[1]/div/div[2]/p[1]/a[1]')[0].href

class VLC:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://www.videolan.org/vlc/')

            return d.element('xpath', '/html/body/div[1]/div[2]/section/div/div[2]/div[4]/div[1]/ul/li[2]/a')[0].href

class Zadig:

    @property
    def Windows(self):
        with Driver() as d:

            d.open('https://zadig.akeo.ie/')

            return d.element('xpath', '/html/body/div[3]/ul[2]/li[1]/span/b/a')[0].href

class BlueStacks:
    
    Windows = "https://www.bluestacks.com/#:~:text=Download" # TODO

class _7_Zip:

    Windows = "https://www.7-zip.org/#:~:text=Windows x64 (64-bit)" # TODO

class Advanced_Renamer:

    Windows = "https://www.advancedrenamer.com/download#:~:text=Download for Windows" # TODO

class FileZilla_Client:

    Windows = "https://filezilla-project.org/download.php?type=client#:~:text=(64bit%20x86)" # TODO

class FileZilla_Server:

    Windows = "https://filezilla-project.org/download.php?type=server#:~:text=(64bit x86)" # TODO

class FireFox:

    Windows = "https://www.firefox.com/en-US/thanks/" # TODO

class Flow_Frames:

    Windows = "https://nmkd.itch.io/flowframes/purchase#:~:text=No%20Thanks,downloads" # TODO

class Free_ISO_Creator:

    Windows = "https://www.softsea.com/download/Free-ISO-Creator.html" # TODO

