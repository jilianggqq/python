# Enter script code
if window.wait_for_exist('gqq@gqq-W541: ~', 0) == True:
    window.activate('gqq@gqq-W541: ~', switchDesktop=False, matchClass=False)
    # dialog.info_dialog("test1")
# else:
    # system.exec_command('/usr/bin/google-chrome', getOutput=True)
    # dialog.info_dialog("test2")
    # x-terminal-emulator.X-terminal-emulator

# if window.wait_for_exist('x-terminal-emulator.X-terminal-emulator', 0) == True:
#     window.activate('x-terminal-emulator.X-terminal-emulator', switchDesktop=False, matchClass=False)
