import threading

import wx
import os
import sys
import json
import datetime
import time
from machineScript import *

conf = {}

with open(os.path.split(os.path.abspath(sys.argv[0]))[0] + '/config.json', 'r') as file:
    conf = json.load(file)


class NumPad(wx.Dialog):
    """
    A class that creates a number pad dialog for entering numbers into a wx.TextCtrl
    """
    def __init__(self, parent, text):
        wx.Dialog.__init__(self, parent)

        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.parent = parent
        self.text = text
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        self.value = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value=self.text.Value)
        self.btn1 = wx.Button(self, label="1")
        self.btn2 = wx.Button(self, label="2")
        self.btn3 = wx.Button(self, label="3")
        self.btn4 = wx.Button(self, label="4")
        self.btn5 = wx.Button(self, label="5")
        self.btn6 = wx.Button(self, label="6")
        self.btn7 = wx.Button(self, label="7")
        self.btn8 = wx.Button(self, label="8")
        self.btn9 = wx.Button(self, label="9")
        self.btnDel = wx.Button(self, label="⌫")
        self.btn0 = wx.Button(self, label="0")
        self.btnEnter = wx.Button(self, label="↵")

        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.value.SetFont(mainFont)

        self.btn1.SetFont(mainFont)
        self.btn2.SetFont(mainFont)
        self.btn3.SetFont(mainFont)
        self.btn4.SetFont(mainFont)
        self.btn5.SetFont(mainFont)
        self.btn6.SetFont(mainFont)
        self.btn7.SetFont(mainFont)
        self.btn8.SetFont(mainFont)
        self.btn9.SetFont(mainFont)
        self.btnDel.SetFont(mainFont)
        self.btn0.SetFont(mainFont)
        self.btnEnter.SetFont(mainFont)

        self.btn1.Bind(wx.EVT_BUTTON, self.onBtn1)
        self.btn2.Bind(wx.EVT_BUTTON, self.onBtn2)
        self.btn3.Bind(wx.EVT_BUTTON, self.onBtn3)
        self.btn4.Bind(wx.EVT_BUTTON, self.onBtn4)
        self.btn5.Bind(wx.EVT_BUTTON, self.onBtn5)
        self.btn6.Bind(wx.EVT_BUTTON, self.onBtn6)
        self.btn7.Bind(wx.EVT_BUTTON, self.onBtn7)
        self.btn8.Bind(wx.EVT_BUTTON, self.onBtn8)
        self.btn9.Bind(wx.EVT_BUTTON, self.onBtn9)
        self.btnDel.Bind(wx.EVT_BUTTON, self.onBtnDel)
        self.btn0.Bind(wx.EVT_BUTTON, self.onBtn0)
        self.btnEnter.Bind(wx.EVT_BUTTON, self.onBtnEnter)

        self.Bind(wx.EVT_LEAVE_WINDOW, self.onLeave)

    def DoLayout(self):
        vSizer = wx.BoxSizer(wx.VERTICAL)
        row1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        row2Sizer = wx.BoxSizer(wx.HORIZONTAL)
        row3Sizer = wx.BoxSizer(wx.HORIZONTAL)
        row4Sizer = wx.BoxSizer(wx.HORIZONTAL)

        vSizer.Add(self.value, 0, wx.EXPAND)

        row1Sizer.Add(self.btn1, 1)
        row1Sizer.Add(self.btn2, 1)
        row1Sizer.Add(self.btn3, 1)

        row2Sizer.Add(self.btn4, 1)
        row2Sizer.Add(self.btn5, 1)
        row2Sizer.Add(self.btn6, 1)

        row3Sizer.Add(self.btn7, 1)
        row3Sizer.Add(self.btn8, 1)
        row3Sizer.Add(self.btn9, 1)

        row4Sizer.Add(self.btnDel, 1)
        row4Sizer.Add(self.btn0, 1)
        row4Sizer.Add(self.btnEnter, 1)

        vSizer.Add(row1Sizer, 0, wx.EXPAND)
        vSizer.Add(row2Sizer, 0, wx.EXPAND)
        vSizer.Add(row3Sizer, 0, wx.EXPAND)
        vSizer.Add(row4Sizer, 0, wx.EXPAND)

        self.SetSizer(vSizer)

        if conf['ON_RASP_PI']:
            self.FitInside()
        else:
            self.Fit()

    def onBtn1(self, event):
        self.value.Value = self.value.Value + '1'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn2(self, event):
        self.value.Value = self.value.Value + '2'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn3(self, event):
        self.value.Value = self.value.Value + '3'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn4(self, event):
        self.value.Value = self.value.Value + '4'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn5(self, event):
        self.value.Value = self.value.Value + '5'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn6(self, event):
        self.value.Value = self.value.Value + '6'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn7(self, event):
        self.value.Value = self.value.Value + '7'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn8(self, event):
        self.value.Value = self.value.Value + '8'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtn9(self, event):
        self.value.Value = self.value.Value + '9'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtnDel(self, event):
        if len(self.value.Value) == 1:
            self.value.Value = '0'
        else:
            self.value.Value = self.value.Value[:-1]

    def onBtn0(self, event):
        self.value.Value = self.value.Value + '0'
        if self.value.Value[0] == '0':
            self.value.Value = self.value.Value[1:]

    def onBtnEnter(self, event):
        self.text.Value = self.value.Value
        self.Close()

    def onLeave(self, event):
        if conf['ON_RASP_PI']:
            self.Close()

    def setValue(self, value):
        self.value.Value = value

    def onClose(self, event):
        self.parent.parent.Enable()
        event.Skip()


