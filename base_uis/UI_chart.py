from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget
import random


# class ChartView(QWidget):
class Loader(QChartView):
    def __init__(self, parent, name, server_gpib):
        super(Loader, self).__init__()
        # super(ChartView, self).__init__()

        self.timer = QTimer()
        self._x = -1
        self._y = 1

        self.timer.timeout.connect(self.handleTimeout)
        self.timer.setInterval(250)

        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)

        # set the font size for the chart title
        font = QFont()
        font.setPixelSize(20)
        font.setPointSize(20)
        self.chart.setTitleFont(font)
        self.chart.setTitle('This is a demo of collecting data')

        self.setChart(self.chart)
        # self.chart_view = QChartView(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        self.setObjectName('chart')
        self.series = QLineSeries()
        self._xaxis = QValueAxis()
        self._yaxis = QValueAxis()

        # this should be part of add series
        color = QPen(Qt.blue)
        color.setWidth(1)
        self.series.setPen(color)

        self.chart.addSeries(self.series)
        self.chart.addAxis(self._xaxis, Qt.AlignBottom)
        self.chart.addAxis(self._yaxis, Qt.AlignLeft)

        # set ranges should be an external call
        self.series.attachAxis(self._xaxis)
        self.series.attachAxis(self._yaxis)
        self._xaxis.setRange(0, 100)
        self._yaxis.setRange(-5, 5)
        self._yaxis.setTickCount(5)

        self.chart.legend().hide()

    def add_element(self, x: float, y: float):
        self.series.append(x, y)
        self.chart.addSeries(self.series)

    # @Slot()
    def handleTimeout(self):
        y = (self._xaxis.max() - self._xaxis.min()) / self._xaxis.tickCount()
        self._x += 1
        self._y = random.uniform(0, 5) - 2.5
        self.series.append(self._x, self._y)
        if self._x == 100:
            self.timer.stop()
