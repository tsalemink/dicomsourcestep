import os
from PySide2 import QtWidgets
from mapclientplugins.dicomsourcestep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        self._previousDirectory = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._makeConnections()

    def _makeConnections(self):
        self._ui.idLineEdit.textChanged.connect(self.validate)
        self._ui.dirButton.clicked.connect(self._dirClicked)
        self._ui.dirLineEdit.textChanged.connect(self._dirEdited)

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        idValue = self.identifierOccursCount(self._ui.idLineEdit.text())
        idValid = (idValue == 0) or (idValue == 1 and self._previousIdentifier == self._ui.idLineEdit.text())
        if idValid:
            self._ui.idLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.idLineEdit.setStyleSheet(INVALID_STYLE_SHEET)

        dirValid = os.path.exists(self._ui.dirLineEdit.text())
        if dirValid:
            self._ui.dirLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.dirLineEdit.setStyleSheet(INVALID_STYLE_SHEET)

        valid = idValid and dirValid
        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(valid)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.idLineEdit.text()
        self._previousDirectory = self._ui.dirLineEdit.text()
        config = {}
        config['identifier'] = self._ui.idLineEdit.text()
        config['Directory'] = self._ui.dirLineEdit.text()
        config['File Pattern'] = self._ui.patternLineEdit.text()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._previousDirectory = config['Directory']
        self._ui.idLineEdit.setText(config['identifier'])
        self._ui.dirLineEdit.setText(config['Directory'])
        self._ui.patternLineEdit.setText(config['File Pattern'])

    def _dirClicked(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', self._previousDirectory)
        if directory:
            self._previousDirectory = directory
            self._ui.dirLineEdit.setText(directory)

    def _dirEdited(self):
        self.validate()
