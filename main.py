from PyQt5 import QtWidgets
import design
import sys

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # Add physician names to comboBox
        physician_list = ['Dr. Hypia',
                          'Dr. Real',
                          'Dr. Smith']
        self.comboPhysician.addItems(physician_list)
        # list of dictionaries for results
        self.list_result = []   
        # adding functionality of Add push button
        self.pushAdd.clicked.connect(self.add)
        # adding functionality of Show push button
        self.pushShow.clicked.connect(self.show_result)
        
    def add(self):
        # get text of line edit objects
        patient = self.linePatient.text()
        disease = self.lineDisease.text()
        # get text of combo box object
        physician = str(self.comboPhysician.currentText())
        # store information in a list of dictionaries
        self.list_result.append({'patient' : patient,
                                 'disease' : disease,
                                 'physician' : physician})
    
    def show_result(self):
        # clear existance text in the Text Box
        self.textResults.clear()
        for item in self.list_result:
            text = 'Patient {} has {} disease diagnoised by {}'.format(
                item['patient'],
                item['disease'],
                item['physician'])
            # append new line to text box
            self.textResults.append(text)
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()