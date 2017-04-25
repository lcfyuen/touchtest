import cv2
import numpy as np
#from matplotlib import pyplot as plt
import os
import subprocess
import time
import datetime
import glob
from PyQt4 import QtGui, QtCore
import sys
import TouchBUI
from scipy.misc import imsave
import csv
# from Tkinter import Tk
# from tkFileDialog import askopenfilename

class TouchApp(QtGui.QMainWindow):

    def __init__(self, parent = None):

        version = 2.0

        super(TouchApp, self).__init__(parent)
        self.ui = TouchBUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.reset_count()

        # self.buttondict = dict()
        # self.buttondict[1] = self.ui.pushBtn1
        # self.buttondict[2] = self.ui.pushBtn2
        # self.buttondict[3] = self.ui.pushBtn3
        # self.buttondict[4] = self.ui.pushBtn4
        # self.buttondict[5] = self.ui.pushBtn5
        # self.buttondict[6] = self.ui.pushBtn6
        # self.buttondict[7] = self.ui.pushBtn7
        # self.buttondict[8] = self.ui.pushBtn8
        # self.buttondict[9] = self.ui.pushBtn9


        #
        # print self.buttondict

        # for i in range(9):
        #     self.buttondict[i+1].clicked.connect(lambda: self.incrementCount(i+1))
        #
        self.ui.pushBtn1.clicked.connect(lambda: self.incrementCount(1))
        self.ui.pushBtn2.clicked.connect(lambda: self.incrementCount(2))
        self.ui.pushBtn3.clicked.connect(lambda: self.incrementCount(3))
        self.ui.pushBtn4.clicked.connect(lambda: self.incrementCount(4))
        self.ui.pushBtn5.clicked.connect(lambda: self.incrementCount(5))
        self.ui.pushBtn6.clicked.connect(lambda: self.incrementCount(6))
        self.ui.pushBtn7.clicked.connect(lambda: self.incrementCount(7))
        self.ui.pushBtn8.clicked.connect(lambda: self.incrementCount(8))
        self.ui.pushBtn9.clicked.connect(lambda: self.incrementCount(9))

        self.reset_count()

        # self.ui.VerNum.setText(str(version))
        #self.barcode = ""
        #self.operator = ""
        #self.logResult = dict()
    def reset_count(self):
        self.count = dict()

        font = QtGui.QFont()
        font.setPointSize(20)

        self.ui.pushBtn1.setStyleSheet("background-color: white")
        self.ui.pushBtn1.setText("-")
        self.ui.pushBtn1.setFont(font)

        self.ui.pushBtn2.setStyleSheet("background-color: white")
        self.ui.pushBtn2.setText("-")
        self.ui.pushBtn2.setFont(font)

        self.ui.pushBtn3.setStyleSheet("background-color: white")
        self.ui.pushBtn3.setText("-")
        self.ui.pushBtn3.setFont(font)

        self.ui.pushBtn4.setStyleSheet("background-color: white")
        self.ui.pushBtn4.setText("-")
        self.ui.pushBtn4.setFont(font)

        self.ui.pushBtn5.setStyleSheet("background-color: white")
        self.ui.pushBtn5.setText("-")
        self.ui.pushBtn5.setFont(font)

        self.ui.pushBtn6.setStyleSheet("background-color: white")
        self.ui.pushBtn6.setText("-")
        self.ui.pushBtn6.setFont(font)

        self.ui.pushBtn7.setStyleSheet("background-color: white")
        self.ui.pushBtn7.setText("-")
        self.ui.pushBtn7.setFont(font)

        self.ui.pushBtn8.setStyleSheet("background-color: white")
        self.ui.pushBtn8.setText("-")
        self.ui.pushBtn8.setFont(font)


        self.ui.pushBtn9.setStyleSheet("background-color: white")
        self.ui.pushBtn9.setText("-")
        self.ui.pushBtn9.setFont(font)

        for i in range(9):
            self.count[i+1] = 0
        print self.count


    def incrementCount(self, num):
        self.count[num] += 1
        self.update_ui()

    def update_ui(self):

        self.ui.pushBtn1.setText(str(self.count[1]))
        self.ui.pushBtn2.setText(str(self.count[2]))
        self.ui.pushBtn3.setText(str(self.count[3]))
        self.ui.pushBtn4.setText(str(self.count[4]))
        self.ui.pushBtn5.setText(str(self.count[5]))
        self.ui.pushBtn6.setText(str(self.count[6]))
        self.ui.pushBtn7.setText(str(self.count[7]))
        self.ui.pushBtn8.setText(str(self.count[8]))
        self.ui.pushBtn9.setText(str(self.count[9]))
        QtGui.QApplication.processEvents()

    #     self.loadConfig()
    #     self.waitforOperator()
    #     self.waitforbarcode()
    #
    # def loadConfig(self):
    #     """
    #     Loads from CSV config file
    #     Stores values in logResult dictionary
    #     :return:
    #     """
    #
    #     configFile = os.getcwd() + '\\testerconfig\BUITesterConfig.csv'
    #     with open(configFile) as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         self.logResult = next(row for row in reader)
    #
    #         # # Load config variables into log dictionary
    #         # for k, v in self.TesterConfig.iteritems():
    #         #     self.logDict[k] = v
    #         # print TesterConfig['Test_Station']
    #         # print TesterConfig['Notes']
    #         # print TesterConfig['Fixture']
    #         # print TesterConfig['BUI_Limit']{
    #
    #     # Set Text on GUI with BUI Limits
    #     self.ui.LimitValue.setText(self.logResult['BUI_Limit']+"%")
    #
    #
    # def waitforOperator(self):
    #
    #     userInput = QtGui.QInputDialog.getText(self, 'Enter ID:', 'Operator:')
    #     while str(userInput[0]) == "":
    #         userInput = QtGui.QInputDialog.getText(self, 'Enter ID:', 'Operator:')
    #
    #     #self.operator = str(userInput[0])
    #     self.logResult['Operator'] = str(userInput[0])
    #     self.ui.OperatorID.setText(self.logResult['Operator'])
    #     print self.logResult['Operator']
    #
    # def waitforbarcode(self):
    #     # Change background to yellow
    #     self.ui.startButton.setStyleSheet("background-color: yellow")
    #     self.ui.startButton.setText("SCAN BARCODE")
    #     QtGui.QApplication.processEvents()
    #
    #     userInput = QtGui.QInputDialog.getText(self, 'Welcome', 'Scan Barcode:')
    #
    #     if str(userInput[0]) != "":
    #         self.barcode = str(userInput[0])
    #         self.logResult['SN'] = self.barcode
    #
    #         #Reset GUI
    #         self.ui.startButton.setStyleSheet("background-color: cyan")
    #         self.ui.startButton.setText("START TEST")
    #         self.ui.SNValue.setText(self.barcode)
    #         self.ui.buiValue.setText("")
    #         self.ui.newbuiValue.setText("")
    #         self.ui.testResultValue.setText("")
    #         self.ui.testResultValue.setStyleSheet("background-color: white")
    #
    #         #Clear image and variable saving image
    #         self.ui.BlackImg.clear()
    #         QtGui.QApplication.processEvents()
    #
    #
    # def imageOpenCv2ToQImage (self, cv_img):
    #     # Change image to format to display in label
    #     height, width, bytesPerComponent = cv_img.shape;
    #     bytesPerLine = bytesPerComponent * width;
    #     cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB, cv_img)
    #     # np.savetxt('cv_img.csv',  cv_img, delimiter=",", fmt='%.9f')
    #     #
    #     return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    #
    # def executeTest(self):
    #
    #     if self.barcode != "":
    #         #Get test notes from GUI
    #         self.logResult['Notes'] = self.ui.TestNotes.toPlainText()
    #         #self.ui.TestNotes.setReadOnly(True)
    #         self.ui.TestNotes.setStyleSheet("background-color: LightGray")
    #
    #         #Update GUI status
    #         self.ui.startButton.setStyleSheet("background-color: gray")
    #         self.ui.startButton.setText("TEST IN PROGRESS...")
    #         QtGui.QApplication.processEvents()
    #
    #
    #         displayTest = DisplayTester(connect_camera = True) #False) #True)
    #         display = DisplayAdapter()
    #
    #         display.showwhite()
    #         displayTest.whiteImgPG = displayTest.captureWhite()
    #         whiteImg = cv2.cvtColor(displayTest.whiteImgPG, cv2.COLOR_RGB2BGR)
    #         display.end()
    #
    #         display.showblack()
    #         displayTest.blackImgPG = displayTest.captureBlack()
    #         blackImg = cv2.cvtColor(displayTest.blackImgPG, cv2.COLOR_RGB2BGR)
    #         display.end()
    #
    #         # whiteImg = cv2.imread(whiteImgPath)
    #         # blackImg = cv2.imread(blackImgPath)
    #
    #         whiteImgUD = displayTest.lens.undistort(whiteImg)
    #         blackImgUD = displayTest.lens.undistort(blackImg)
    #
    #         # ## Test code to just load images
    #         # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    #         # whiteImgPath = askopenfilename(title="Select image of WHITE Display") # show an "Open" dialog box and return the path to the selected file
    #         #
    #         # Tk().withdraw()
    #         # blackImgPath = askopenfilename(title="Select image of BLACK Display")
    #         # whiteImgUD = cv2.imread(whiteImgPath)
    #         # blackImgUD = cv2.imread(blackImgPath)
    #
    #         ### ------ Contour cropping method ------
    #         # mask = displayTest.generateMask(whiteImgUD)
    #         # ROI = displayTest.findROI(blackImgUD, mask)
    #         # BUI = displayTest.computeBUI(ROI)
    #
    #
    #         mask = displayTest.findThresholdROIMask(whiteImgUD)
    #         #np.savetxt('mask.csv',  mask, delimiter=",", fmt='%d')
    #         ROI_6 = displayTest.findROI(blackImgUD,mask)
    #         BUI_6 = displayTest.computeNoLimitBUI6(ROI_6)
    #
    #         BUI = displayTest.computeFastBUI(blackImgUD,mask)
    #         Yrgb = displayTest.generateBUImg(mask)
    #
    #         self.ui.BlackImg.setScaledContents(True)
    #         # plt.imshow(Yrgb)
    #         # plt.show()
    #         imgUDQT = self.imageOpenCv2ToQImage(Yrgb)
    #
    #         #imgUDQT = self.imageOpenCv2ToQImage(blackImgUD) #displayTest.Ycorrected)
    #         self.ui.BlackImg.setPixmap(QtGui.QPixmap.fromImage(imgUDQT))
    #
    #         font = QtGui.QFont()
    #         font.setPointSize(15)
    #         self.ui.buiValue.setText("{0:.0f}%".format(BUI * 100))
    #         self.ui.buiValue.setFont(font)
    #         self.ui.newbuiValue.setText("{0:.0f}%".format(BUI_6 * 100))
    #         self.ui.newbuiValue.setFont(font)
    #
    #
    #         self.logResult['BUI'] = str(BUI*100)
    #         self.logResult['NewBUI'] = str(BUI_6*100)
    #
    #         # Update GUI based on Pass/ Fail
    #         if (BUI * 100 <= int(self.logResult['BUI_Limit'])):
    #             self.ui.testResultValue.setText("PASS!")
    #             self.ui.testResultValue.setFont(font)
    #             self.ui.testResultValue.setStyleSheet("background-color: green")
    #             self.logResult['Test_Result'] = 'Pass'
    #         else:
    #             self.ui.testResultValue.setText("FAIL!")
    #             self.ui.testResultValue.setFont(font)
    #             self.ui.testResultValue.setStyleSheet("background-color: red")
    #             self.logResult['Test_Result'] = 'Fail'
    #
    #
    #
    #         self.ui.TestNotes.setStyleSheet("background-color: white")
    #         self.ui.TestNotes.setReadOnly(False)
    #
    #
    #         status = displayTest.logData(self.logResult)
    #         if status == 0:
    #             print('Successfully Logged!')
    #
    #
    #     self.barcode = ""
    #     self.waitforbarcode()



if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    form = TouchApp()
    form.show()
    sys.exit(app.exec_())