import QtBind
from classes.NameGenerator import NameGenerator
from phBot import *

from Plugins.classes.NameGenerator import NameGenerator

gui = QtBind.init(__name__, 'Name Generator')

QtBind.createLabel(gui,
                   'Welcome to the Name Generator',
                   10, 10)

name_input = QtBind.createLineEdit(gui, '', 10, 30, 132, 16)
only_name = QtBind.createCheckBox(gui, 'olny_name_clicked', 'Only names', 10, 50)
generate_button = QtBind.createButton(gui, 'generate', 'Generate', 10, 70)


def olny_name_clicked(checked):
    global only_name

    only_name = checked


def generate():
    global only_name

    generator = NameGenerator()
    random_name = generator.get(only_name)
    QtBind.setText(gui, name_input, random_name)
    log('Random name generated.')


log('[%s] Loaded' % __name__)
