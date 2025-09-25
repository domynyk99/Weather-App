def select_icon(icon_name: str) -> str:
    """This function receives the icon_name as a string and returns 
    the path to an icon that matches the name"""
    icon_path = ''
    
    match icon_name:
        case 'snow': icon_path = ''
        case 'rain': icon_path = 'src/gui/icons/rainy-weather-50.png' 
        case 'fog': icon_path = '' 
        case 'wind': icon_path = '' 
        case 'cloudy': icon_path = 'src/gui/icons/clouds-50.png' 
        case 'partly-cloudy-day': icon_path = '' 
        case 'partly-cloudy-night': icon_path = '' 
        case 'clear-day': icon_path = ''
        case 'clear-night': icon_path = '' 
        case _ : print(f"ERROR: Could not find an icon for '{icon_name}'")
    
    return icon_path