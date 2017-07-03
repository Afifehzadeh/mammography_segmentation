# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Thu Nov 17 15:54:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from myview import MyView

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButtonPath = QtGui.QPushButton(Dialog)
        self.pushButtonPath.setObjectName("pushButtonPath")
        self.horizontalLayout_2.addWidget(self.pushButtonPath)
        self.pushButtonLoad = QtGui.QPushButton(Dialog)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout_2.addWidget(self.pushButtonLoad)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView = MyView(Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidgetImages = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetImages.sizePolicy().hasHeightForWidth())
        self.listWidgetImages.setSizePolicy(sizePolicy)
        self.listWidgetImages.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listWidgetImages.setObjectName("listWidgetImages")
        self.verticalLayout.addWidget(self.listWidgetImages)
        self.pushButtonPreview = QtGui.QPushButton(Dialog)
        self.pushButtonPreview.setObjectName("pushButtonPreview")
        self.verticalLayout.addWidget(self.pushButtonPreview)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButtonSegm = QtGui.QPushButton(Dialog)
        self.pushButtonSegm.setObjectName("pushButtonSegm")
        self.verticalLayout.addWidget(self.pushButtonSegm)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalSliderThreshold = QtGui.QSlider(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSliderThreshold.sizePolicy().hasHeightForWidth())
        self.horizontalSliderThreshold.setSizePolicy(sizePolicy)
        self.horizontalSliderThreshold.setProperty("value", 90)
        self.horizontalSliderThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderThreshold.setObjectName("horizontalSliderThreshold")
        self.horizontalLayout_4.addWidget(self.horizontalSliderThreshold)
        self.spinBox = QtGui.QSpinBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setReadOnly(True)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBoxCls = QtGui.QComboBox(Dialog)
        self.comboBoxCls.setObjectName("comboBoxCls")
        self.verticalLayout.addWidget(self.comboBoxCls)
        self.checkBoxShowMask = QtGui.QCheckBox(Dialog)
        self.checkBoxShowMask.setChecked(True)
        self.checkBoxShowMask.setObjectName("checkBoxShowMask")
        self.verticalLayout.addWidget(self.checkBoxShowMask)
        #self.groupBox = QtGui.QGroupBox(Dialog)
        #self.groupBox.setObjectName("groupBox")
        #self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        #self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.radioButtonMitosis = QtGui.QRadioButton(self.groupBox)
        #self.radioButtonMitosis.setChecked(True)
        #self.radioButtonMitosis.setObjectName("radioButtonMitosis")
        #self.verticalLayout_2.addWidget(self.radioButtonMitosis)
        #self.radioButtonRemoteSensing = QtGui.QRadioButton(self.groupBox)
        #self.radioButtonRemoteSensing.setObjectName("radioButtonRemoteSensing")
        #self.verticalLayout_2.addWidget(self.radioButtonRemoteSensing)
        #self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 248, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.pushButtonTest = QtGui.QPushButton(Dialog)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.horizontalLayout.addWidget(self.pushButtonTest)
        self.pushButtonQuit = QtGui.QPushButton(Dialog)
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButtonQuit, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QObject.connect(self.horizontalSliderThreshold, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.horizontalSliderThreshold, QtCore.SIGNAL("actionTriggered(int)"), self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Path data:", None, QtGui.QApplication.UnicodeUTF8))
        #self.lineEdit.setText(QtGui.QApplication.translate("Dialog", "/home/ar/datasets/Demos/data-demo-remote-sensing/cfg.ini", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPath.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLoad.setText(QtGui.QApplication.translate("Dialog", "Load data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Available images:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPreview.setText(QtGui.QApplication.translate("Dialog", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSegm.setText(QtGui.QApplication.translate("Dialog", "Run Segmentation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Classes:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowMask.setText(QtGui.QApplication.translate("Dialog", "Show Mask", None, QtGui.QApplication.UnicodeUTF8))
        #self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        #self.radioButtonMitosis.setText(QtGui.QApplication.translate("Dialog", "Encoder & decoder", None, QtGui.QApplication.UnicodeUTF8))
        #self.radioButtonRemoteSensing.setText(QtGui.QApplication.translate("Dialog", "U-net", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTest.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuit.setText(QtGui.QApplication.translate("Dialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))

#