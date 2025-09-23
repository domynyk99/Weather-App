import sys
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QLabel, QApplication

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout(self)

        self.main_box()

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
        self.layout.addWidget(groupbox)

    def update(self, data: dict) -> None:
        """Update method from Observer Pattern"""
        self.location.setText(f"Location: {data["location"]}")
        self.temperature.setText(f"Temperature: {data["temp_now"]}")
        self.description.setText(f"Description: {data["description"]}")

if __name__ == "__main__":
    app = QApplication([])
    
    gui = MainWindow()
    gui.show()

    gui.set_location("Mannheim")
    gui.set_temperature("")

    sys.exit(app.exec())

