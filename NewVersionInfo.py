import os
import platform
import traceback
import adsk.core, adsk.fusion

_thisAddinName = 'New Version Info'
_thisAddinVersion = '0.1.0'

def run(context): # pylint: disable=unused-argument

    ui = None

    try:

        app = adsk.core.Application.get()
        ui = app.userInterface

        folderName = 'NewVersionInfoForFusion360'

        if platform.system() == 'Windows':
            dataPath = os.path.join(os.getenv('APPDATA'), folderName)
        else:
            userPath = os.path.expanduser('~')
            dataPath = os.path.join(userPath, 'Library', 'Application Support', folderName)

        if not os.path.exists(dataPath):
            os.mkdir(dataPath)
            with open(os.path.join(dataPath, app.version), 'w+'):
                pass
        else:
            currentVersion = app.version
            savedVersion = os.listdir(dataPath)[0]
            if currentVersion != savedVersion:
                os.remove(os.path.join(dataPath, savedVersion))
                with open(os.path.join(dataPath, currentVersion), 'w+'):
                    pass
                ui.messageBox('Fusion 360 has been updated:\n{} => {}'.format(savedVersion, currentVersion),
                              '{} v{}'.format(_thisAddinName, _thisAddinVersion),
                              adsk.core.MessageBoxButtonTypes.OKButtonType,
                              adsk.core.MessageBoxIconTypes.InformationIconType)

    except: # pylint: disable=bare-except

        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()), '{} v{}'.format(_thisAddinName, _thisAddinVersion))

def stop(context): # pylint: disable=unused-argument

    ui = None
    try:
        pass
    except: # pylint: disable=bare-except
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()), '{} v{}'.format(_thisAddinName, _thisAddinVersion))
