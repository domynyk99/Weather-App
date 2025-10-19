from PySide6.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QLabel, QFrame, QHBoxLayout,
                               QGridLayout, QScrollArea)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from . import icon_selector

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QPixmap('src/gui/icons/sun-50.png'))
        self.setWindowTitle('Roadmap.sh: Weather API Project Solution - Dominik Kratz')
        
        self.layout: QGridLayout = QGridLayout(self)

        self.main_box()
        self.forecast_hours_box()
        self.forecast_days_box()
        self.info_box()

    def main_box(self) -> None:
        """
        Create the top-left group box containing the main weather information:
        location, temperature, and description.
        """
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
        """
        Create the right group box displaying the temperature forecast
        for the next 14 days.
        """
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
        """
        Update the 14-day forecast box with data from the API response.
        """
        for i, day in enumerate(self.forecast_days):
            date = data['forecast_days'][i]['datetime']
            temp_min = data['forecast_days'][i]['temp_min']
            temp_max = data['forecast_days'][i]['temp_max']
            conditions = data['forecast_days'][i]['conditions']
            day.setText(f"{date}: {temp_min}{unit_group} to {temp_max}{unit_group} --- {conditions}")

    def forecast_hours_box(self) -> None:
        """
        Create the middle-left group box showing hourly temperature forecasts
        for the 24 hours of the current day.

        Initially, the labels are filled with placeholder values (10°C and a default icon).
        The data is later updated in `_update_forecast_hours()` to reflect real-time values.
        """
        groupbox = QGroupBox("")
        h_box = QHBoxLayout()

        self.forecast_hours: list[tuple[(QLabel, QLabel, QLabel)]] = []
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
        """
        Update the hourly forecast box with real-time weather data.
        """
        for i, hour in enumerate(self.forecast_hours):
            time = data['forecast_days'][0]['hours'][i]['time'][0:2]
            icon = icon_selector.select_icon(data['forecast_days'][0]['hours'][i]['icon'])
            temp = round(float(data['forecast_days'][0]['hours'][i]['temp']))
            
            hour[0].setText(f"{time}")
            hour[1].setText(f"{temp}{unit_group}")
            hour[2].setPixmap(QPixmap(icon).scaled(25,25, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def info_box(self) -> None:
        """
        Create the bottom-left group box displaying additional weather data
        such as UV index and wind direction.

        The labels are updated later via `_update_info_box()` to show real-time data.
        """
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
        """
        Update the additional information box (UV index, wind direction) with
        real-time weather data.
        """
        pass

    def update(self, data: dict) -> None:
        """
        Observer pattern entry point.

        Updates the entire GUI with new weather data from the API response,
        including current temperature, description, hourly forecast, and
        daily forecast.
        """
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