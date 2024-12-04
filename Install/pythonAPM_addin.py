import os
import arcpy
import pythonaddins
relPath = os.path.dirname(__file__)
toolPath = relPath + r"\APM.tbx"
print toolPath

class BuildBPI(object):
    """Implementation for pythonAPM_addin.button2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "BuildBPI")
        pass

class CalculateParametersUno2(object):
    """Implementation for pythonAPM_addin.button5 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "CalculateParametersUno2")
        pass

class LowPassFilter(object):
    """Implementation for pythonAPM_addin.button1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "LowPassFilter")
        pass

class ManualCleaning(object):
    """Implementation for pythonAPM_addin.button4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "ManualCleaning")  
        pass

class PockmarksExtraction2(object):
    """Implementation for pythonAPM_addin.button3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "PockmarksExtraction2")
        pass

class PockmarksParameters2(object):
    """Implementation for pythonAPM_addin.button6 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolPath, "PockmarksParameters2")
        pass