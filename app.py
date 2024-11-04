import sys
import os
from time import strftime, gmtime
import threading
from time import sleep

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtCore import QObject, pyqtSignal
from TimeExtractor import TimeExtractor


class Backend(QObject):


    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])

    def updater(self, curr_time):
        self.updated.emit(curr_time)

    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()

    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(0.1)


QQuickWindow.setSceneGraphBackend('software')

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./app.qml')

back_end = Backend()
time_extractor = TimeExtractor()
# engine.rootObjects()[0].setProperty('backend', back_end)
engine.rootObjects()[0].setProperty('currTime', time_extractor.extract())

# back_end.bootUp()

sys.exit(app.exec())