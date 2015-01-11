from YoshiViz import report_generator, decision_tree_algorithm
from PyQt4 import QtGui
import sys
import os


class Gui(QtGui.QMainWindow):

    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        QtGui.QMainWindow.__init__(self)
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QtGui.qApp.quit)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)
        self._central_widget_layout()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Yoshi Vis')
        self.show()
        sys.exit(app.exec_())

    def _central_widget_layout(self):
        central_widget = QtGui.QWidget(self)
        grid = QtGui.QGridLayout()

        #Yoshi box
        yoshi_box = QtGui.QGroupBox("Get data from Github")
        yoshi_grid = QtGui.QGridLayout()
        yoshi_grid.addWidget(QtGui.QLabel("Github repository URL:"), 0, 0)
        self.gh_url_text_box = QtGui.QLineEdit()
        gh_button = QtGui.QPushButton("Ok")
        gh_button.setEnabled(False)
        yoshi_grid.addWidget(gh_button, 1, 2)
        yoshi_grid.addWidget(self.gh_url_text_box, 0, 1)
        yoshi_box.setLayout(yoshi_grid)

        #File box
        file_box = QtGui.QGroupBox("Load existing JSON file")
        file_grid = QtGui.QGridLayout()
        file_box.setLayout(file_grid)
        file_grid.addWidget(QtGui.QLabel("File Path:"), 0, 0)
        self.file_path = QtGui.QLineEdit()
        file_grid.addWidget(self.file_path, 0, 1)
        button_browse = QtGui.QPushButton("Browse")
        file_grid.addWidget(button_browse, 0, 2)
        file_grid.addWidget(QtGui.QLabel("Repository name:"), 1, 0)
        self.repositoryName = QtGui.QLineEdit()
        file_grid.addWidget(self.repositoryName, 1, 1)
        button_file = QtGui.QPushButton("Ok")
        file_grid.addWidget(button_file, 2, 2)

        #General layout
        grid.addWidget(yoshi_box, 0, 0)
        grid.addWidget(file_box, 0, 1)
        central_widget.setLayout(grid)
        button_browse.clicked.connect(self.browse_button_clicked)
        button_file.clicked.connect(self.ok_file_button_clicked)
        self.setCentralWidget(central_widget)

    def browse_button_clicked(self):
        file_browser = QtGui.QFileDialog(self, "Open Yoshi JSON output file.", None, "JSON files (*.json *.txt)")
        file_browser.show()
        if file_browser.exec():
            self.file_path.setText(file_browser.selectedFiles()[0])

    def ok_file_button_clicked(self):
        try:
            temp_community_type = decision_tree_algorithm.\
                community_type(self.file_path.text(), self.repositoryName.text())
            file_directory = os.path.join(os.path.abspath('.'), 'YoshiViz', 'input.txt')
            report_generator.\
            generate_pdf_report(file_directory, self.repositoryName.text(), temp_community_type)
            dialog = QtGui.QMessageBox(self)
            dialog.setText("The type of " + self.repositoryName.text() + " is " + temp_community_type +
                ". Check ./yoshiviz/output for more informations.")
            dialog.exec()
        except:
            error = QtGui.QMessageBox(self)
            error.setText("Unable to find community " + self.repositoryName.text() + " in " +
                                 self.file_path.text() + " file.")
            error.setIcon(3)
            error.show()





