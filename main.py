import wx
import os
import sys

class NumPad(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

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
        self.btnDel = wx.Button(self, label="Del")
        self.btn0 = wx.Button(self, label="0")
        self.btnEnter = wx.Button(self, label="Enter")

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

        vSizer.Add(row1Sizer, 1, wx.EXPAND)
        vSizer.Add(row2Sizer, 1, wx.EXPAND)
        vSizer.Add(row3Sizer, 1, wx.EXPAND)
        vSizer.Add(row4Sizer, 1, wx.EXPAND)

        self.SetSizer(vSizer)
        self.Fit()


class SetUpTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lPouchSize = wx.StaticText(self, label="Select Pouch Size")
        self.lPouchSize.SetFont(mainFont)
        self.btn750 = wx.ToggleButton(self, label="750mL", style=1)
        self.btn750.Bind(wx.EVT_TOGGLEBUTTON, self.onBtn750)


        self.btn1500 = wx.ToggleButton(self, label="1.5L", style=1)
        self.btn1500.Bind(wx.EVT_TOGGLEBUTTON, self.onBtn1500)


    def DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.lPouchSize, 0, wx.CENTER)
        hsizer.Add(self.btn750, 1, wx.EXPAND)
        hsizer.Add(self.btn1500, 1, wx.EXPAND)
        sizer.Add(hsizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()

    def onBtn750(self, event):
        self.btn1500.SetValue(False)

    def onBtn1500(self, event):
        self.btn750.SetValue(False)


class CalTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.CreateCtrls()
        self.DoLayout()

    def CreateCtrls(self):
        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        largeFont = wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lTime = wx.StaticText(self, label="Fill Time (ms)")
        self.lTime.SetFont(mainFont)

        self.tTime = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY, value="0")
        self.tTime.SetFont(largeFont)

        self.enterTimeBtn = wx.Button(self, label="Enter Time")
        self.enterTimeBtn.SetFont(mainFont)

        self.numPad = NumPad(self.tTime)
        self.enterTimeBtn.Bind(wx.EVT_BUTTON, self.onEnterTimeBtn)

    def DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lTime, 1, wx.CENTER)
        sizer.Add(self.tTime, 1, wx.EXPAND)
        sizer.Add(self.enterTimeBtn, 0)
        self.SetSizer(sizer)
        self.Fit()

    def onEnterTimeBtn(self, event):
        self.numPad.Show()


class RunTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20,20))


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

        mainFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.notebook.SetFont(mainFont)

        self.notebook.AddPage(self.setUpTab, "        Setup         ")
        self.notebook.AddPage(self.calTab,   "     Calibration      ")
        self.notebook.AddPage(self.runTab,   "         Run          ")

    def DoLayout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()



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
