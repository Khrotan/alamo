# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final.ui'
#
# Created: Thu Sep 11 22:40:56 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

import subprocess
import os
from subprocess import PIPE,Popen,check_output
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

pswd=str()
def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]
def getDriveNames():
	stdout = Popen("find /dev/disk/ -ls | grep /usb", shell=True, stdout=PIPE).stdout
	output = stdout.read()
	output = str(output)
	devices = list()
	output = output + ("\n")
	many = output.count("\n")
	def deviceAppend(output,devices):
	    start = output.find("/usb-")
	    end = output.find("->")
	    devices.append(output[start+5:end-1])
	    start = output.find("../../")
	    end = output.find("\n")
	    devices.append(output[start+6:end])
	for i in range(many):
	    deviceAppend(output,devices)
	    output = output[output.find("\n")+1:]

	driveNames=devices[:-2:2]
	return driveNames

def getPartitionPoints():
	stdout = Popen("find /dev/disk/ -ls | grep /usb", shell=True, stdout=PIPE).stdout
	output = stdout.read()
	output = str(output)
	devices = list()
	output = output + ("\n")
	many = output.count("\n")
	def deviceAppend(output,devices):
	    start = output.find("/usb-")
	    end = output.find("->")
	    devices.append(output[start+5:end-1])
	    start = output.find("../../")
	    end = output.find("\n")
	    devices.append(output[start+6:end])
	for i in range(many):
	    deviceAppend(output,devices)
	    output = output[output.find("\n")+1:]
	partitionPoints=devices[1:-2:2]
	return partitionPoints

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(957, 783)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 911, 231))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
	self.treeWidget.setHeaderLabels(["Partition","Label","Capacity","Free Space","Mounted or Not","Connection Point","Usage","Type","Name","Permission","Connection Point Permission"])
        self.buttons_frame = QtGui.QFrame(self.centralwidget)
        self.buttons_frame.setGeometry(QtCore.QRect(20, 300, 911, 111))
        self.buttons_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.buttons_frame.setObjectName(_fromUtf8("buttons_frame"))
        self.buttons_splitter = QtGui.QSplitter(self.buttons_frame)
        self.buttons_splitter.setGeometry(QtCore.QRect(10, 10, 891, 91))
        self.buttons_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_splitter.setObjectName(_fromUtf8("buttons_splitter"))
        self.updateTree_button = QtGui.QToolButton(self.buttons_splitter)
        self.updateTree_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Actions-edit-redo-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateTree_button.setIcon(icon)
        self.updateTree_button.setIconSize(QtCore.QSize(64, 64))
        self.updateTree_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.updateTree_button.setObjectName(_fromUtf8("updateTree_button"))
        self.checkForBadBlocks_button = QtGui.QToolButton(self.buttons_splitter)
        self.checkForBadBlocks_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/document-application-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkForBadBlocks_button.setIcon(icon1)
        self.checkForBadBlocks_button.setIconSize(QtCore.QSize(64, 64))
        self.checkForBadBlocks_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.checkForBadBlocks_button.setObjectName(_fromUtf8("checkForBadBlocks_button"))
        self.format_button = QtGui.QToolButton(self.buttons_splitter)
        self.format_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Delete-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.format_button.setIcon(icon2)
        self.format_button.setIconSize(QtCore.QSize(64, 64))
        self.format_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.format_button.setObjectName(_fromUtf8("format_button"))


        self.permission_button = QtGui.QToolButton(self.buttons_splitter)
        self.permission_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Actions-im-ban-user-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.permission_button.setIcon(icon2)
        self.permission_button.setIconSize(QtCore.QSize(64, 64))
        self.permission_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.permission_button.setObjectName(_fromUtf8("permission_button"))


        self.mount_button = QtGui.QToolButton(self.buttons_splitter)
        self.mount_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/1410400946_usbpendrive_mount.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mount_button.setIcon(icon3)
        self.mount_button.setIconSize(QtCore.QSize(64, 64))
        self.mount_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mount_button.setObjectName(_fromUtf8("mount_button"))
        self.unmount_button = QtGui.QToolButton(self.buttons_splitter)
        self.unmount_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/1410400946_usbpendrive_UNmount.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unmount_button.setIcon(icon4)
        self.unmount_button.setIconSize(QtCore.QSize(64, 64))
        self.unmount_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.unmount_button.setObjectName(_fromUtf8("unmount_button"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 430, 911, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.backup_tab = QtGui.QWidget()
        self.backup_tab.setStatusTip(_fromUtf8(""))
        self.backup_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backup_tab.setObjectName(_fromUtf8("backup_tab"))
        self.backupToISO_tab = QtGui.QFrame(self.backup_tab)
        self.backupToISO_tab.setGeometry(QtCore.QRect(20, 20, 861, 101))
        self.backupToISO_tab.setFrameShape(QtGui.QFrame.StyledPanel)
        self.backupToISO_tab.setFrameShadow(QtGui.QFrame.Raised)
        self.backupToISO_tab.setObjectName(_fromUtf8("backupToISO_tab"))
        self.layoutWidget_4 = QtGui.QWidget(self.backupToISO_tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.backupToISO_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.backupToISO_verticalLayout.setMargin(0)
        self.backupToISO_verticalLayout.setObjectName(_fromUtf8("backupToISO_verticalLayout"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.backupToISO_lineEdit = QtGui.QLineEdit(self.layoutWidget_4)
        self.backupToISO_lineEdit.setObjectName(_fromUtf8("backupToISO_lineEdit"))
        self.horizontalLayout_12.addWidget(self.backupToISO_lineEdit)
        self.backupToISO_selectTool = QtGui.QToolButton(self.layoutWidget_4)
        self.backupToISO_selectTool.setToolTip(_fromUtf8(""))
        self.backupToISO_selectTool.setStatusTip(_fromUtf8(""))
        self.backupToISO_selectTool.setWhatsThis(_fromUtf8(""))
        self.backupToISO_selectTool.setAutoFillBackground(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Apps-File-Iso-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backupToISO_selectTool.setIcon(icon5)
        self.backupToISO_selectTool.setObjectName(_fromUtf8("backupToISO_selectTool"))
        self.horizontalLayout_12.addWidget(self.backupToISO_selectTool)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.backupToISO_actionTool = QtGui.QToolButton(self.layoutWidget_4)
        self.backupToISO_actionTool.setObjectName(_fromUtf8("backupToISO_actionTool"))
        self.horizontalLayout_11.addWidget(self.backupToISO_actionTool)
        self.backupToISO_verticalLayout.addLayout(self.horizontalLayout_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backupToFolder_frame = QtGui.QFrame(self.backup_tab)
        self.backupToFolder_frame.setGeometry(QtCore.QRect(20, 160, 861, 101))
        self.backupToFolder_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.backupToFolder_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.backupToFolder_frame.setObjectName(_fromUtf8("backupToFolder_frame"))
        self.layoutWidget_6 = QtGui.QWidget(self.backupToFolder_frame)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.backupToFoler_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.backupToFoler_verticalLayout.setMargin(0)
        self.backupToFoler_verticalLayout.setObjectName(_fromUtf8("backupToFoler_verticalLayout"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.backupToFolder_lineEdit = QtGui.QLineEdit(self.layoutWidget_6)
        self.backupToFolder_lineEdit.setObjectName(_fromUtf8("backupToFolder_lineEdit"))
        self.horizontalLayout_16.addWidget(self.backupToFolder_lineEdit)
        self.backupToFolder_selectTool = QtGui.QToolButton(self.layoutWidget_6)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Folder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon98 = QtGui.QIcon()
        icon98.addPixmap(QtGui.QPixmap(_fromUtf8(":/cd-rom-driver-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backupToFolder_selectTool.setIcon(icon6)
        self.backupToFolder_selectTool.setObjectName(_fromUtf8("backupToFolder_selectTool"))
        self.horizontalLayout_16.addWidget(self.backupToFolder_selectTool)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.backupToFolder_actionTool = QtGui.QToolButton(self.layoutWidget_6)
        self.backupToFolder_actionTool.setObjectName(_fromUtf8("backupToFolder_actionTool"))
        self.horizontalLayout_15.addWidget(self.backupToFolder_actionTool)
        self.backupToFoler_verticalLayout.addLayout(self.horizontalLayout_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.addTab(self.backup_tab, _fromUtf8(""))
        self.restoreFromFolder_tab = QtGui.QWidget()
        self.restoreFromFolder_tab.setObjectName(_fromUtf8("restoreFromFolder_tab"))
        self.restoreFromISO_Frame = QtGui.QFrame(self.restoreFromFolder_tab)
        self.restoreFromISO_Frame.setGeometry(QtCore.QRect(20, 20, 861, 101))
        self.restoreFromISO_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.restoreFromISO_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.restoreFromISO_Frame.setObjectName(_fromUtf8("restoreFromISO_Frame"))
        self.layoutWidget = QtGui.QWidget(self.restoreFromISO_Frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.restoreFromISO_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.restoreFromISO_verticalLayout.setMargin(0)
        self.restoreFromISO_verticalLayout.setObjectName(_fromUtf8("restoreFromISO_verticalLayout"))
        self.restoreFromISO_horizantalLayout_ALL = QtGui.QHBoxLayout()
        self.restoreFromISO_horizantalLayout_ALL.setObjectName(_fromUtf8("restoreFromISO_horizantalLayout_ALL"))
        self.restoreFromISO_horizantalLayout_select = QtGui.QHBoxLayout()
        self.restoreFromISO_horizantalLayout_select.setObjectName(_fromUtf8("restoreFromISO_horizantalLayout_select"))
        self.restoreFromISO_lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.restoreFromISO_lineEdit.setObjectName(_fromUtf8("restoreFromISO_lineEdit"))
        self.restoreFromISO_horizantalLayout_select.addWidget(self.restoreFromISO_lineEdit)
        self.restoreFromISO_selectTool = QtGui.QToolButton(self.layoutWidget)
        self.restoreFromISO_selectTool.setIcon(icon5)
        self.restoreFromISO_selectTool.setObjectName(_fromUtf8("restoreFromISO_selectTool"))
        self.restoreFromISO_horizantalLayout_select.addWidget(self.restoreFromISO_selectTool)
        self.restoreFromISO_horizantalLayout_ALL.addLayout(self.restoreFromISO_horizantalLayout_select)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.restoreFromISO_horizantalLayout_ALL.addItem(spacerItem2)
        self.restoreFromISO_actionTool = QtGui.QToolButton(self.layoutWidget)
        self.restoreFromISO_actionTool.setObjectName(_fromUtf8("restoreFromISO_actionTool"))
        self.restoreFromISO_horizantalLayout_ALL.addWidget(self.restoreFromISO_actionTool)
        self.restoreFromISO_verticalLayout.addLayout(self.restoreFromISO_horizantalLayout_ALL)
        self.restoreFromISO_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restoreFromISO_label.setFont(font)
        self.restoreFromISO_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.restoreFromISO_label.setObjectName(_fromUtf8("restoreFromISO_label"))
        self.restoreFromISO_verticalLayout.addWidget(self.restoreFromISO_label)
        self.restoreFromFolder_frame = QtGui.QFrame(self.restoreFromFolder_tab)
        self.restoreFromFolder_frame.setGeometry(QtCore.QRect(20, 160, 861, 101))
        self.restoreFromFolder_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.restoreFromFolder_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.restoreFromFolder_frame.setObjectName(_fromUtf8("restoreFromFolder_frame"))
        self.layoutWidget1 = QtGui.QWidget(self.restoreFromFolder_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.restoreFromFolder_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.restoreFromFolder_verticalLayout.setMargin(0)
        self.restoreFromFolder_verticalLayout.setObjectName(_fromUtf8("restoreFromFolder_verticalLayout"))
        self.restoreFromFolder_horizantalLayout_ALL = QtGui.QHBoxLayout()
        self.restoreFromFolder_horizantalLayout_ALL.setObjectName(_fromUtf8("restoreFromFolder_horizantalLayout_ALL"))
        self.restoreFromFolder_horizantalLayout_choose = QtGui.QHBoxLayout()
        self.restoreFromFolder_horizantalLayout_choose.setObjectName(_fromUtf8("restoreFromFolder_horizantalLayout_choose"))
        self.restoreFromFolder_lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.restoreFromFolder_lineEdit.setObjectName(_fromUtf8("restoreFromFolder_lineEdit"))
        self.restoreFromFolder_horizantalLayout_choose.addWidget(self.restoreFromFolder_lineEdit)
        self.restoreFromFolder_selectTool = QtGui.QToolButton(self.layoutWidget1)
        self.restoreFromFolder_selectTool.setIcon(icon6)
        self.restoreFromFolder_selectTool.setObjectName(_fromUtf8("restoreFromFolder_selectTool"))
        self.restoreFromFolder_horizantalLayout_choose.addWidget(self.restoreFromFolder_selectTool)
        self.restoreFromFolder_horizantalLayout_ALL.addLayout(self.restoreFromFolder_horizantalLayout_choose)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.restoreFromFolder_horizantalLayout_ALL.addItem(spacerItem3)
        self.restoreFromFolder_actionTool = QtGui.QToolButton(self.layoutWidget1)
        self.restoreFromFolder_actionTool.setObjectName(_fromUtf8("restoreFromFolder_actionTool"))
        self.restoreFromFolder_horizantalLayout_ALL.addWidget(self.restoreFromFolder_actionTool)
        self.restoreFromFolder_verticalLayout.addLayout(self.restoreFromFolder_horizantalLayout_ALL)
        self.restoreFromFolder_label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restoreFromFolder_label.setFont(font)
        self.restoreFromFolder_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.restoreFromFolder_label.setObjectName(_fromUtf8("restoreFromFolder_label"))
        self.restoreFromFolder_verticalLayout.addWidget(self.restoreFromFolder_label)
        self.tabWidget.addTab(self.restoreFromFolder_tab, _fromUtf8(""))
        self.makeBootable_tab = QtGui.QWidget()
        self.makeBootable_tab.setObjectName(_fromUtf8("makeBootable_tab"))
        self.makeBootableFromISO_frame = QtGui.QFrame(self.makeBootable_tab)
        self.makeBootableFromISO_frame.setGeometry(QtCore.QRect(20, 20, 861, 101))
        self.makeBootableFromISO_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.makeBootableFromISO_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.makeBootableFromISO_frame.setObjectName(_fromUtf8("makeBootableFromISO_frame"))
        self.layoutWidget_2 = QtGui.QWidget(self.makeBootableFromISO_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.makeBootableFromISO_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.makeBootableFromISO_verticalLayout.setMargin(0)
        self.makeBootableFromISO_verticalLayout.setObjectName(_fromUtf8("makeBootableFromISO_verticalLayout"))
        self.makeBootableFromISO_horizantalLayout_ALL = QtGui.QHBoxLayout()
        self.makeBootableFromISO_horizantalLayout_ALL.setObjectName(_fromUtf8("makeBootableFromISO_horizantalLayout_ALL"))
        self.makeBootableFromISO_horizantalLayout_select = QtGui.QHBoxLayout()
        self.makeBootableFromISO_horizantalLayout_select.setObjectName(_fromUtf8("makeBootableFromISO_horizantalLayout_select"))
        self.makeBootableFromISO_lineEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.makeBootableFromISO_lineEdit.setObjectName(_fromUtf8("makeBootableFromISO_lineEdit"))
        self.makeBootableFromISO_horizantalLayout_select.addWidget(self.makeBootableFromISO_lineEdit)
        self.makeBootableFromISO_selectTool = QtGui.QToolButton(self.layoutWidget_2)
        self.makeBootableFromISO_selectTool.setIcon(icon5)
        self.makeBootableFromISO_selectTool.setObjectName(_fromUtf8("makeBootableFromISO_selectTool"))
        self.makeBootableFromISO_horizantalLayout_select.addWidget(self.makeBootableFromISO_selectTool)
        self.makeBootableFromISO_horizantalLayout_ALL.addLayout(self.makeBootableFromISO_horizantalLayout_select)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.makeBootableFromISO_horizantalLayout_ALL.addItem(spacerItem4)
        self.makeBootableFromISO_actionTool = QtGui.QToolButton(self.layoutWidget_2)
        self.makeBootableFromISO_actionTool.setObjectName(_fromUtf8("makeBootableFromISO_actionTool"))
        self.makeBootableFromISO_horizantalLayout_ALL.addWidget(self.makeBootableFromISO_actionTool)
        self.makeBootableFromISO_verticalLayout.addLayout(self.makeBootableFromISO_horizantalLayout_ALL)
        self.makeBootableFromISO_label = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.makeBootableFromISO_label.setFont(font)
        self.makeBootableFromISO_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.makeBootableFromISO_label.setObjectName(_fromUtf8("makeBootableFromISO_label"))
        self.makeBootableFromISO_verticalLayout.addWidget(self.makeBootableFromISO_label)
        self.makeBootableFromROM_frame = QtGui.QFrame(self.makeBootable_tab)
        self.makeBootableFromROM_frame.setGeometry(QtCore.QRect(20, 160, 861, 101))
        self.makeBootableFromROM_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.makeBootableFromROM_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.makeBootableFromROM_frame.setObjectName(_fromUtf8("makeBootableFromROM_frame"))
        self.layoutWidget_3 = QtGui.QWidget(self.makeBootableFromROM_frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 841, 81))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.makeBootableFromROM_verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.makeBootableFromROM_verticalLayout.setMargin(0)
        self.makeBootableFromROM_verticalLayout.setObjectName(_fromUtf8("makeBootableFromROM_verticalLayout"))
        self.makeBootableFromROM_horizantalLayout_ALL = QtGui.QHBoxLayout()
        self.makeBootableFromROM_horizantalLayout_ALL.setObjectName(_fromUtf8("makeBootableFromROM_horizantalLayout_ALL"))
        self.makeBootableFromROM_horizantalLayout_select = QtGui.QHBoxLayout()
        self.makeBootableFromROM_horizantalLayout_select.setObjectName(_fromUtf8("makeBootableFromROM_horizantalLayout_select"))
#        self.makeBootableFromROM_lineEdit = QtGui.QLineEdit(self.layoutWidget_3)
#        self.makeBootableFromROM_lineEdit.setObjectName(_fromUtf8("makeBootableFromROM_lineEdit"))
#        self.makeBootableFromROM_horizantalLayout_select.addWidget(self.makeBootableFromROM_lineEdit)
#        self.makeBootableFromROM_selectTool = QtGui.QToolButton(self.layoutWidget_3)
#        self.makeBootableFromROM_selectTool.setIcon(icon98)
#        self.makeBootableFromROM_selectTool.setObjectName(_fromUtf8("makeBootableFromROM_selectTool"))
#        self.makeBootableFromROM_horizantalLayout_select.addWidget(self.makeBootableFromROM_selectTool)
        self.makeBootableFromROM_horizantalLayout_ALL.addLayout(self.makeBootableFromROM_horizantalLayout_select)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.makeBootableFromROM_horizantalLayout_ALL.addItem(spacerItem5)
        self.makeBootableFromROM_actionTool = QtGui.QToolButton(self.layoutWidget_3)
        self.makeBootableFromROM_actionTool.setObjectName(_fromUtf8("makeBootableFromROM_actionTool"))
        self.makeBootableFromROM_horizantalLayout_ALL.addWidget(self.makeBootableFromROM_actionTool)
        self.makeBootableFromROM_verticalLayout.addLayout(self.makeBootableFromROM_horizantalLayout_ALL)
        self.makeBootableFromROM_label = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.makeBootableFromROM_label.setFont(font)
        self.makeBootableFromROM_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.makeBootableFromROM_label.setObjectName(_fromUtf8("makeBootableFromROM_label"))
        self.makeBootableFromROM_verticalLayout.addWidget(self.makeBootableFromROM_label)
        self.tabWidget.addTab(self.makeBootable_tab, _fromUtf8(""))
        self.selectPartition_label = QtGui.QLabel(self.centralwidget)
        self.selectPartition_label.setGeometry(QtCore.QRect(340, 20, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectPartition_label.setFont(font)
        self.selectPartition_label.setObjectName(_fromUtf8("selectPartition_label"))
        MainWindow.setCentralWidget(self.centralwidget)
	self.format_button.clicked.connect(self.formatDialogOpen)
	self.permission_button.clicked.connect(self.permissionDialogOpen)
	self.checkForBadBlocks_button.clicked.connect(self.badBlocksDialogOpen)
	self.restoreFromISO_selectTool.clicked.connect(self.openISO)
	self.backupToISO_selectTool.clicked.connect(self.saveISO)
	self.appendAllDrives_withChildren()
	self.updateRom()
	self.updateTree_button.clicked.connect(self.updateTree)
	self.unmount_button.clicked.connect(self.unmount)
	self.mount_button.clicked.connect(self.mount)
	self.backupToISO_actionTool.clicked.connect(self.backupToISO_dialogOpen)
	self.restoreFromISO_actionTool.clicked.connect(self.restoreFromISO_dialogOpen)
	self.backupToFolder_selectTool.clicked.connect(self.openFolder)
	self.restoreFromFolder_selectTool.clicked.connect(self.openFolder_restore)
	self.backupToFolder_actionTool.clicked.connect(self.backupToFolderDialogOpen)
	self.makeBootableFromISO_selectTool.clicked.connect(self.openISO_yardir)
	self.makeBootableFromISO_actionTool.clicked.connect(self.makeBootableFromISO_dialogOpen)
	self.makeBootableFromROM_actionTool.clicked.connect(self.syncWithRomDialogOpen)
	self.restoreFromFolder_actionTool.clicked.connect(self.restoreFromFolderDialogOpen)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateTree(self):
	self.treeWidget.clear()
	self.updateRom()
	self.appendAllDrives_withChildren()

    def updateRom(self):
	output = self.getCapacity_pleb( self.getRomDriveName() )
	if output == "Please mount to see":
	    self.makeBootableFromROM_label.setText("Capacity : Your optical drive is empty.") 
	else:
	    self.makeBootableFromROM_label.setText("Capacity : %s kb"%( self.getCapacity_pleb( self.getRomDriveName() ) )) 
    def badBlocks(self):
	if uik.sudo == False:
	    QMessageBox.warning(None,"Alamo","Please try to use this function with sudo privileges.")
	    return 0
	elif len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	else:
	    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	    p2 = subprocess.Popen(["sudo","-S","badblocks","-v","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
	    p1.stdout.close()
	    output = p2.communicate()[1]
	    if output.find("0 bad blocks") != -1:
	        QMessageBox.information(None,"Alamo","Your partition looks well fine! There seems to be no bad blocks.")
	    else:
		start = output.find("Pass comple")
		output = output[start:]
	        QMessageBox.warning(None,"Alamo",output+"\n"+"Please repair your drive.")
    def getModifyTime_folder(self):
	file_ = ui.restoreFromFolder_lineEdit.text()
	p1 = subprocess.Popen(["stat","%s"%file_], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep","Modify"],stdin=p1.stdout, stdout=subprocess.PIPE)
	output = p2.communicate()[0]
	start = output.find(":")
	finish = output.find("+")
	output = output[start+2:finish-7]
	return output
    def getModifyTime(self):
	file_ = ui.restoreFromISO_lineEdit.text()
	p1 = subprocess.Popen(["stat","%s"%file_], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep","Modify"],stdin=p1.stdout, stdout=subprocess.PIPE)
	output = p2.communicate()[0]
	start = output.find(":")
	finish = output.find("+")
	output = output[start+2:finish-7]
	return output
    def getFakeConnectionPoint(self,partitionPoint):
	p1 = subprocess.Popen(["df"], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep",partitionPoint],stdin=p1.stdout, stdout=subprocess.PIPE)
	output = p2.communicate()[0]
	a=output.find("%")
	output=output[a+2:-1]
	if len(partitionPoint)==8:
	    return "Null"
	else:
	    return output
    def getUsage(self, fakeConnectionPoint):
	realConnectionPoint=fakeConnectionPoint.replace(' ','\ ')
	stdout = Popen("du -k -s " + realConnectionPoint, shell=True, stdout=PIPE).stdout
	output = stdout.read()
	output = str(output)
	usage=str()
	for i in output:
	    try:
		if int(i) or int(i)==0:
		    usage += str(i)
	    except ValueError:
		break
	return usage

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Alamo", None, QtGui.QApplication.UnicodeUTF8))
        self.updateTree_button.setText(QtGui.QApplication.translate("MainWindow", "Update Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.checkForBadBlocks_button.setText(QtGui.QApplication.translate("MainWindow", "Check for Bad Blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.format_button.setText(QtGui.QApplication.translate("MainWindow", "Format", None, QtGui.QApplication.UnicodeUTF8))

        self.permission_button.setText(QtGui.QApplication.translate("MainWindow", "Set Permissions", None, QtGui.QApplication.UnicodeUTF8))

        self.mount_button.setText(QtGui.QApplication.translate("MainWindow", "Mount", None, QtGui.QApplication.UnicodeUTF8))
        self.unmount_button.setText(QtGui.QApplication.translate("MainWindow", "Unmount", None, QtGui.QApplication.UnicodeUTF8))
        self.backupToISO_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.backupToISO_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Backup to ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.backupToFolder_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.backupToFolder_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Backup to Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.backup_tab), QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromISO_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromISO_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Restore from ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromISO_label.setText(QtGui.QApplication.translate("MainWindow", "Capacity :              Last Change :", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromFolder_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromFolder_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Restore from Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreFromFolder_label.setText(QtGui.QApplication.translate("MainWindow", "Capacity :              Last Change :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.restoreFromFolder_tab), QtGui.QApplication.translate("MainWindow", "Restore from Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.makeBootableFromISO_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.makeBootableFromISO_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Make Bootable by Using an ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.makeBootableFromISO_label.setText(QtGui.QApplication.translate("MainWindow", "Capacity :          Suitable:", None, QtGui.QApplication.UnicodeUTF8))
#        self.makeBootableFromROM_selectTool.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.makeBootableFromROM_actionTool.setText(QtGui.QApplication.translate("MainWindow", "Sync Partition with Optical Drive", None, QtGui.QApplication.UnicodeUTF8))
        self.makeBootableFromROM_label.setText(QtGui.QApplication.translate("MainWindow", "Capacity :", None, QtGui.QApplication.UnicodeUTF8))
	self.updateRom()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.makeBootable_tab), QtGui.QApplication.translate("MainWindow", "Make Bootable and Sync With Optical Drive", None, QtGui.QApplication.UnicodeUTF8))
        self.selectPartition_label.setText(QtGui.QApplication.translate("MainWindow", "Please Select The Partition", None, QtGui.QApplication.UnicodeUTF8))

    def appendAllDrives_withChildren(self):
	driveNames = getDriveNames()
	partitionPoints = getPartitionPoints()
	self.major=list()
	self.minor=list()
	if uik.sudo==True:
	    for i in range(len(driveNames)):
	        try:
	            if len(partitionPoints[i])==4:
		        currentPoint = partitionPoints[i]
		        label = self.getLabel(currentPoint)
		        type_ = self.getType(currentPoint)
		        capacity = str( self.getCapacity("/dev/"+currentPoint) )
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        freeSpace = str( int(capacity) - int(usage) )
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
		        self.minor.append(QtGui.QTreeWidgetItem([ currentPoint,label,capacity,freeSpace,mount,connectionPoint,usage,type_,driveNames[i],permission,self.getPermissionConnect(currentPoint) ]))
	            else:
	                currentPoint = partitionPoints[i]
		        capacity = str( self.getCapacity("/dev/"+currentPoint) )
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        type_ = self.getType(currentPoint)
		        freeSpace = "Null"
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
		        self.major.append(QtGui.QTreeWidgetItem([currentPoint,"",capacity,freeSpace,mount,"",usage,type_,driveNames[i],permission,self.getPermissionConnect(currentPoint)]))
	        except ValueError:
		    if len(partitionPoints[i])==3:
		        currentPoint = partitionPoints[i]
		        capacity = str( self.getCapacity("/dev/"+currentPoint) )
		        type_ = self.getType(currentPoint)
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        freeSpace = "Null"
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
		        self.major.append(QtGui.QTreeWidgetItem([currentPoint,"",capacity,freeSpace,mount,"",usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
		    else:
		        currentPoint = partitionPoints[i]
		        label = self.getLabel(currentPoint)
		        type_ = self.getType(currentPoint)
		        capacity = str( self.getCapacity("/dev/"+currentPoint) )
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
		        self.minor.append(QtGui.QTreeWidgetItem([currentPoint,label,capacity," ",mount,connectionPoint,usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
#	    for i in self.major:
#	        sumFree=0
#	        usage=0
#	        capacity=0
#	        for j in self.minor:
#		    if j.text(0)[:3]==i.text(0):
#		        i.addChild(j)
#		        sumFree+=int(j.text(3))
#		        usage+=int(j.text(6))
#		        capacity+=int(j.text(2))
#	        i.setText(2,str(capacity))
#	        i.setText(3,str(sumFree))
#	        i.setText(6,str(usage))

	    for i in self.major:
		for j in self.minor:
		    if j.text(0)[:3]==i.text(0):
			i.addChild(j)

	    for i in self.major:
	        self.treeWidget.addTopLevelItem(i)
	        i.setExpanded(1)
	else:
	    for i in range(len(driveNames)):
	        try:
	            if len(partitionPoints[i])==4:
		        currentPoint = partitionPoints[i]
		        label = self.getLabel(currentPoint)
			type_ = self.getType_pleb("/dev/"+currentPoint)
		        capacity = str( self.getCapacity_pleb("/dev/"+currentPoint) )
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        freeSpace = str( int(capacity) - int(usage) )
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
			if mount == "Not mounted":
		            self.minor.append(QtGui.QTreeWidgetItem([currentPoint,label,capacity,freeSpace,mount,connectionPoint,"Please mount to see",type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
			else:
		            self.minor.append(QtGui.QTreeWidgetItem([currentPoint,label,capacity,freeSpace,mount,connectionPoint,usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
	            else:
	                currentPoint = partitionPoints[i]
		        capacity = str( self.getCapacity_pleb("/dev/"+currentPoint) )
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        freeSpace = ""
		        type_ = self.getType_pleb(currentPoint)
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			permission = self.getPermission(currentPoint)
			if mount == "Not mounted":
		            self.major.append(QtGui.QTreeWidgetItem([currentPoint,"","",freeSpace,"","","Please mount to see",type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
			else:
		            self.major.append(QtGui.QTreeWidgetItem([currentPoint,"","",freeSpace,"","",usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
	        except ValueError:
		    if len(partitionPoints[i])==3:
		        currentPoint = partitionPoints[i]
		        mount = self.checkMounted("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
		        freeSpace = ""
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
			type_=""
			permission = self.getPermission(currentPoint)
		        self.major.append(QtGui.QTreeWidgetItem([currentPoint,"","",freeSpace,"","",usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
		    else:
		        currentPoint = partitionPoints[i]
		        label = self.getLabel(currentPoint)
		        capacity = str( self.getCapacity_pleb("/dev/"+currentPoint) )
		        type_ = self.getType_pleb("/dev/"+currentPoint)
		        mount = self.checkMounted("/dev/"+currentPoint)
		        connectionPoint = self.getFakeConnectionPoint("/dev/"+currentPoint)
		        usage = self.getUsage(self.getFakeConnectionPoint("/dev/"+currentPoint))
			permission = self.getPermission(currentPoint)
		        self.minor.append(QtGui.QTreeWidgetItem([currentPoint,label,capacity," ",mount,connectionPoint,usage,type_,driveNames[i],permission, self.getPermissionConnect(currentPoint)]))
	    for i in self.major:
	        for j in self.minor:
		    if j.text(0)[:3]==i.text(0):
		        i.addChild(j)
	    for i in self.major:
	        self.treeWidget.addTopLevelItem(i)
	        i.setExpanded(1)

	
    def backupToFolder(self):
	output = cmd_output(["df"])
	output = str(output)
	ourline = output.find("/dev/"+self.treeWidget.currentItem().text(0))
	output=str(output)
	output=output[ourline:]
	a=output.find("%")
	output=output[a+2:-1]
	connectionPoint = output
	destination = self.backupToFolder_lineEdit.text()
	if ui.treeWidget.currentItem().text(4) == "Not mounted":
	    QMessageBox.warning(None, "Alamo", "Please mount to backup.")
	    return 0
	if len(destination) == 0:
	    QMessageBox.warning(None, "Alamo", "Please select a folder")
	    return 0 
	if connectionPoint.find('/dev/') != -1:
	    last = connectionPoint.find('/dev/')
	    connectionPoint = connectionPoint[:last-1]
	connectionPoint=connectionPoint.replace(' ','\\ ')
	if uik.sudo == False:
	    stdout = Popen("rsync -r -a %s %s"%(connectionPoint,destination), shell=True, stdout=PIPE).stdout
	    output = stdout.read()
	    output = str(output)
	    if len(output) == 0:
	        QMessageBox.information(None, "Alamo", "Gratz! It has been backuped.")
	else:
	    stdout = Popen("rsync -r -a %s %s"%(connectionPoint,destination), shell=True, stdout=PIPE).stdout
	    output = stdout.read()
	    output = str(output)
	    if len(output) == 0:
	        QMessageBox.information(None, "Alamo", "Gratz! It has been backuped.")
	self.updateTree()

    def restoreFromFolderDialogOpen(self):
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	if len( self.restoreFromFolder_lineEdit.text() ) == 0 :
	    QMessageBox.warning(None, "Alamo", "Please select a folder")
	    return 0
	if self.treeWidget.currentItem().text(9)[-2] != "w":
	    QMessageBox.warning(None, "Alamo", "You don't have write access to that partition.")
	    return 0
	if self.treeWidget.currentItem().text(10)[-2] != "w":
	    QMessageBox.warning(None, "Alamo", "You don't have write access to connection point of that partition. This may be because of data on the partition is read-only.")
	    return 0
	self.dialog = restoreFromFolderDialog()

	if self.dialog.exec_():
	    self.restoreFromFolder()
	else:
	    pass

	

    def restoreFromFolder(self):
	output = cmd_output(["df"])
	output = str(output)
	ourline = output.find("/dev/"+self.treeWidget.currentItem().text(0))
	output = str(output)
	output = output[ourline:]
	a=output.find("%")
	output=output[a+2:-1]
	destination = output
	source = self.restoreFromFolder_lineEdit.text()
#	if ui.treeWidget.currentItem().text(4) == "Not mounted":
#	    QMessageBox.warning(None, "Alamo", "Please mount to backup.")
#	    return 0
	if len(destination) == 0:
	    QMessageBox.warning(None, "Alamo", "Please select a folder")
	    return 0 
	if destination.find('/dev/') != -1:
	    last = destination.find('/dev/')
	    destination = destination[:last-1]
	destination = destination.replace(' ','\\ ')
	source = source.replace(' ','\\ ')
	if uik.sudo == False:
	    stdout = Popen("rsync -r -a %s %s"%(source, destination), shell=True, stdout=PIPE).stdout
	    output = stdout.read()
	    output = str(output)
	    if len(output) == 0:
	        QMessageBox.information(None, "Alamo", "It has been restored.")
	else:
	    stdout = Popen("rsync -r -a %s %s"%(source, destination), shell=True, stdout=PIPE).stdout
	    output = stdout.read()
	    output = str(output)
	    if len(output) == 0:
	        QMessageBox.information(None, "Alamo", "It has been restored.")
	self.updateTree()

    def makeBootableFromROM(self):
	if uik.sudo == False:
	    if ui.treeWidget.currentItem().text(4) == "Mounted":
	        QMessageBox.warning(None,"Alamo","In order to use this option you need to unmount your partition first.")
		return 0
	    p1 = subprocess.Popen(["cp","/dev/"+self.getRomDriveName(),"/dev/"+ui.treeWidget.currentItem().text(0)], stdout = subprocess.PIPE, stderr = PIPE)
	    output = p1.communicate()
	    if output[1] == '':
		p2 = subprocess.Popen(["sync"], stdout = PIPE,stderr = PIPE)
	        self.updateTree()
	        QMessageBox.information(None,"Alamo", "Your partition has been synced with your optical drive.")
	    elif output[1].find("engellendi") != -1:
		QMessageBox.warning(None, "Alamo", "You don't have write permission to partition that you've chosen.")
	    elif output[1].find("medium yok") != -1:
		QMessageBox.warning(None, "Alamo", "Your optical drive is empty.")
	    self.updateTree()
	else:
	    if ui.treeWidget.currentItem() == None:
	        QMessageBox.warning(None,"Alamo","Please select a minor partition.")
		return 0
	    elif ui.treeWidget.currentItem().text(4) == "Mounted":
	        QMessageBox.warning(None,"Alamo","In order to use this option you need to unmount your partition first.")
		return 0
	    p0 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	    p1 = subprocess.Popen(["sudo","-S","cp","/dev/"+self.getRomDriveName(),"/dev/"+ui.treeWidget.currentItem().text(0)], stdin=p0.stdout, stdout=subprocess.PIPE)
	    p2 = subprocess.Popen(["sync"], stdout = subprocess.PIPE,stderr = subprocess.PIPE)
	    p0.stdout.close()
	    self.updateTree()
	    QMessageBox.information(None,"Alamo","Your partition has been synced with your optical drive.")
	self.updateTree()

    def getRomDriveName(self):
	p1 = subprocess.Popen(["cat","/proc/sys/dev/cdrom/info"], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep","name"],stdin=p1.stdout, stdout=subprocess.PIPE)
	check = p2.communicate()[0]
	start = check.find(":")
	check = check[start+1:]
	while (check.find("	") == 0):
	    check = check[1:]
	check = check[:-1]
	return check

    def backupToISO(self):
	if uik.sudo == True:
	    partition = "/dev/"+ui.treeWidget.currentItem().text(0)
	    connectionPoint = self.getFakeConnectionPoint(partition)
	    connectionPoint = connectionPoint.replace(' ','\ ')
	    destination = ui.backupToISO_lineEdit.text()
	    if len(destination) == 0 or destination[-3:] != "iso":
		QMessageBox.warning(None, "Alamo", "Please select an ISO.")
		return 0
	    if ui.treeWidget.currentItem().text(4) == "Not mounted":
		QMessageBox.warning(None, "Alamo", "Please mount to backup.")
		return 0
	    p1 = subprocess.Popen(["genisoimage", "-o", "%s"%destination,"%s"%connectionPoint], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	    output, err = p1.communicate()
	    QMessageBox.information(None, "Alamo", "It has been backuped to ISO.")
	else:
	    partition = "/dev/"+ui.treeWidget.currentItem().text(0)
	    connectionPoint = self.getFakeConnectionPoint(partition)
	    connectionPoint = connectionPoint.replace(' ','\ ')
	    destination = ui.backupToISO_lineEdit.text()
	    if len(destination) == 0 or destination[-3:] != "iso":
		QMessageBox.warning(None, "Alamo", "Please select an ISO.")
		return 0
	    if ui.treeWidget.currentItem().text(4) == "Not mounted":
		QMessageBox.warning(None, "Alamo", "Please mount to backup.")
		return 0
	    p2 = subprocess.Popen(["genisoimage", "-o", "%s"%destination,"%s"%connectionPoint], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	    output, err = p2.communicate()
	    QMessageBox.information(None, "Alamo", "It has been backuped to ISO.")
	self.updateTree()
    def restoreFromISO(self):
	partition = "/dev/"+ui.treeWidget.currentItem().text(0)
	source = ui.restoreFromISO_lineEdit.text()
	if uik.sudo == False:
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None,"Alamo","You need to unmount and mount again or replug your drive in order to see restored contents after process having finished.")
	    else:
	        output=cmd_output(["cp", "%s"%source, "%s"%partition])
	        output=str(output)
	        os.system("sync")
	        if len(output) == 0:	
		    QMessageBox.information(None, "Alamo", "Your partition has been made bootable with your ISO.")
	        elif output.find("normal dosya") != -1:
		    QMessageBox.warning(None, "Alamo", "Please be sure about that you have write permission to partition.")	
	else:
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None,"Alamo","In order to use this option you need to unmount your partition first.")
	    else:
		p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		p2 = subprocess.Popen(["sudo", "-S", "cp", "%s"%source, "%s"%partition], stdin = p1.stdout, stdout = PIPE, stderr = PIPE)
		p1.stdout.close()
	        os.system("sync")
	        QMessageBox.information(None, "Alamo", "It has been restored.")
	self.updateTree()
    def yardir(self):
	partition="/dev/"+ui.treeWidget.currentItem().text(0)
	source=ui.makeBootableFromISO_lineEdit.text()
	if source[-3:] != "iso" or len(source) == 0:
	    QMessageBox.warning(None,"Alamo","Please choose an ISO.")
	    return 0
	if self.checkBootable() == "The ISO that you've chosen isn't bootable.":
	    QMessageBox.warning(None,"Alamo","The chosen ISO isn't bootable. Please try 'Restore from ISO' function")
	    return 0
	if len( ui.treeWidget.currentItem().text(0) )==4:
	    QMessageBox.warning(None,"Alamo","Please use this function with major partitions.")
	    return 0
	if uik.sudo == False:
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None, "Alamo", "In order to use this option you need to unmount your partition first.")
		return 0
	    elif (ui.treeWidget.currentItem().text(4) == "Not mounted"):
		opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity information while the partition is unmounted. Please be sure about you have enough space.", "OK", "Cancel")
		if opt == 0:
	            #output=cmd_output(["cp", "%s"%source, "%s"%partition])
		    p1 = subprocess.Popen(["cp", "%s"%source, "%s"%partition], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		    p1.stdout.close()
	            #output=str(output)
		    output, err = p1.communicate()
	            os.system("sync")

	            if len(err) == 0 and len(output) == 0:
		        QMessageBox.information(None, "Alamo", "Your partition has been made bootable with your ISO.")
	            elif err.find("normal dosya") != -1:
		        QMessageBox.warning(None, "Alamo", "Please be sure about that you have write permission to partition.")
		    elif err.find("engellendi") != -1 :
		        QMessageBox.warning(None, "Alamo", "Please be sure about that you have write permission to partition.")

		else:
		    return 0
	    elif (ui.treeWidget.currentItem().text(4) == ""):
#		opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity and mount situation information while the partition is unmounted. Please be sure about you have enough space and all your partitions are unmounted.", "OK", "Cancel")
#		if opt == 0:
	            #output=cmd_output(["cp", "%s"%source, "%s"%partition])
		p1 = subprocess.Popen(["cp", "%s"%source, "%s"%partition], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	            #output=str(output)
		output, err = p1.communicate()
	        os.system("sync")
	        if len(output) == 0:	
		    QMessageBox.information(None, "Alamo", "Your partition has been made bootable with your ISO.")
	        elif output.find("normal dosya") != -1:
		    QMessageBox.warning(None, "Alamo", "Please be sure about that you have write permission to partition.")
	else:
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None,"Alamo","In order to use this option you need to unmount your partition first.")
		return 0
	    if int( ui.treeWidget.currentItem().text(2) ) < int( self.getISO_Capacity() ) + 100:
	        QMessageBox.warning(None,"Alamo","There is not enough space in your partition.")
		return 0
	    else:
		p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		p2 = subprocess.Popen(["sudo", "-S", "cp", "%s"%source, "%s"%partition], stdin = p1.stdout, stdout = subprocess.PIPE)
		check = p2.communicate()[0]
	        os.system("sync")
	        if len(check) == 0:	
		    QMessageBox.information(None, "Alamo", "Your partition has been made bootable with your ISO.")
	        elif check.find("normal dosya") != -1:
		    QMessageBox.warning(None, "Alamo", "Please be sure about that you have write permission to partition.")
	self.updateTree()
    def checkMounted(self,partition):
	output=check_output("mount")
	output=str(output)
	if output.find(partition) != -1:
	    return "Mounted"
	else:
	    return "Not mounted"
    def mount(self):
	partitionName = ui.treeWidget.currentItem().text(0)

	if uik.sudo == False:
	    QMessageBox.warning(None,"Alamo","Please use this function with sudo privileges.")
	    return 0
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	elif len(partitionName)==3:
	    QMessageBox.warning(None,"Alamo","Please select a minor partition.")
	    return 0
	else:
	    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	    p2 = subprocess.Popen(["file", "/media/%s"%partitionName], stdin = p1.stdout, stdout = subprocess.PIPE)
	    check = p2.communicate()[0]
	    if check.find("ERROR") != -1: #mnt klasoru icinde degilse klasor aciyoruz
		p1 = subprocess.Popen(["echo", "%s"%uik.pswd], stdout = subprocess.PIPE)
		p2 = subprocess.Popen(["sudo", "-S", "mkdir", "/media/"+partitionName], stdin=p1.stdout, stdout=subprocess.PIPE)
	    partitionPoint="/dev/"+partitionName
	    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	    p2 = subprocess.Popen(["sudo","-S","mount","%s"%partitionPoint,"/media/%s"%partitionName],stdin=p1.stdout, stdout=subprocess.PIPE)
	    check = p2.communicate()[0]
	    if len(check) == 0:
	        QMessageBox.information(None, "Alamo", "Your device has been mounted into system successfully!")
	    elif check.find("bunu sadece") != -1:
	        QMessageBox.warning(None,"Alamo","Please try it with sudo permissions.")
	    elif check[-6:-3]== "yok":
	        QMessageBox.warning(None,"Alamo","There is no device in %s"%partition)
	    elif check.find("salt-okunur") != -1:
	        QMessageBox.information(None, "Alamo", "Your device has been mounted into system as read-only.")
	    elif check.find("read-only") != -1:
	        QMessageBox.information(None, "Alamo", "Your device has been mounted into system as read-only.")
	    else:
	        QMessageBox.warning(None,"Alamo","Your device is already mounted!")
	self.updateTree()
    def unmount(self,partitionPoint):
	if uik.sudo == False:
	    QMessageBox.warning(None,"Alamo","Please use this function with sudo privileges.")
	    return 0
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	partitionPoint="/dev/"+ui.treeWidget.currentItem().text(0)
	p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["sudo","-S","umount",partitionPoint],stdin=p1.stdout, stdout=subprocess.PIPE)
	output=p2.communicate()[0]

	if len(output) == 0:
	    QMessageBox.information(None, "Alamo", "Your device has been unmounted from system.")
	elif output.find("ve siz root") != -1:
	    QMessageBox.warning(None, "Alamo", "Please try it with sudo permissions.")
	else:
	    QMessageBox.warning(None, "Alamo", "Your device doesn't exist or already unmounted.")
	self.updateTree()
    def getCapacity_restore(self,dest):
	p1 = subprocess.Popen(["du","-s","%s"%dest],stdout=PIPE)
	output = p1.communicate()[0]
	finish = output.find("	")
	output = output [:finish]
	return output
	
    def getCapacity(self,partition):
	try:
	    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	    p2 = subprocess.Popen(["sudo","-S","blockdev","--getsz",partition],stdin=p1.stdout, stdout=subprocess.PIPE)
	    output = p2.communicate()[0]
	    output = int(output)
	    output = output*(0.5)
	    capacity = int(output)
	    return capacity
	except ValueError:
	    return "Please mount to see"
    def getCapacity_pleb(self,partitionPoint):
	p1 = subprocess.Popen(["df","-k"], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep", partitionPoint],stdin=p1.stdout, stdout=subprocess.PIPE)
	output=p2.communicate()[0]
	if len(output)==0:
	    return "Please mount to see"
	elif len(partitionPoint)==9:
	    output = output[9:]
	else:
	    output = output[8:]

	while output.find(' ') == 0:
	    output = output[1:]

	finish = output.find(' ')
	output = output[:finish]
	return output
	
    def getType(self,partitionPoint):
	stdout = Popen("echo '%s' | sudo -S blkid | grep "%uik.pswd + partitionPoint, shell=True, stdout=PIPE).stdout
	output = stdout.read()
	output = str(output)
	start = output.find(" TYPE=")
	output = output[start+6:]
	finish = output.find(" ")
	type_ = output[1:finish-1]
	return type_
    def getType_pleb(self,partitionPoint):
	p1 = subprocess.Popen(["df","-T"], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep", partitionPoint],stdin=p1.stdout, stdout=subprocess.PIPE)
	output=p2.communicate()[0]
	output = str(output)
	if len(output)==0:
	    return "Please mount to see."
	if len(partitionPoint)==9:
	    output = output[9:]
	else:
	    output = output[8:]

	while output.find(' ') == 0:
	    output = output[1:]

	finish = output.find(' ')
	output = output[:finish]
	return output
    def checkBootable(self):
	file_ = self.makeBootableFromISO_lineEdit.text()
	fileType = cmd_output(["file", "%s"%file_])
	fileType = str(fileType)
	if fileType.find("bootable") != -1:
	    return("Bootable ISO")
	else:
	    return("The ISO that you've chosen isn't bootable.")
#    def getLabel(self,partitionPoint):
#	stdout = Popen("blkid | grep " + partitionPoint, shell=True, stdout=PIPE).stdout
#	output = stdout.read()
#	output = str(output)
#	if output.find("LABEL=") != -1:
#	    start = output.find("LABEL=")
#	    output = output[start+7:]
#	    label = output[:-3]
#	    finish = output.find("\"")
#	    return label[:finish]
#	else:
#	    return "No label"
    def getLabel(self,partitionPoint):
	stdout = Popen("ls -al /dev/disk/by-label | grep "+partitionPoint, shell=True, stdout=PIPE).stdout
	output = stdout.read()
	output=str(output)
	if len(output) != 0:
	    finish = output.find("->")
	    finish = finish - 1
	    start = output.find(":")
	    start = start + 4
	    output = output[start:finish]
	    return output
	else:
	    return "No label"
    def syncWithRomDialogOpen(self):
        self.dialog = syncWithRomDialog()
	if self.dialog.exec_():
	    self.makeBootableFromROM()
	else:
	    pass
    def formatDialogOpen(self):
	if uik.sudo == False:
            QMessageBox.warning(None, "Alamo", "Please use this function with sudo privileges.")
	    return 0
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	if ui.treeWidget.currentItem().text(4) == "Mounted":
            QMessageBox.warning(None, "Alamo", "Please unmount your partition first.")
	    return 0
        self.dialog = formatDialog()
        if self.dialog.exec_():
	    if self.dialog.checkBox.checkState() == False:
	        if self.dialog.typeComboBox.currentText() == "ext2":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext2","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "ext3":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext3","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "ext4":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext4","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "ext4dev":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext4dev","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "msdos":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","msdos","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "minix":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","minix","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "vfat":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs","-t","vfat","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]
	        elif self.dialog.typeComboBox.currentText() == "fat32":
		    p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		    p2 = subprocess.Popen(["sudo","-S","mkfs.vfat","-F","32","/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		    output = p2.communicate()[0]

	        if output.find("contains a mounted file system") != -1:
                    QMessageBox.warning(None, "Alamo", "Please be sure about your %s partition is unmounted!"%("/dev/"+ui.treeWidget.currentItem().text(0)))
		elif output.find("komut yok") != -1:
                    QMessageBox.warning(None, "Alamo", "Please try it with sudo privileges.")
		elif output.find("izin yok") != -1:
                    QMessageBox.warning(None, "Alamo", "Please try it with sudo privileges.")
	        elif output.find("burada bir dosya sistemi") != -1:
                    QMessageBox.warning(None, "Alamo", "Please be sure about your %s partition is unmounted!"%("/dev/"+ui.treeWidget.currentItem().text(0)))
	        elif output.find("Not enough clusters") != -1:
	            QMessageBox.warning(None, "Alamo", "Please be sure about partition that you've chosen has enough clusters.")
	        else:
	            QMessageBox.information(None, "Alamo", "Gratz! Your partition has been succesfully formatted.")

	    else:
		label = self.dialog.labelLineEdit.text()
		if len(label) == 0:
		    QMessageBox.warning(None, "Alamo", "Please enter a text.")
		else:
	            if self.dialog.typeComboBox.currentText() == "ext2":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext2","-L",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "ext3":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext3","-L",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "ext4":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext4","-L",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "ext4dev":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","ext4dev","-L",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "msdos":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","msdos","-n",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "minix":
			if len(label) != 0:
			    QMessageBox.warning(None, "Alamo", "Sorry, you can't label your partition with minix file system.")
			else:
	                    output = cmd_output(["mkfs", "-t", "minix", "-L", label,"/dev/"+ui.treeWidget.currentItem().text(0)])
	                    output = str(output)
	            elif self.dialog.typeComboBox.currentText() == "vfat":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs","-t","vfat","-L",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]
	            elif self.dialog.typeComboBox.currentText() == "vfat":
		        p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
		        p2 = subprocess.Popen(["sudo","-S","mkfs.vfat","-F","32","-n",label,"/dev/"+ui.treeWidget.currentItem().text(0)],stdin=p1.stdout, stdout=subprocess.PIPE)
		        output=p2.communicate()[0]

	            if output.find("contains a mounted file system") != -1:
                        QMessageBox.warning(None, "Alamo", "Please be sure about your %s partition is unmounted!"%("/dev/"+ui.treeWidget.currentItem().text(0)))
	            elif output.find("burada bir dosya sistemi") != -1:
                        QMessageBox.warning(None, "Alamo", "Please be sure about your %s partition is unmounted!"%("/dev/"+ui.treeWidget.currentItem().text(0)))
	            elif output.find("Not enough clusters") != -1:
	                QMessageBox.warning(None, "Alamo", "Please be sure about partition that you've chosen has enough clusters.")
	            else:
	                QMessageBox.information(None, "Alamo", "Gratz! Your partition has been succesfully formatted.")

    def badBlocksDialogOpen(self):
	if uik.sudo == False:
	    QMessageBox.warning(None, "Alamo", "Please use this function with sudo privileges.")
	    return 0
	elif len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	else:
	    self.dialog = badBlockDialog()
	    if self.dialog.exec_():
	        self.badBlocks()
	    else:
	        pass

    def openISO(self):
        directory = QString(".")
	fileObj = QFileDialog.getOpenFileName(None, "Alamo" + " Open File Dialog", directory, filter="ISO Files (*.iso)")
	self.restoreFromISO_lineEdit.setText(fileObj)
	self.restoreFromISO_label.setText("Capacity : {0}       Last Change : {1}".format(self.getISO_Capacity_restore(),str(self.getModifyTime())))

    def openISO_yardir(self):
        directory = QString(".")
	fileObj = QFileDialog.getOpenFileName(None, "Alamo" + " Open File Dialog", directory, filter="ISO Files (*.iso)")
	self.makeBootableFromISO_lineEdit.setText(fileObj)
	self.makeBootableFromISO_label.setText("Capacity : {0}       Suitable : {1}".format(self.getISO_Capacity(),self.checkBootable()))

    def getISO_Capacity_restore(self):
	file_ = self.restoreFromISO_lineEdit.text()
	output = cmd_output(["du","-s","%s"%file_])
	output = str(output)
	sum_ = int()
        try:
	    for i in range(len(output)):
		int(output[i])
	except ValueError:
	    output = output[:i]
	return(output)

    def getISO_Capacity(self):
	file_ = ui.makeBootableFromISO_lineEdit.text()
	p2 = subprocess.Popen(["du","-s","%s"%file_], stdout=PIPE, stderr=PIPE)
	output = p2.communicate()[0]
	sum_ = int()
        try:
	    for i in range(len(output)):
		int(output[i])
	except ValueError:
	    output = output[:i]
	return(output)

    def saveISO(self):
        directory = QString(".")
	fileObj = QFileDialog.getSaveFileName(None, "Alamo" + " Open File Dialog", directory, filter="ISO Files (*.iso)")
	self.backupToISO_lineEdit.setText(fileObj)

    def openFolder(self):
	directory = QString(".")
	fileObj = QFileDialog.getExistingDirectory(None, 'Select directory', directory)
	self.backupToFolder_lineEdit.setText(fileObj)

    def openFolder_restore(self):
	directory = QString(".")
	fileObj = QFileDialog.getExistingDirectory(None, 'Select directory', directory)
	self.restoreFromFolder_lineEdit.setText(fileObj)
	self.restoreFromFolder_label.setText("Capacity : {0}              Last Change : {1}".format(self.getCapacity_restore(self.restoreFromFolder_lineEdit.text()), str( self.getModifyTime_folder() ) ) )

    def getPermission(self, partitionPoint):
	p1 = subprocess.Popen(["ls","-l","/dev/"], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["grep",partitionPoint],stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
	p1.stdout.close()
	output = p2.communicate()[0]
	finish = output.find(" ")
	output = output[1:finish]
	return output

    def getPermissionConnect(self,partitionPoint):
        p1 = subprocess.Popen(["ls","-l","/media/"], stdout = subprocess.PIPE)
        conPoint = self.getFakeConnectionPoint(partitionPoint)
        conPoint = conPoint.replace(' ','\\ ')
        conPoint = conPoint[8:]
        p2 = subprocess.Popen(["grep", conPoint],stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
        p1.stdout.close()
        output = p2.communicate()[0]
        finish = output.find(" ")
        output = output[1:finish]
        return output

    def permissionDialogOpen(self):
	if uik.sudo == False:
            QMessageBox.warning(None, "Alamo", "Please use this function with sudo privileges.")
	    return 0
#	if len(ui.treeWidget.currentItem().text(0))==3:
#	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
        self.dialog = permissionDialog()
        if self.dialog.exec_():
	    if self.dialog.checkBoxDrive.checkState()==False and self.dialog.checkBoxConn.checkState()==False:
		return 0
	    elif self.dialog.checkBoxDrive.isChecked()==True and self.dialog.checkBoxConn.isChecked()==False:
	        self.groupPerm = str( self.dialog.groupComboBox.currentText() )
	        self.otherPerm = str( self.dialog.otherComboBox.currentText() )
	        self.privilege = "7" + self.groupPerm + self.otherPerm
	        self.permissionSet()
	    elif self.dialog.checkBoxDrive.isChecked()==False and self.dialog.checkBoxConn.isChecked()==True:
	        self.groupPermConn = str( self.dialog.groupComboBoxConn.currentText() )
	        self.otherPermConn = str( self.dialog.otherComboBoxConn.currentText() )
	        self.privilegeConn = "7" + self.groupPermConn + self.otherPermConn
	        self.permissionSetConn()
	    elif self.dialog.checkBoxDrive.isChecked()==True and self.dialog.checkBoxConn.isChecked()==True:
	        self.groupPerm = str( self.dialog.groupComboBox.currentText() )
	        self.otherPerm = str( self.dialog.otherComboBox.currentText() )
	        self.privilege = "7" + self.groupPerm + self.otherPerm
	        self.permissionSet()
	        self.groupPermConn = str( self.dialog.groupComboBoxConn.currentText() )
	        self.otherPermConn = str( self.dialog.otherComboBoxConn.currentText() )
	        self.privilegeConn = "7" + self.groupPermConn + self.otherPermConn
	        self.permissionSetConn()
	    
	else:
	    pass

    def permissionSetConn(self):
	if len( ui.treeWidget.currentItem().text(0) ) == 3:
	    QMessageBox.warning(None, "Alamo", "Please use set permissions of connection point function for minor partitions.")
	    return 0
	connPoint = str( self.getFakeConnectionPoint( ui.treeWidget.currentItem().text(0) ) )
	p1 = subprocess.Popen( ["echo","%s"%uik.pswd],stdout=subprocess.PIPE )
	p2 = subprocess.Popen( ["sudo", "-S", "chmod", self.privilegeConn, "{0}".format(connPoint)], stdin=p1.stdout, stdout=PIPE,stderr=PIPE )
	p1.stdout.close()
	output=p2.communicate()
	if output[1].find("Salt-okunur") != -1:
	    QMessageBox.warning(None, "Alamo", "Partition's connection point permissions can't be change because it is read only.")
	elif len(output[0]) == 0 and len(output[1])== 0:
	    QMessageBox.information(None, "Alamo", "Partition's connection point permissions has been changed successfully.")

    def permissionSet(self):
	p1 = subprocess.Popen(["echo","%s"%uik.pswd], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["sudo","-S","chmod",self.privilege,"/dev/"+ui.treeWidget.currentItem().text(0)], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
	p1.stdout.close()
	output = p2.communicate()
	if len(output[0]) == 0 and len(output[1]) == 0:
	    QMessageBox.information(None,"Alamo","Partition's drive permissions has been changed successfully.")

    def backupToISO_dialogOpen(self):
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	if len( self.backupToISO_lineEdit.text() ) == 0 or self.backupToISO_lineEdit.text()[-3:] != "iso":
	    QMessageBox.warning(None, "Alamo", "Please select an ISO")
	    return 0

	self.dialog = backupToISO_dialog()
	if self.dialog.exec_():
	    self.backupToISO()
	else:
	    pass

    def backupToFolderDialogOpen(self):
	if len(ui.treeWidget.currentItem().text(0))==3:
	    QMessageBox.warning(None,"Alamo","Please use this function with minor partitions.")
	    return 0
	if ui.treeWidget.currentItem().text(4) == "Not mounted":
	    QMessageBox.warning(None, "Alamo", "Please mount to backup.")
	    return 0
	if len( self.backupToFolder_lineEdit.text() ) == 0:
	    QMessageBox.warning(None, "Alamo", "Please select a folder")
	    return 0
	self.dialog = backupToFolderDialog()
	if self.dialog.exec_():
	    self.backupToFolder()
	else:
	    pass
    def restoreFromISO_dialogOpen(self):
	try:
	    source = ui.restoreFromISO_lineEdit.text()
	    if len(ui.treeWidget.currentItem().text(0))==3:
	        QMessageBox.warning(None, "Alamo", "Please use this function with minor partitions.")
	        return 0
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None, "Alamo", "In order to use this option you need to unmount your partition first.")
	        return 0
	    if len(source) == 0 or source[-3:] != "iso":
	        QMessageBox.warning(None, "Alamo", "Please select an ISO.")
	        return 0
	    if int( ui.treeWidget.currentItem().text(2)  ) < int( ui.getISO_Capacity_restore() ) + 100:
	        QMessageBox.warning(None,"Alamo","The selected partition doesn't have enough space.")
	        return 0
	    self.dialog = restoreFromISO_dialog()
	    if self.dialog.exec_():
	        self.restoreFromISO()
	    else:
	        pass
	except:
	    opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity information while the partition is unmounted. Please be sure about you have enough space.", "OK", "Cancel")
	    if opt == 0:
	        self.dialog = restoreFromISO_dialog()
	        if self.dialog.exec_():
	            self.restoreFromISO()
	        else:
	            pass
	    else:
		pass

    def makeBootableFromISO_dialogOpen(self):
	try:
	    source = ui.makeBootableFromISO_lineEdit.text()
	    if len(ui.treeWidget.currentItem().text(0))==4:
	        QMessageBox.warning(None, "Alamo", "Please use this function with major partitions.")
	        return 0
	    if (ui.treeWidget.currentItem().text(9)[-2] != "w" and uik.sudo == False):
	        QMessageBox.warning(None, "Alamo", "You don't have write permissions.")
		return 0
	    if (ui.treeWidget.currentItem().text(4) != "None"):
	        if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	            QMessageBox.warning(None, "Alamo", "In order to use this option you need to unmount all your partitions first.")
	            return 0
#	        if (ui.treeWidget.currentItem().text(4) == ""):
#	    	    opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity and mount status information. Please be sure about you have enough space and all your partitions are unmounted.", "OK", "Cancel")
#		    if opt != 0:
#			return 0
	    if len(source) == 0 or source[-3:] != "iso":
	        QMessageBox.warning(None, "Alamo", "Please select an ISO.")
	        return 0
	    if int( ui.treeWidget.currentItem().text(2) ) < ( int( ui.getISO_Capacity() ) + 100 ):
	        QMessageBox.warning(None,"Alamo","The selected partition doesn't have enough space.")
	        return 0
	    if self.checkBootable() == "The ISO that you've chosen isn't bootable.":
	        QMessageBox.warning(None,"Alamo","The chosen ISO isn't bootable. Please try 'Restore from ISO' function")
	        return 0
	    if len( ui.treeWidget.currentItem().text(0) )==4:
	        QMessageBox.warning(None,"Alamo","Please use this function with major partitions.")
	        return 0
	    if (ui.treeWidget.currentItem().text(4) == "Mounted"):
	        QMessageBox.warning(None, "Alamo", "In order to use this option you need to unmount your partition first.")
		return 0
#	    elif (ui.treeWidget.currentItem().text(4) == "Not mounted" or len(ui.treeWidget.currentItem().text(4)) == 0 ):
	#	opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity information while the partition is unmounted. Please be sure about you have enough space.", "OK", "Cancel")
	    self.dialog = restoreFromISO_dialog()
	    if self.dialog.exec_():
	        self.yardir()
	    else:
	        pass
	except:
	    opt = QMessageBox.question(None, "Alamo", "Alamo can't get total capacity and mount status information. Please be sure about you have enough space and all your partitions are unmounted.", "OK", "Cancel")
	    if opt == 0:
	        self.dialog = makeBootableFromISO_dialog()
	        if self.dialog.exec_():
	            self.yardir()
	        else:
	            pass
	    else:
		pass

class restoreFromISO_dialog(QDialog):
    def __init__(self, parent=None):
	super(restoreFromISO_dialog,self).__init__(parent)
	self.setWindowTitle("Restore from ISO")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label0 = QLabel("Warning: ALL the data on the "+"/dev/"+ui.treeWidget.currentItem().text(0)+" will be changed irreversibly.")
	self.label1 = QLabel("%s"%ui.restoreFromISO_lineEdit.text()+"will be copied into "+"/dev/"+ui.treeWidget.currentItem().text(0))
	self.label2 = QLabel("The process may take long time according to the performance of partition that have been chosen.")
	self.label3 = QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
	self.layout.addWidget(self.label0,0,0)
        self.layout.addWidget(self.label1,1,0)
        self.layout.addWidget(self.label2,2,0)
	self.layout.addWidget(self.label3,3,0)
        self.layout.addWidget(self.buttonOk, 4, 0)
        self.layout.addWidget(self.buttonCancel, 4, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
	    

class permissionDialog(QDialog):
    def __init__(self, parent=None):
        super(permissionDialog, self).__init__(parent)
        self.setWindowTitle("Permission Set")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1 = QLabel("Owner")
	self.label2 = QLabel("Group")
	self.label3 = QLabel("Other users")
	self.checkBoxDrive = QCheckBox("Drive Permission")
	self.checkBoxConn = QCheckBox("Connection Point Permission")
	self.ownerComboBoxConn = QComboBox()
	self.ownerComboBoxConn.addItem("7 (Can't be change)")
	self.groupComboBoxConn = QComboBox()
	self.groupComboBoxConn.addItem("7")
	self.groupComboBoxConn.addItem("6")
	self.groupComboBoxConn.addItem("5")
	self.groupComboBoxConn.addItem("4")
	self.groupComboBoxConn.addItem("3")
	self.groupComboBoxConn.addItem("2")
	self.groupComboBoxConn.addItem("1")
	self.groupComboBoxConn.addItem("0")
	self.otherComboBoxConn = QComboBox()
	self.otherComboBoxConn.addItem("7")
	self.otherComboBoxConn.addItem("6")
	self.otherComboBoxConn.addItem("5")
	self.otherComboBoxConn.addItem("4")
	self.otherComboBoxConn.addItem("3")
	self.otherComboBoxConn.addItem("2")
	self.otherComboBoxConn.addItem("1")
	self.otherComboBoxConn.addItem("0")
	self.ownerComboBox = QComboBox()
	self.ownerComboBox.addItem("7 (Can't be change)")
	self.groupComboBox = QComboBox()
	self.groupComboBox.addItem("7")
	self.groupComboBox.addItem("6")
	self.groupComboBox.addItem("5")
	self.groupComboBox.addItem("4")
	self.groupComboBox.addItem("3")
	self.groupComboBox.addItem("2")
	self.groupComboBox.addItem("1")
	self.groupComboBox.addItem("0")
	self.otherComboBox = QComboBox()
	self.otherComboBox.addItem("7")
	self.otherComboBox.addItem("6")
	self.otherComboBox.addItem("5")
	self.otherComboBox.addItem("4")
	self.otherComboBox.addItem("3")
	self.otherComboBox.addItem("2")
	self.otherComboBox.addItem("1")
	self.otherComboBox.addItem("0")
        self.layout = QGridLayout()
	self.layout.addWidget(self.checkBoxDrive,1,0)
	self.layout.addWidget(self.checkBoxConn,2,0)
	self.layout.addWidget(self.label1,0,1)
	self.layout.addWidget(self.label2,0,2)
	self.layout.addWidget(self.label3,0,3)
	self.layout.addWidget(self.ownerComboBox,1,1)
	self.layout.addWidget(self.groupComboBox,1,2)
	self.layout.addWidget(self.otherComboBox,1,3)
	self.layout.addWidget(self.ownerComboBoxConn,2,1)
	self.layout.addWidget(self.groupComboBoxConn,2,2)
	self.layout.addWidget(self.otherComboBoxConn,2,3)
	self.layout.addWidget(self.otherComboBox,2,3)
	self.layout.addWidget(self.buttonOk,3,2)
	self.layout.addWidget(self.buttonCancel,3,3)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
	
class formatDialog(QDialog):
    def __init__(self,parent=None):
        super(formatDialog, self).__init__(parent)
        self.setWindowTitle("Format")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("All the data on the partition "+"/dev/"+ui.treeWidget.currentItem().text(0)+" will be deleted irreversibly.")
	self.label2=QLabel("Are you sure you want to do this ?")
	self.label3=QLabel("Please do not unplug your drive through the process.")
	self.checkBox = QCheckBox("I want to label my partition with the name:")
	self.typeLabel = QLabel("Please choose the partition type you want to set")
	self.typeComboBox = QComboBox()
	self.typeComboBox.addItem("ext2")
	self.typeComboBox.addItem("ext3")
	self.typeComboBox.addItem("ext4")
	self.typeComboBox.addItem("ext4dev")
	self.typeComboBox.addItem("minix")
	self.typeComboBox.addItem("msdos")
	self.typeComboBox.addItem("vfat")
	self.typeComboBox.addItem("fat32")
	self.labelLineEdit = QLineEdit()
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
	self.layout.addWidget(self.checkBox,3,0)
	self.layout.addWidget(self.labelLineEdit,3,1)
	self.layout.addWidget(self.typeLabel,4,0)
	self.layout.addWidget(self.typeComboBox,4,1)
        self.layout.addWidget(self.buttonOk, 5, 0)
        self.layout.addWidget(self.buttonCancel, 5, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

class backupToISO_dialog(QDialog):
    def __init__(self, parent=None):
	super(backupToISO_dialog,self).__init__(parent)
	self.setWindowTitle("Backup to ISO")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("/dev/"+ui.treeWidget.currentItem().text(0)+" partition will be backuped into "+"%s"%ui.backupToISO_lineEdit.text())
	self.label2=QLabel("The process may take long time according to the performance of partition that have been chosen.")
	self.label3=QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
        self.layout.addWidget(self.buttonOk, 3, 0)
        self.layout.addWidget(self.buttonCancel, 3, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

class makeBootableFromISO_dialog(QDialog):
    def __init__(self, parent=None):
	super(makeBootableFromISO_dialog,self).__init__(parent)
	self.setWindowTitle("Make Bootable")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("/dev/"+ui.treeWidget.currentItem().text(0)+" partition will be made bootable with "+"%s"%ui.makeBootableFromISO_lineEdit.text())
	self.label2=QLabel("The process may take long time according to the performance of partition that have been chosen.")
	self.label3=QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
        self.layout.addWidget(self.buttonOk, 3, 0)
        self.layout.addWidget(self.buttonCancel, 3, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

class backupToFolderDialog(QDialog):
    def __init__(self, parent=None):
	super(backupToFolderDialog,self).__init__(parent)
	self.setWindowTitle("Backup to Folder")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("/dev/"+ui.treeWidget.currentItem().text(0)+" partition will be backuped into "+"%s"%ui.backupToFolder_lineEdit.text())
	self.label2=QLabel("The process may take long time according to the performance of partition that have been chosen.")
	self.label3=QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
        self.layout.addWidget(self.buttonOk, 3, 0)
        self.layout.addWidget(self.buttonCancel, 3, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
	
class badBlockDialog(QDialog):
    def __init__(self,parent = None):
	super(badBlockDialog,self).__init__(parent)
	self.setWindowTitle("Hatali Blok Kontrolu")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("A bad block checking operation will be held on your "+"/dev/"+ui.treeWidget.currentItem().text(0)+" partition.")
	self.label2=QLabel("The process may take long time according to the performance of partition that have been chosen.")
	self.label3=QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
        self.layout.addWidget(self.buttonOk, 3, 0)
        self.layout.addWidget(self.buttonCancel, 3, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

class restoreFromFolderDialog(QDialog):
    def __init__(self, parent=None):
	super(restoreFromFolderDialog,self).__init__(parent)
	self.setWindowTitle("Restore from Folder")
        self.buttonOk = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")
	self.label1=QLabel("/dev/"+ui.treeWidget.currentItem().text(0)+" partition will be restored with "+"%s"%ui.restoreFromFolder_lineEdit.text())
	self.label2=QLabel("The process may take long time according to the performance of partition that have been chosen.\nYou will loose ALL data on the partition. It is recommended to make a backup.")
	self.label3=QLabel("Are you sure you want to continue ?")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
        self.layout.addWidget(self.buttonOk, 3, 0)
        self.layout.addWidget(self.buttonCancel, 3, 1)
        self.setLayout(self.layout)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

class syncWithRomDialog(QDialog):
    def __init__(self, parent=None):
	super(syncWithRomDialog,self).__init__(parent)
	self.setWindowTitle("Sync with Optical Drive")
	self.buttonOk = QPushButton("OK")
	self.buttonCancel = QPushButton("Cancel")
	self.label1 = QLabel( "/dev/" + ui.treeWidget.currentItem().text(0) + " partition will be synced with your optical drive." )
	self.label2 = QLabel( "The process may take long time according to the performance of optical drive and partition that have been chosen." )
	self.label3 = QLabel( "Are you sure you want to continue ?" )
	self.layout = QGridLayout()
	self.layout.addWidget(self.label1,0,0)
	self.layout.addWidget(self.label2,1,0)
	self.layout.addWidget(self.label3,2,0)
	self.layout.addWidget(self.buttonOk,3,0)
	self.layout.addWidget(self.buttonCancel,3,1)
	self.setLayout(self.layout)
	self.connect(self.buttonOk, SIGNAL("clicked()"), self, SLOT("accept()") )
	self.connect(self.buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()") )

class Ui_passwordMainWindow(object):
    def setupUi(self, passwordMainWindow):
        passwordMainWindow.setObjectName(_fromUtf8("passwordMainWindow"))
        passwordMainWindow.resize(570, 474)
        self.centralwidget = QtGui.QWidget(passwordMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
	self.label.setGeometry(QtCore.QRect(180, 0, 244, 130))        
	self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/onyuklerfinal.png")))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 145, 520, 186))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pswdContPushBtn = QtGui.QPushButton(self.centralwidget)
        self.pswdContPushBtn.setGeometry(QtCore.QRect(24, 410, 511, 31))
        self.pswdContPushBtn.setObjectName(_fromUtf8("pswdContPushBtn"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 335, 520, 51))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(22, 206, 525, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(22, 226, 525, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
	self.label_6_1 = QtGui.QLabel(self.centralwidget)
	self.label_6_1.setGeometry(QtCore.QRect(22, 246, 525, 21))
	self.label_6_1.setObjectName(_fromUtf8("label_6_1"))
	self.label_6_2 = QtGui.QLabel(self.centralwidget)
	self.label_6_2.setGeometry(QtCore.QRect(22, 266, 525, 21))
	self.label_7 = QtGui.QLabel(self.centralwidget)
	self.label_7.setGeometry(QtCore.QRect(22, 290, 525, 21))
	self.label_7.setObjectName(_fromUtf8("label_7"))
	self.label_8 = QtGui.QLabel(self.centralwidget)
	self.label_8.setGeometry(QtCore.QRect(22, 310, 525, 21))
	self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(22, 146, 525, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(22, 166, 525, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(22, 186, 525, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(22, 341, 511, 33))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pswdLineEdit = QtGui.QLineEdit(self.widget)
        self.pswdLineEdit.setText(_fromUtf8(""))
        self.pswdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pswdLineEdit.setObjectName(_fromUtf8("pswdLineEdit"))
        self.horizontalLayout.addWidget(self.pswdLineEdit)
        self.pswdOkPushBtn = QtGui.QPushButton(self.widget)
        self.pswdOkPushBtn.setObjectName(_fromUtf8("pswdOkPushBtn"))
        self.horizontalLayout.addWidget(self.pswdOkPushBtn)
	self.sudo = False
	self.pswd = str()
        passwordMainWindow.setCentralWidget(self.centralwidget)
	self.pswdContPushBtn.clicked.connect(self.contAsDefault)
	self.pswdOkPushBtn.clicked.connect(self.contAsSu)
        self.retranslateUi(passwordMainWindow)
        QtCore.QMetaObject.connectSlotsByName(passwordMainWindow)
    def contAsDefault(self):
	passwordMainWindow.close()
	MainWindow.show()
    def contAsSu(self):
	self.pswd = self.pswdLineEdit.text()
	p1 = subprocess.Popen(["echo","%s"%self.pswd], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(["sudo","-S","blkid"],stdin=p1.stdout, stdout=subprocess.PIPE)
	output=p2.communicate()[0]
	if len(output) == 0:
	    sudo = False
	    QMessageBox.warning(None,"Alamo","Your password does not match, please try again.")
	else:
	    self.sudo = True
	    ui.updateTree()
	    MainWindow.show()
	    passwordMainWindow.close()
    def retranslateUi(self, passwordMainWindow):
        passwordMainWindow.setWindowTitle(QtGui.QApplication.translate("passwordMainWindow", "Password Window - Alamo", None, QtGui.QApplication.UnicodeUTF8))
        self.pswdContPushBtn.setText(QtGui.QApplication.translate("passwordMainWindow", "Continue without password as default user", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("passwordMainWindow", "  Alamo is a USB drive manager which provides useful functions with simple", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("passwordMainWindow", "GUI. It needs superuser privileges in most of it\'s functions. Please enter your", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("passwordMainWindow", "sudo password in order to use checking for badblocks, mounting, unmounting,", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("passwordMainWindow", "formatting and setting permission of a partition functions. If you don\'t want to", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("passwordMainWindow", "use them, you may continue as default user. Alamo is still in development, ", None, QtGui.QApplication.UnicodeUTF8))
	self.label_6_1.setText("please do not hesitate to contact me through <b>guney.arda@metu.edu.tr</b> if ")
	self.label_6_2.setText("you're having any problem or have suggestions.")
	self.label_7.setText("P.S Thanks to Oguzhan Unlu, Begumnaz Ozcelik, Leuthar for their enormous")
	self.label_8.setText("support and Fatih Semiz for his marvelous mentorship through all process.")
        self.pswdLineEdit.setPlaceholderText(QtGui.QApplication.translate("passwordMainWindow", "Please enter your password", None, QtGui.QApplication.UnicodeUTF8))
        self.pswdOkPushBtn.setText(QtGui.QApplication.translate("passwordMainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    passwordMainWindow = QtGui.QMainWindow()
    uik = Ui_passwordMainWindow()
    uik.setupUi(passwordMainWindow)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    passwordMainWindow.show()
    sys.exit(app.exec_())

