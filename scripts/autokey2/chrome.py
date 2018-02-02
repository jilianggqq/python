# Enter script code
if window.wait_for_exist('.*Google Chrome', 0) == True:
    window.activate('Google Chrome', switchDesktop=False, matchClass=False)
else:
    system.exec_command('/usr/bin/google-chrome', getOutput=True)
