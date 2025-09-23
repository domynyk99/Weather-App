import sys
from PySide6.QtWidgets import QApplication
from .weather_api import WeatherAPI
from ..gui.main_window import MainWindow

if __name__ == "__main__":
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    weather_api = WeatherAPI(base_url)
    
    app = QApplication(sys.argv)
    
    gui = MainWindow()
    gui.show()

    weather_api.register_observer(gui)
    weather_api.get_weather("Mannheim,Germany")
    
    sys.exit(app.exec())