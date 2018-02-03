# Enter script code
if window.wait_for_exist('.*— Atom', 0) == True:
    window.activate('atom.Atom', switchDesktop=False, matchClass=True)
else:
    system.exec_command('/usr/bin/atom', getOutput=True)
