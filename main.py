import wx
import os
import sys
import json

conf = {}

with open('config.json', 'r') as file:
    conf = json.load(file)


class NumPad(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        self.value = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value=self.parent.Value)
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
        self.parent.Value = self.value.Value
        self.Close()

    def onLeave(self, event):
        if conf['ON_RASP_PI']:
            self.Close()


class SetUpTab(wx.Panel):
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

        self.loadBtn = wx.Button(self, label="Load Profile")
        self.loadBtn.SetFont(mediumFont)
        self.loadBtn.Bind(wx.EVT_BUTTON, self.onLoadBtn)

        self.lastBtn = wx.Button(self, label="Load Last Used")
        self.lastBtn.SetFont(mediumFont)
        self.loadBtn.Bind(wx.EVT_BUTTON, self.onLastBtn)

        self.selection = '750mL'

    def DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(self.lPouchSize, 0, wx.CENTER)

        hsizer1.Add(self.btn750, 1, wx.EXPAND | wx.ALL, 5)
        hsizer1.Add(self.btn1500, 1, wx.EXPAND | wx.ALL, 5)

        hsizer2.Add(self.loadBtn, 1, wx.EXPAND | wx.ALL, 5)
        hsizer2.Add(self.lastBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizer.Add(hsizer1, 2, wx.EXPAND)
        vsizer.Add(hsizer2, 1, wx.EXPAND)

        self.SetSizer(vsizer)

    def onBtn750(self, event):
        self.btn1500.SetBackgroundColour('grey')
        self.btn750.SetBackgroundColour('lime green')
        self.selection = self.Label

    def onBtn1500(self, event):
        self.btn750.SetBackgroundColour('grey')
        self.btn1500.SetBackgroundColour('lime green')
        self.selection = self.Label

    def onLoadBtn(self, event):
        pass

    def onLastBtn(self, event):
        pass

class CalTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lTime = wx.StaticText(self, label="Fill Time (ms)")
        self.lTime.SetFont(mainFont)

        self.tTime = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value="0")
        self.tTime.SetFont(largeFont)

        self.enterTimeBtn = wx.Button(self, label="Enter Time")
        self.enterTimeBtn.SetFont(mediumFont)

        self.timeNumPad = NumPad(self.tTime)
        self.enterTimeBtn.Bind(wx.EVT_BUTTON, self.onEnterTimeBtn)

        self.saveBtn = wx.Button(self, label="Save Profile")
        self.saveBtn.SetFont(mediumFont)
        self.saveBtn.Bind(wx.EVT_BUTTON, self.onSaveBtn)

        self.lVol = wx.StaticText(self, label="Volume (mL)")
        self.lVol.SetFont(mainFont)

        self.tVol = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value="0")
        self.tVol.SetFont(largeFont)

        self.enterVolBtn = wx.Button(self, label="Enter Volume")
        self.enterVolBtn.SetFont(mediumFont)

        self.volNumPad = NumPad(self.tVol)
        self.enterVolBtn.Bind(wx.EVT_BUTTON, self.onEnterVolBtn)

        self.recalcBtn = wx.Button(self, label="Recalculate Time")
        self.recalcBtn.SetFont(mediumFont)
        self.recalcBtn.Bind(wx.EVT_BUTTON, self.onRecalcBtn)

    def DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizerL = wx.BoxSizer(wx.VERTICAL)
        vsizerR = wx.BoxSizer(wx.VERTICAL)

        vsizerL.Add(self.lTime, 0, wx.CENTER | wx.TOP, 5)
        vsizerL.Add(self.tTime, 0, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.enterTimeBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerL.Add(self.saveBtn, 1, wx.EXPAND | wx.ALL, 5)

        vsizerR.Add(self.lVol, 0, wx.CENTER | wx.TOP, 5)
        vsizerR.Add(self.tVol, 0, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.enterVolBtn, 1, wx.EXPAND | wx.ALL, 5)
        vsizerR.Add(self.recalcBtn, 1, wx.EXPAND | wx.ALL, 5)

        hsizer.Add(vsizerL, 1, wx.EXPAND)
        hsizer.Add(vsizerR, 1, wx.EXPAND)

        self.SetSizer(hsizer)

    def onEnterTimeBtn(self, event):
        self.timeNumPad.Show()

    def onSaveBtn(self, event):
        pass

    def onEnterVolBtn(self, event):
        self.volNumPad.Show()

    def onRecalcBtn(self, event):
        pass


class RunTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        mediumFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lStatus = wx.StaticText(self, label="Status", style=wx.TE_CENTER)
        self.lStatus.SetFont(mediumFont)
        self.lStatus.SetBackgroundColour('goldenrod')

        self.tStatus = wx.TextCtrl(self, style=wx.TE_READONLY, value="READY")
        self.tStatus.SetFont(mainFont)

        self.lFillCt = wx.StaticText(self, label="Pouches Filled:", style=wx.TE_CENTER)
        self.lFillCt.SetFont(mainFont)

        self.tFillCt = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_RIGHT, value="0")
        self.tFillCt.SetFont(mainFont)

        self.runBtn = wx.Button(self, label="Run")
        self.runBtn.SetBackgroundColour('lime green')
        self.runBtn.SetFont(mediumFont)

        self.stopBtn = wx.Button(self, label="Stop")
        self.stopBtn.SetBackgroundColour('red')
        self.stopBtn.SetFont(mediumFont)

    def DoLayout(self):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizerL = wx.BoxSizer(wx.VERTICAL)
        vsizerR = wx.BoxSizer(wx.VERTICAL)
        hsizerL = wx.BoxSizer(wx.HORIZONTAL)

        hsizerL.Add(self.lFillCt, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        hsizerL.Add(self.tFillCt, 1, wx.EXPAND)

        vsizerL.Add(self.lStatus, 0, wx.EXPAND)
        vsizerL.Add(self.tStatus, 1, wx.EXPAND)
        vsizerL.Add(hsizerL, 0, wx.EXPAND)

        vsizerR.Add(self.runBtn, 1, wx.EXPAND)
        vsizerR.Add(self.stopBtn, 1, wx.EXPAND)

        hsizer.Add(vsizerL, 1, wx.EXPAND)
        hsizer.Add(vsizerR, 1, wx.EXPAND)

        self.SetSizer(hsizer)


class EPCNotebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        self.parent = parent


class EPCOptionsBox(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        self.notebook = EPCNotebook(self)

        self.setUpTab = SetUpTab(self.notebook)
        self.calTab = CalTab(self.notebook)
        self.runTab = RunTab(self.notebook)
        self.exitTab = wx.Panel(self.notebook)

        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.notebook.SetFont(mainFont)

        self.notebook.AddPage(self.setUpTab, "       Setup      ")
        self.notebook.AddPage(self.calTab,   "    Calibration   ")
        self.notebook.AddPage(self.runTab,   "        Run       ")
        self.notebook.AddPage(self.exitTab,  " X ")

        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onExitTab)

    def DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()

    def onExitTab(self, event):
        if event.GetSelection() == 3:
            wx.Exit()


class EPCPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):

        self.options = EPCOptionsBox(self)

    def DoLayout(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.options, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()

class EPCFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, -1, title, size=(800, 480))

        self.CreateCtrls()

    def CreateCtrls(self):
        self.panel = EPCPanel(self)

        if conf['ON_RASP_PI']:
            self.ShowFullScreen(True)


class EPC(wx.App):
    def OnInit(self):

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

        frame = EPCFrame("Evergood Pi Control v0.0.1")
        self.SetTopWindow(frame)
        frame.Show(True)

        return True

    def GetInstallDir(self):
        return self.installDir


def main():

    app = EPC(False)
    app.MainLoop()

if __name__ == '__main__':
    main()
