import os
import sys


def sayHello():
    print("Hello, World!")

def openHome():
    os.system('xdg-open ~/')

def openDocuments():
    os.system('xdg-open ~/Documentos')

def openImages():
    os.system('xdg-open ~/Imagens')

def openDownloads():
    os.system('xdg-open ~/Downloads')

def openBrowser():
    os.system('opera')



