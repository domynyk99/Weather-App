def select_icon(icon_name: str) -> str:
    """This function receives the icon_name as a string and returns 
    the path to an icon that matches the name"""
    icon_path = ''
    
    match icon_name:
        case 'snow': icon_path = 'src/gui/icons/snow.png'
        case 'rain': icon_path = 'src/gui/icons/rainy.png' 
        case 'fog': icon_path = 'src/gui/icons/fog.png' 
        case 'wind': icon_path = 'src/gui/icons/windy.png' 
        case 'cloudy': icon_path = 'src/gui/icons/cloudy.png' 
        case 'partly-cloudy-day': icon_path = 'src/gui/icons/partly-cloudy-day.png' 
        case 'partly-cloudy-night': icon_path = 'src/gui/icons/partly-cloudy-night.png' 
        case 'clear-day': icon_path = 'src/gui/icons/sun.png'
        case 'clear-night': icon_path = 'src/gui/icons/night.png' 
        case _ : print(f"ERROR: Could not find an icon for '{icon_name}'")
    
    return icon_path