def select_icon(icon_name: str) -> str:
    """This function receives the icon_name as a string and returns 
    the path to an icon that matches the name"""
    icon_path = ''
    
    match icon_name:
        case 'snow': icon_path = 'src/gui/icons/winter-50.png'
        case 'rain': icon_path = 'src/gui/icons/rainy-weather-50.png' 
        case 'fog': icon_path = 'src/gui/icons/fog-50.png' 
        case 'wind': icon_path = 'src/gui/icons/wind-50.png' 
        case 'cloudy': icon_path = 'src/gui/icons/clouds-50.png' 
        case 'partly-cloudy-day': icon_path = 'src/gui/icons/partly-cloudy-day-50.png' 
        case 'partly-cloudy-night': icon_path = 'src/gui/icons/partly-cloudy-night-50.png' 
        case 'clear-day': icon_path = 'src/gui/icons/sun-50.png'
        case 'clear-night': icon_path = 'src/gui/icons/moon-and-stars-50.png' 
        case _ : print(f"ERROR: Could not find an icon for '{icon_name}'")
    
    return icon_path