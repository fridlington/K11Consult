# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ConsultFrame
###########################################################################

class ConsultFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"T124RAR Live Data Stream", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		boxSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1 = wx.FlexGridSizer( 7, 2, 0, 0 )
		flexGrid1.SetFlexibleDirection( wx.BOTH )
		flexGrid1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.mphLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"MPH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mphLabel.Wrap( -1 )
		self.mphLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.mphLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.mphLabel, 0, wx.ALL, 5 )
		
		self.mphGauge = wx.Gauge( self.panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.mphGauge.SetValue( 0 ) 
		self.mphGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.mphGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.rpmLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"RMP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rpmLabel.Wrap( -1 )
		self.rpmLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.rpmLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.rpmLabel, 0, wx.ALL, 5 )
		
		self.rpmGauge = wx.Gauge( self.panel1, wx.ID_ANY, 7500, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.rpmGauge.SetValue( 0 ) 
		self.rpmGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.rpmGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.tempLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"Temp:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempLabel.Wrap( -1 )
		self.tempLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.tempLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.tempLabel, 0, wx.ALL, 5 )
		
		self.tempGauge = wx.Gauge( self.panel1, wx.ID_ANY, 160, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.tempGauge.SetValue( 0 ) 
		self.tempGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.tempGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.batLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"Battery:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.batLabel.Wrap( -1 )
		self.batLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.batLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.batLabel, 0, wx.ALL, 5 )
		
		self.batGauge = wx.Gauge( self.panel1, wx.ID_ANY, 16, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.batGauge.SetValue( 0 ) 
		self.batGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.batGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.mafLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"MAF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mafLabel.Wrap( -1 )
		self.mafLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.mafLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.mafLabel, 0, wx.ALL, 5 )
		
		self.mafGauge = wx.Gauge( self.panel1, wx.ID_ANY, 4000, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.mafGauge.SetValue( 0 ) 
		self.mafGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.mafGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.aacLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"AAC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aacLabel.Wrap( -1 )
		self.aacLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.aacLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.aacLabel, 0, wx.ALL, 5 )
		
		self.aacGauge = wx.Gauge( self.panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.aacGauge.SetValue( 0 ) 
		self.aacGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.aacGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.injectionLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"Injection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.injectionLabel.Wrap( -1 )
		self.injectionLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.injectionLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.injectionLabel, 0, wx.ALL, 5 )
		
		self.injectionGauge = wx.Gauge( self.panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.injectionGauge.SetValue( 0 ) 
		self.injectionGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.injectionGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.timingLabel = wx.StaticText( self.panel1, wx.ID_ANY, u"Timing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.timingLabel.Wrap( -1 )
		self.timingLabel.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		self.timingLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		flexGrid1.Add( self.timingLabel, 0, wx.ALL, 5 )
		
		self.timingGauge = wx.Gauge( self.panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.timingGauge.SetValue( 0 ) 
		self.timingGauge.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.timingGauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.labelSpacer = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), wx.LI_HORIZONTAL )
		self.labelSpacer.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.labelSpacer, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.gaugeSpacer = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1600,-1 ), wx.LI_HORIZONTAL )
		self.gaugeSpacer.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		flexGrid1.Add( self.gaugeSpacer, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel1.SetSizer( flexGrid1 )
		self.panel1.Layout()
		flexGrid1.Fit( self.panel1 )
		boxSizer1.Add( self.panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.startData = wx.Button( self.m_panel2, wx.ID_ANY, u"Start Stream", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.startData, 0, wx.ALL, 5 )
		
		self.stopData = wx.Button( self.m_panel2, wx.ID_ANY, u"Stop Stream", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stopData.Enable( False )
		
		bSizer3.Add( self.stopData, 0, wx.ALL, 5 )
		
		self.toggleButton1 = wx.ToggleButton( self.m_panel2, wx.ID_ANY, u"Start Thread", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.toggleButton1, 0, wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		boxSizer1.Add( self.m_panel2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( boxSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.startData.Bind( wx.EVT_BUTTON, self.startStream )
		self.stopData.Bind( wx.EVT_BUTTON, self.stopStream )
		self.toggleButton1.Bind( wx.EVT_TOGGLEBUTTON, self.toggleButton1Method )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def startStream( self, event ):
		event.Skip()
	
	def stopStream( self, event ):
		event.Skip()
	
	def toggleButton1Method( self, event ):
		event.Skip()
	

