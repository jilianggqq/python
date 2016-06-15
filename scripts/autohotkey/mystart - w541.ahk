; 1、启动total commander
#t::
DetectHiddenWindows, on
IfWinNotExist ahk_class TTOTAL_CMD
	run,d:\green\TotalCMD64\Totalcmd64.exe
Else
	IfWinNotActive ahk_class TTOTAL_CMD
		WinActivate
Else
	WinMinimize
DetectHiddenWindows, off
Return

; 2. youdao dictionary
#u::
IfWinNotExist, ahk_class YodaoMainWndClass
	run, d:\Program Files\Dict\YodaoDict.exe
Else
	IfWinNotActive ahk_class YodaoMainWndClass
	WinActivate
Else
	Winminimize
Return

; 3. emeditor
#n::
IfWinNotExist, ahk_class EmEditorMainFrame3
	run,d:\green\EmEditor14\EmEditor.exe
Else
	IfWinNotActive ahk_class EmEditorMainFrame3
	WinActivate
Else
	Winminimize
Return

; 3. notepad ++
;#n::
;IfWinNotExist, ahk_class Notepad++
;	run,c:\Green\npp.6.8.1.bin\notepad++.exe
;Else
;	IfWinNotActive ahk_class Notepad++
;	WinActivate
;Else
;	Winminimize
;Return


; 4、启动chrome。
#c::
IfWinNotExist ahk_class Chrome_WidgetWin_1
	run, C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
Else
	IfWinNotActive ahk_class Chrome_WidgetWin_1
		WinActivate
Else
	WinMinimize
Return


; 5、sublime text。
#s::
IfWinNotExist ahk_class PX_WINDOW_CLASS
	run, c:\Program Files\Sublime Text 3\sublime_text.exe
Else
	IfWinNotActive ahk_class PX_WINDOW_CLASS
		WinActivate
Else
	WinMinimize
Return


; 6、qq
#q::
IfWinNotActive, ahk_class TXGuiFoundation
{
	WinActivate, ahk_class TXGuiFoundation
}
Else
{
	WinMinimize, ahk_class TXGuiFoundation
}
Return

; 7、power shell
#p::
IfWinNotActive, ahk_class ConsoleWindowClass
{
	WinActivate, ahk_class ConsoleWindowClass
}
Else
{
	WinMinimize, ahk_class ConsoleWindowClass
}
Return

; (1)if chrome is activeted, define some shortcuts
#IfWinActive, ahk_class Chrome_WidgetWin_1
f2::Send ^{PgUp}
f3::Send ^{PgDn}
f1::Send !d
!q::Send ^w
#IfWinActive

; (2)if qq is being activated, do some hotkey.
#IfWinActive, ahk_class TXGuiFoundation
Tab::Send ^+{Tab}
#IfWinActive

; (3)disable win+c(for touch pad)
; #c::return