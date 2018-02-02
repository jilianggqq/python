# Enter script code
if window.wait_for_exist('.*— Atom', 0) == True:
    window.activate('Atom', switchDesktop=False, matchClass=False)
else:
    system.exec_command('/usr/bin/atom', getOutput=True)
