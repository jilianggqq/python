# Enter script code
if window.wait_for_exist('.*- VLC media player', 0) == True:
    window.activate('vlc.vlc', switchDesktop=False, matchClass=True)
else:
    system.exec_command('/usr/bin/vlc', getOutput=True)
