## Weather App

This is a small Python project that displays weather data in a PySide6 GUI using the [Visual Crossing API](https://www.visualcrossing.com/weather-api).
The goal of the project is to learn how to work with 3rd-party APIs, environment variables, and caching mechanisms like Redis.

## Features

- Fetches real-time weather data from the Visual Crossing API
- Displays temperature, conditions, and other details in a graphical interface
- Built with PySide6 for a clean and simple GUI
- Designed to later include a search bar for different locations
- Planned integration of Redis caching to avoid unnecessary API calls

## Why I built this

This project is part of the backend learning roadmap on [roadmap.sh](https://roadmap.sh/projects/weather-api-wrapper-service)

I created this project to practice working with external APIs and caching solutions.
I wanted to understand how to integrate API data into a GUI application and handle things like request limits, data storage, and user input.

## What should be added in the future

This app is still a work in progress and my next steps are:

- Add a search bar to look up any city directly from the GUI
- Implement a Redis cache to store API responses and reduce load times (repeated requests for the same city on the same day should be served directly from the cache)
- Improve the layout and overall design of the GUI for a cleaner look and better usability
- Add more robust error handling for invalid city names or failed API requests, including clear warnings and messages so users understand what went wrong and why