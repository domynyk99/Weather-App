# Weather App – Python GUI with PySide6 & Visual Crossing API

## Overview

This is a small Python project that displays weather data in a PySide6 GUI using the [Visual Crossing API](https://www.visualcrossing.com/weather-api).  
The goal of the project is to learn how to work with 3rd-party APIs, environment variables, and integrating API data into a GUI application.

## Features

- Fetches real-time weather data from the Visual Crossing API
- Displays temperature, conditions, and additional weather details in a simple GUI
- Built with PySide6 for a clean and easy-to-use interface

## Usage

#### Prerequisites
To use this app you need to create an account on [Visual Crossing](https://www.visualcrossing.com/weather-api)'s website and go into your account details to get your API Key

- Python 3.13 (There are compatibility problems with 3.14 and PySide6)
- [Visual Crossing API](https://www.visualcrossing.com/weather-api) – source of weather data

All of the following are automatically installed when later using `pip install -e .`
- [PySide6](https://pypi.org/project/PySide6) – GUI framework
- [requests](https://pypi.org/project/requests) – for HTTP requests
- [python-dotenv](https://pypi.org/project/python-dotenv) – to manage environment variables

1. Clone the repository:

    ```bash
    git clone https://github.com/domynyk99/Weather-App.git
    cd Weather-App
    ```

2. Install dependencies:

    ```bash
    pip install -e .
    ```

3. Setup environment variables:  
    Create a `.env` file in the project root with your API key:
    ```bash
    API_KEY = "YOUR_API_KEY_HERE"
    ```
4. Run the app:

    ```bash
    weather
    ```

Now the window should pop up and you'll be able to see the weather

## Why I built this

This project is part of the backend learning roadmap on [roadmap.sh](https://roadmap.sh/projects/weather-api-wrapper-service)

I created this project to practice working with external APIs and caching solutions.
I wanted to understand how to integrate API data into a GUI application, how to securely manage API keys using `.env` files and handle things like data storage, and user input.

## Planned features / Future Improvements
This app is still a work in progress and my next steps are:

- Implement Redis caching to reduce repeated API requests  
- Improve the layout and design of the GUI  
- Add robust error handling for invalid city names or failed API requests