class ManualTimeFill(wx.Dialog):
    """
    A class that holds a manual fill control dialog
    """
    def __init__(self, parent, text):
        wx.Dialog.__init__(self, parent, size=(800, 504))

        self.fillTime = 0
        self.start = 0

        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.parent = parent
        self.text = text
        self.CreateCtrls()
        self.DoLayout()

        if conf['ON_RASP_PI']:
            self.ShowFullScreen(True)


    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lStatus = wx.StaticText(self, label="Manual Fill\nStatus", style=wx.TE_CENTER)
        self.lStatus.SetFont(mediumFont)
        self.lStatus.SetBackgroundColour('goldenrod')

        self.tStatus = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_WORDWRAP, value="Ready")
        self.tStatus.SetFont(mainFont)

        self.saveExitBtn = wx.Button(self, label="Save Time\nand Exit")
        self.saveExitBtn.SetFont(mediumFont)
        self.saveExitBtn.Bind(wx.EVT_BUTTON, self.onSaveExitBtn)

        self.lowerBtn = wx.Button(self, label="Lower\nTool Heads")
        self.lowerBtn.SetFont(mediumFont)
        self.lowerBtn.Bind(wx.EVT_BUTTON, self.onLowerBtn)

        self.startFillBtn = wx.Button(self, label="Start Fill")
        self.startFillBtn.SetFont(mediumFont)
        self.startFillBtn.Bind(wx.EVT_BUTTON, self.onStartFillBtn)

        self.stopFillBtn = wx.Button(self, label="Stop Fill")
        self.stopFillBtn.SetFont(mediumFont)
        self.stopFillBtn.Bind(wx.EVT_BUTTON, self.onStopFillBtn)

        self.raiseBtn = wx.Button(self, label="Raise\nTool Heads")
        self.raiseBtn.SetFont(mediumFont)
        self.raiseBtn.Bind(wx.EVT_BUTTON, self.onRaiseBtn)

        self.indexBtn = wx.Button(self, label="Cycle Indexer")
        self.indexBtn.SetFont(mediumFont)
        self.indexBtn.Bind(wx.EVT_BUTTON, self.onIndexBtn)

        self.stopBtn = wx.Button(self, label="Stop All")
        self.stopBtn.SetBackgroundColour('red')
        self.stopBtn.SetFont(mediumFont)
        self.stopBtn.Bind(wx.EVT_BUTTON, self.onStopBtn)

        self.startFillBtn.Disable()
        self.stopFillBtn.Disable()
        self.raiseBtn.Disable()

    def DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizerL = wx.BoxSizer(wx.VERTICAL)
        vsizerM = wx.BoxSizer(wx.VERTICAL)
        vsizerR = wx.BoxSizer(wx.VERTICAL)

        vsizerL.Add(self.lStatus, 0, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.tStatus, 1, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.saveExitBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizerM.Add(self.lowerBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerM.Add(self.raiseBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerM.Add(self.indexBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizerR.Add(self.startFillBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.stopFillBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.stopBtn, 1, wx.EXPAND | wx.ALL, 5)

        hsizer.Add(vsizerL, 1, wx.EXPAND)
        hsizer.Add(vsizerM, 1, wx.EXPAND)
        hsizer.Add(vsizerR, 1, wx.EXPAND)

        self.SetSizer(hsizer)

    def onSaveExitBtn(self, event):
        self.text.Value = str(round(1000 * self.fillTime))
        self.fillTime = 0
        self.tStatus.SetValue("Ready")
        self.Close()

    def onLowerBtn(self, event):
        self.lStatus.SetBackgroundColour('green')
        self.parent.parent.parent.machine.setFault(0)
        self.saveExitBtn.Disable()
        self.lowerBtn.Disable()
        self.indexBtn.Disable()
        self.tStatus.SetValue("Began lowering fill heads\n\n" + self.tStatus.GetValue())
        self.lowerThread = threading.Thread(target=self.manLower)
        self.lowerThread.start()

    def onStartFillBtn(self, event):
        self.startFillBtn.Disable()
        self.stopFillBtn.Enable()
        self.raiseBtn.Disable()
        self.start = time.time()

        if self.parent.parent.parent.machine.wine1sw.getState():
            self.parent.parent.parent.machine.openWine1()
            self.tStatus.SetValue("Began filling\n\n" + self.tStatus.GetValue())
        else:
            self.lStatus.SetBackgroundColour('goldenrod')
            self.parent.parent.parent.machine.setFault(1)
            self.tStatus.SetValue("Wine 1 missing pouch\n\n" + self.tStatus.GetValue())

        if self.parent.parent.parent.machine.wine2sw.getState():
            self.parent.parent.parent.machine.openWine2()
            self.tStatus.SetValue("Began filling\n\n" + self.tStatus.GetValue())
        else:
            self.lStatus.SetBackgroundColour('goldenrod')
            self.parent.parent.parent.machine.setFault(1)
            self.tStatus.SetValue("Wine 2 missing pouch\n\n" + self.tStatus.GetValue())

    def onStopFillBtn(self, event):
        self.startFillBtn.Enable()
        self.stopFillBtn.Disable()
        self.raiseBtn.Enable()
        self.parent.parent.parent.machine.closeWine1()
        self.parent.parent.parent.machine.closeWine2()
        self.lStatus.SetBackgroundColour('green')
        self.parent.parent.parent.machine.setFault(0)
        self.fillTime += time.time() - self.start
        self.tStatus.SetValue("Recorded fill time of " + str(round(1000 * self.fillTime)) + " ms\n\n" + self.tStatus.GetValue())

    def onRaiseBtn(self, event):
        self.startFillBtn.Disable()
        self.raiseBtn.Disable()
        self.tStatus.SetValue("Began raising fill heads\n\n" + self.tStatus.GetValue())
        self.raiseThread = threading.Thread(target=self.manRaise)
        self.raiseThread.start()


    def onIndexBtn(self, event):
        self.parent.parent.parent.machine.moveIndexer(conf["INDEX_TIME"])
        self.tStatus.SetValue("Moving indexer\n\n" + self.tStatus.GetValue())

    def onStopBtn(self, event):
        self.parent.parent.parent.machine.shutoff()
        self.lStatus.SetBackgroundColour('red')
        self.parent.parent.parent.machine.setFault(2)
        self.tStatus.SetValue("Emergency Stop\n\n" + self.tStatus.GetValue())

    def onClose(self, event):
        self.parent.parent.Enable()
        event.Skip()

    def manLower(self):
        self.parent.parent.parent.machine.wineMotor.down(conf["LOWER_TIME"], conf["PUL_DELAY"])
        self.startFillBtn.Enable()
        self.raiseBtn.Enable()
        self.tStatus.SetValue("Fill heads lowered\n\n" + self.tStatus.GetValue())


    def manRaise(self):
        self.parent.parent.parent.machine.wineMotor.up(conf["LOWER_TIME"], conf["PUL_DELAY"])
        self.saveExitBtn.Enable()
        self.lowerBtn.Enable()
        self.indexBtn.Enable()
        self.tStatus.SetValue("Fill heads raised\n\n" + self.tStatus.GetValue())
        self.lStatus.SetBackgroundColour('goldenrod')


class SetUpTab(wx.Panel):
    """
    A class that holds the setup panel
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lPouchSize = wx.StaticText(self, label="Select Pouch Size")
        self.lPouchSize.SetFont(mainFont)

        self.btn750 = wx.Button(self, label="750mL")
        self.btn750.SetBackgroundColour('lime green')
        self.btn750.SetFont(mediumFont)
        self.btn750.Bind(wx.EVT_BUTTON, self.onBtn750)

        self.btn1500 = wx.Button(self, label="1.5L")
        self.btn1500.SetBackgroundColour('grey')
        self.btn1500.SetFont(mediumFont)
        self.btn1500.Bind(wx.EVT_BUTTON, self.onBtn1500)

        self.saveBtn = wx.Button(self, label="Save Profile")
        self.saveBtn.SetFont(mediumFont)
        self.saveBtn.Bind(wx.EVT_BUTTON, self.onSaveBtn)

        self.loadBtn = wx.Button(self, label="Load Profile")
        self.loadBtn.SetFont(mediumFont)
        self.loadBtn.Bind(wx.EVT_BUTTON, self.onLoadBtn)

    def DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(self.lPouchSize, 0, wx.CENTER)

        hsizer1.Add(self.btn750, 1, wx.EXPAND | wx.ALL, 5)
        hsizer1.Add(self.btn1500, 1, wx.EXPAND | wx.ALL, 5)

        hsizer2.Add(self.saveBtn, 1, wx.EXPAND | wx.ALL, 5)
        hsizer2.Add(self.loadBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizer.Add(hsizer1, 2, wx.EXPAND)
        vsizer.Add(hsizer2, 1, wx.EXPAND)

        self.SetSizer(vsizer)

    def onBtn750(self, event):
        self.setVolume(750)

    def onBtn1500(self, event):
        self.setVolume(1500)

    def onSaveBtn(self, event):
        fileName = str(datetime.datetime.now()).replace(':', '').replace(' ', '_')[:-7] + ".evgp"
        with open(self.parent.parent.parent.parent.installDir + "/Profiles/" + fileName, 'w') as profile:
            profile.write(str(self.parent.parent.rate))

            profile.close()

    def onLoadBtn(self, event):
        with wx.FileDialog(self, "Open saved profile", wildcard="EVGP files (*.evgp)|*.evgp") as fileDialog:
            fileDialog.SetDirectory(self.parent.parent.parent.parent.installDir + "/Profiles")
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as profile:
                    self.parent.parent.rate = float(profile.read())
                    self.setVolume(self.parent.parent.selection)
            except IOError:
                wx.LogError("Cannot open file")

    def setVolume(self, vol):
        self.parent.parent.selection = vol

        if vol == 750:
            self.btn1500.SetBackgroundColour('grey')
            self.btn750.SetBackgroundColour('lime green')
        else:
            self.btn750.SetBackgroundColour('grey')
            self.btn1500.SetBackgroundColour('lime green')

        self.parent.parent.calTab.tTime.Value = str(int(self.parent.parent.selection / self.parent.parent.rate))
        self.parent.parent.calTab.tVol.Value = str(self.parent.parent.selection)


class CalTab(wx.Panel):
    """
    A class that holds the calibration panel
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lTime = wx.StaticText(self, label="Fill Time (ms)", style=wx.TE_CENTER)
        self.lTime.SetFont(mainFont)

        self.tTime = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value=str(int(self.parent.parent.selection / self.parent.parent.rate)))
        self.tTime.SetFont(largeFont)

        self.enterTimeBtn = wx.Button(self, label="Enter Time")
        self.enterTimeBtn.SetFont(mediumFont)

        self.timeNumPad = NumPad(self, self.tTime)
        self.enterTimeBtn.Bind(wx.EVT_BUTTON, self.onEnterTimeBtn)

        self.manualTimeBtn = wx.Button(self, label="Manual Time Fill")
        self.manualTimeBtn.SetFont(mediumFont)

        self.manualTimeFill = ManualTimeFill(self, self.tTime)
        self.manualTimeBtn.Bind(wx.EVT_BUTTON, self.onManualTimeBtn)

        self.lVol = wx.StaticText(self, label="Volume (mL)", style=wx.TE_CENTER)
        self.lVol.SetFont(mainFont)

        self.tVol = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value=str(self.parent.parent.selection))
        self.tVol.SetFont(largeFont)

        self.enterVolBtn = wx.Button(self, label="Enter Volume")
        self.enterVolBtn.SetFont(mediumFont)

        self.volNumPad = NumPad(self, self.tVol)
        self.enterVolBtn.Bind(wx.EVT_BUTTON, self.onEnterVolBtn)

        self.recalcBtn = wx.Button(self, label="Recalculate Time")
        self.recalcBtn.SetFont(mediumFont)
        self.recalcBtn.Bind(wx.EVT_BUTTON, self.onRecalcBtn)

    def DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizerL = wx.BoxSizer(wx.VERTICAL)
        vsizerR = wx.BoxSizer(wx.VERTICAL)

        vsizerL.Add(self.lTime, 0, wx.EXPAND | wx.TOP, 5)
        vsizerL.Add(self.tTime, 0, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.enterTimeBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.manualTimeBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizerR.Add(self.lVol, 0, wx.EXPAND | wx.TOP, 5)
        vsizerR.Add(self.tVol, 0, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.enterVolBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.recalcBtn, 1, wx.EXPAND | wx.ALL, 5)

        hsizer.Add(vsizerL, 1, wx.EXPAND)
        hsizer.Add(vsizerR, 1, wx.EXPAND)

        self.SetSizer(hsizer)

    def onEnterTimeBtn(self, event):
        self.timeNumPad.Show()
        self.timeNumPad.setValue(self.tTime.GetValue())
        self.parent.Disable()

    def onManualTimeBtn(self, event):
        self.manualTimeFill.Show()
        self.manualTimeFill.SetFocus()
        self.parent.Disable()

    def onEnterVolBtn(self, event):
        self.volNumPad.Show()
        self.volNumPad.setValue(self.tVol.GetValue())
        self.parent.Disable()

    def onRecalcBtn(self, event):

        oldTime = self.tTime.Value
        oldVol = self.tVol.Value
        pouchSize = self.parent.parent.selection

        newTime = int(oldTime) * pouchSize // int(oldVol)

        self.tTime.Value = str(newTime)
        self.tVol.Value = str(pouchSize)
        self.parent.parent.rate = int(oldVol) / int(oldTime)


class RunTab(wx.Panel):
    """
    A class that holds the run panel
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lStatus = wx.StaticText(self, label="Status", style=wx.TE_CENTER | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.lStatus.SetFont(mediumFont)
        self.lStatus.SetBackgroundColour('goldenrod')

        self.tStatus = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_WORDWRAP, value="Ready\n")
        self.tStatus.SetFont(mainFont)

        self.lFillCt = wx.StaticText(self, label="Pouches Filled:", style=wx.TE_CENTER)
        self.lFillCt.SetFont(mainFont)

        self.tFillCt = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_RIGHT, value="0")
        self.tFillCt.SetFont(mainFont)

        self.lAdjustCycles = wx.StaticText(self, label="# Cycles", style=wx.TE_CENTER | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.lAdjustCycles.SetFont(mediumFont)

        self.increaseCyclesBtn = wx.Button(self, label="+")
        self.increaseCyclesBtn.SetFont(largeFont)
        self.increaseCyclesBtn.Bind(wx.EVT_BUTTON, self.onIncreaseCyclesBtn)

        self.decreaseCyclesBtn = wx.Button(self, label="-")
        self.decreaseCyclesBtn.SetFont(largeFont)
        self.decreaseCyclesBtn.Bind(wx.EVT_BUTTON, self.onDecreaseCyclesBtn)

        self.tNumCycles = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_RIGHT, value=str(self.parent.parent.cycles))
        self.tNumCycles.SetFont(mediumFont)

        self.runBtn = wx.Button(self, label="Run")
        self.runBtn.SetBackgroundColour('lime green')
        self.runBtn.SetFont(mediumFont)
        self.runBtn.Bind(wx.EVT_BUTTON, self.onRunBtn)

        self.stopBtn = wx.Button(self, label="Stop")
        self.stopBtn.SetBackgroundColour('red')
        self.stopBtn.SetFont(mediumFont)
        self.stopBtn.Bind(wx.EVT_BUTTON, self.onStopBtn)

    def DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizerL = wx.BoxSizer(wx.VERTICAL)
        vsizerM = wx.BoxSizer(wx.VERTICAL)
        vsizerR = wx.BoxSizer(wx.VERTICAL)
        hsizerL = wx.BoxSizer(wx.HORIZONTAL)

        hsizerL.Add(self.lFillCt, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        hsizerL.Add(self.tFillCt, 1, wx.EXPAND)

        vsizerL.Add(self.lStatus, 0, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.tStatus, 1, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(hsizerL, 0, wx.EXPAND | wx.ALL, 5)

        vsizerM.Add(self.lAdjustCycles, 0, wx.EXPAND | wx.ALL, 5)
        vsizerM.Add(self.tNumCycles, 0, wx.EXPAND | wx.ALL, 5)
        vsizerM.Add(self.increaseCyclesBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerM.Add(self.decreaseCyclesBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizerR.Add(self.runBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.stopBtn, 1, wx.EXPAND | wx.ALL, 5)

        hsizer.Add(vsizerL, 1, wx.EXPAND)
        hsizer.Add(vsizerM, 0, wx.EXPAND)
        hsizer.Add(vsizerR, 1, wx.EXPAND)

        self.SetSizer(hsizer)

    def onRunBtn(self, event):
        self.parent.parent.Running = True
        self.runThread = threading.Thread(target=self.Run)
        self.runThread.start()
        self.lStatus.SetBackgroundColour('green')
        self.parent.parent.machine.setFault(0)
        self.tStatus.SetValue("Running\n\n" + self.tStatus.GetValue())


    def Run(self):
        for i in range(self.parent.parent.cycles):

            motorthread1 = threading.Thread(target=self.parent.parent.machine.n2Motor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))
            motorthread2 = threading.Thread(target=self.parent.parent.machine.wineMotor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))
            motorthread3 = threading.Thread(target=self.parent.parent.machine.cappingMotor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))

            motorthread1.start()
            motorthread2.start()
            motorthread3.start()

            time.sleep(conf["LOWER_TIME"])

            if not (self.parent.parent.machine.irLeft.getState() \
                    and not self.parent.parent.machine.irMid.getState() \
                    and self.parent.machine.irRight.getState()):

                self.parent.parent.machine.shutoff()
                self.lStatus.SetBackgroundColour('red')
                self.parent.parent.machine.setFault(2)
                self.tStatus.SetValue("Capping error stopped function\n\n" + self.tStatus.GetValue())

            else:

                if self.parent.parent.machine.n2sw.getState():
                    self.parent.parent.machine.puffN2()
                    self.tStatus.SetValue("Puffed N2\n\n" + self.tStatus.GetValue())
                else:
                    self.lStatus.SetBackgroundColour('goldenrod')
                    self.parent.parent.machine.setFault(1)
                    self.tStatus.SetValue("N2 missing pouch\n\n" + self.tStatus.GetValue())

                if self.parent.parent.machine.wine1sw.getState():
                    self.parent.parent.machine.openWine1()
                    self.tStatus.SetValue("Began filling\n\n" + self.tStatus.GetValue())
                else:
                    self.lStatus.SetBackgroundColour('goldenrod')
                    self.parent.parent.machine.setFault(1)
                    self.tStatus.SetValue("Wine 1 missing pouch\n\n" + self.tStatus.GetValue())

                if self.parent.parent.machine.wine2sw.getState():
                    self.parent.parent.machine.openWine2()
                    self.tStatus.SetValue("Began filling\n\n" + self.tStatus.GetValue())
                else:
                    self.lStatus.SetBackgroundColour('goldenrod')
                    self.parent.parent.machine.setFault(1)
                    self.tStatus.SetValue("Wine 2 missing pouch\n\n" + self.tStatus.GetValue())

                time.sleep(self.parent.parent.calTab.tTime / 1000)

                self.parent.parent.machine.closeWine1()
                self.parent.parent.machine.closeWine2()

                motorthread4 = threading.Thread(target=self.parent.parent.machine.n2Motor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))
                motorthread5 = threading.Thread(target=self.parent.parent.machine.wineMotor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))

                motorthread4.start()
                motorthread5.start()

                time.sleep(conf["LOWER_TIME"])

                self.parent.parent.machine.moveIndexer(conf["INDEX_TIME"])

                motorthread6 = threading.Thread(target=self.parent.parent.machine.cappingMotor.down(conf["LOWER_TIME"], conf["PUL_DELAY"]))

                motorthread6.start()

                time.sleep(conf["LOWER_TIME"])

        self.tStatus.SetValue("Running finished\n\n" + self.tStatus.GetValue())
        self.lStatus.SetBackgroundColour('goldenrod')


    def onStopBtn(self, event):
        self.parent.parent.machine.shutoff()
        self.lStatus.SetBackgroundColour('red')
        self.parent.parent.machine.setFault(2)
        self.tStatus.SetValue("Emergency Stop\n\n" + self.tStatus.GetValue())

    def onIncreaseCyclesBtn(self, event):
        self.parent.parent.cycles += 1
        self.tNumCycles.Value = str(self.parent.parent.cycles)

    def onDecreaseCyclesBtn(self, event):
        if self.parent.parent.cycles > 1:
            self.parent.parent.cycles -= 1
            self.tNumCycles.Value = str(self.parent.parent.cycles)


class EPCNotebook(wx.Notebook):
    """
    A notebook class for implementing parent items in notebook tabs
    """
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        self.parent = parent


class EPCPanel(wx.Panel):
    """
    A class for the main app panel and function
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.selection = 750
        self.rate = 1500 / 8500
        self.cycles = 1

        self.Running = False

        self.parent = parent

        self.machine = Machine(conf["GPIO"])

        self.CreateCtrls()
        self.DoLayout()

        self.setupTab.setVolume(750)

    def CreateCtrls(self):
        self.notebook = EPCNotebook(self)

        self.setupTab = SetUpTab(self.notebook)
        self.calTab = CalTab(self.notebook)
        self.runTab = RunTab(self.notebook)
        self.exitTab = wx.Panel(self.notebook)

        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.notebook.SetFont(mainFont)

        self.notebook.AddPage(self.setupTab, "       Setup      ")
        self.notebook.AddPage(self.calTab,   "    Calibration   ")
        self.notebook.AddPage(self.runTab,   "        Run       ")
        self.notebook.AddPage(self.exitTab,  " X ")

        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onTabChange)

    def DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()

    def onTabChange(self, event):
        if self.Running:
            self.notebook.ChangeSelection(2)
            self.runTab.tStatus.SetValue("Process running\nPlease wait to change tab\n\n"
                                         + self.runTab.tStatus.GetValue())
        elif event.GetSelection() == 3:
            wx.Exit()


class EPCFrame(wx.Frame):
    """
    A class that holds the main app frame (for window sizing)
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, None, -1, title, size=(800, 480))

        self.parent = parent
        self.CreateCtrls()

    def CreateCtrls(self):
        self.panel = EPCPanel(self)

        if conf['ON_RASP_PI']:
            self.ShowFullScreen(True)


class EPC(wx.App):
    """
    A class that holds the GUI App
    """
    def OnInit(self):

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.frame = EPCFrame(self, "Evergood Pi Control v1.0.0")
        self.SetTopWindow(self.frame)
        self.frame.Show(True)

        return True

    def GetInstallDir(self):
        return self.installDir

    def onClose(self):
        self.frame.panel.machine.cleanUp()


def main():

    app = EPC(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
