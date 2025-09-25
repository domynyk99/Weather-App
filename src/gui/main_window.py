import sys
from PySide6.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QLabel, QFrame, QHBoxLayout,
                               QGridLayout, QScrollArea)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from . import icon_selector

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(900, 600)
        self.layout: QGridLayout = QGridLayout(self)

        self.main_box()
        self.forecast_hours_box()
        self.forecast_days_box()
        self.info_box()

        print("MainWindow has been initialized!")

    def main_box(self) -> None:
        groupbox = QGroupBox("")
        v_box = QVBoxLayout()

        self.location = QLabel("Location:")
        self.temperature = QLabel("Temperature:")
        self.description = QLabel("Description:")

        v_box.addWidget(self.location)
        v_box.addWidget(self.temperature)
        v_box.addWidget(self.description)

        groupbox.setLayout(v_box)
        self.layout.addWidget(groupbox, 0, 0)

    def forecast_days_box(self):
        groupbox = QGroupBox("")
        v_box = QVBoxLayout()

        self.forecast_days: list[QLabel] = []

        for i in range(14):
            day = QLabel(f"{i}")
            v_box.addWidget(day)
            day.setAlignment(Qt.AlignmentFlag.AlignCenter)
            day.setLineWidth(2)
            day.setFrameStyle(QFrame.Shape.StyledPanel)
            self.forecast_days.append(day)
        
        groupbox.setLayout(v_box)
        self.layout.addWidget(groupbox, 0, 1, 3, 1)
    
    def _update_forecast_days(self, data: dict, unit_group: str) -> None:
        for i, day in enumerate(self.forecast_days):
            date = data['forecast_days'][i]['datetime']
            temp_min = data['forecast_days'][i]['temp_min']
            temp_max = data['forecast_days'][i]['temp_max']
            conditions = data['forecast_days'][i]['conditions']
            day.setText(f"{date}: {temp_min}{unit_group} to {temp_max}{unit_group} --- {conditions}")

    def forecast_hours_box(self) -> None:
        groupbox = QGroupBox("")
        h_box = QHBoxLayout()

        self.forecast_hours: list[(QLabel, QLabel, QLabel)] = []
        for i in range(24):
            gbox = QGroupBox()
            v_box = QVBoxLayout()

            time_label = QLabel(f"{i} AM")
            temp_label = QLabel("10°C")
            pixmap = QLabel()
            pixmap.setPixmap(QPixmap("src/gui/icons/rainy-weather-50.png").scaled(30,30))

            time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            pixmap.setAlignment(Qt.AlignmentFlag.AlignCenter)

            v_box.addWidget(time_label)
            v_box.addWidget(pixmap)
            v_box.addWidget(temp_label)

            gbox.setLayout(v_box)

            h_box.addWidget(gbox)

            self.forecast_hours.append((time_label, temp_label, pixmap))

        groupbox.setLayout(h_box)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(130)
        self.layout.addWidget(scroll, 1, 0)

    def _update_forecast_hours(self, data: dict, unit_group: str) -> None:
        for i, hour in enumerate(self.forecast_hours):
            time = data['forecast_days'][0]['hours'][i]['time'][0:2]
            icon = icon_selector.select_icon(data['forecast_days'][0]['hours'][i]['icon'])
            temp = round(float(data['forecast_days'][0]['hours'][i]['temp']))
            
            hour[0].setText(f"{time}")
            hour[1].setText(f"{temp}{unit_group}")
            hour[2].setPixmap(QPixmap(icon).scaled(25,25, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def info_box(self) -> None:
        groupbox = QGroupBox("")
        grid = QGridLayout()

        self.extra_info = []

        wind_direction = QLabel("Wind Direction will be shown here")
        self.extra_info.append(wind_direction)
        uv_index = QLabel("UV Index will be shown here")
        self.extra_info.append(uv_index)

        for i,info in enumerate(self.extra_info):
            info.setAlignment(Qt.AlignmentFlag.AlignCenter)
            info.setLineWidth(2)
            info.setFrameStyle(QFrame.Shape.StyledPanel)
            grid.addWidget(info, i//2, i%2)
        
        groupbox.setLayout(grid)
        groupbox.setAlignment(Qt.AlignmentFlag.AlignBaseline)
        self.layout.addWidget(groupbox, 2, 0)

    def _update_info_box(self, data: dict, unit_group: str) -> None:
        pass

    def update(self, data: dict) -> None:
        """Update method from Observer Pattern"""
        unit_group = ""
        match data['unit_group']:
            case 'metric': unit_group = '°C'
            case 'us': unit_group = '°F'
            case 'base': unit_group = 'K'
        self.location.setText(f"Location: {data['location']}")
        self.temperature.setText(f"Temperature: {data['forecast_days'][0]['temp_now']}{unit_group}")
        self.description.setText(f"Description: {data['forecast_days'][0]['description']}")
        self._update_forecast_days(data, unit_group)
        self._update_forecast_hours(data, unit_group)