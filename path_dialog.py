#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Nov  4 00:40:19 2010

#    This file is part of wxpymaps.
#
#    wxpymaps is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wxpymaps is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with wxpymaps.  If not, see <http://www.gnu.org/licenses/>.

import wx

# begin wxGlade: extracode
# end wxGlade



class PathDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: newMarkerDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.grid_sizer_1_staticbox = wx.StaticBox(self, -1, "")
        #self.coordinates = wx.TextCtrl(self, -1, "")
        self.name = wx.TextCtrl(self, -1, "")
        self.description = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_RICH)
        self.ID_NEWPATH = wx.NewId()
        self.Ok = wx.Button(self, self.ID_NEWPATH,"Ok")
        self.__set_properties()
        self.__do_layout()
        # end wxGlade


    def __set_properties(self):
        # begin wxGlade: newMarkerDialog.__set_properties
        self.SetTitle("dialog_5")
        #self.coordinates.SetMinSize((300, 27))
        self.name.SetMinSize((300, 27))
        self.description.SetMinSize((300, 300))
        self.Ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: newMarkerDialog.__do_layout
        grid_sizer_1 = wx.StaticBoxSizer(self.grid_sizer_1_staticbox, wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        #Coordinates = wx.StaticText(self, -1, "Coordinates")
        #grid_sizer_1.Add(Coordinates, 0, 0, 0)
        #grid_sizer_1.Add(self.coordinates, 0, 0, 0)
        Name = wx.StaticText(self, -1, "Name")
        grid_sizer_1.Add(Name, 0, 0, 0)
        grid_sizer_1.Add(self.name, 0, 0, 0)
        label_1 = wx.StaticText(self, -1, "Description")
        grid_sizer_1.Add(label_1, 0, 0, 0)
        grid_sizer_1.Add(self.description, 0, 0, 8)
        sizer_1.Add(self.Ok, 0, 0, 0)
        grid_sizer_1.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class newMarkerDialog



if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_2 = PathDialog(None, -1, "")
    app.SetTopWindow(dialog_2)
    dialog_2.Show()
    app.MainLoop()
