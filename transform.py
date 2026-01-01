from datetime import datetime as dt


def transform(data):
    output_data ={}

    output_data["longitude"]    = data['coord'] ['lon']
    output_data["latitude"]     = data['coord'] [ 'lat']    
    output_data["description"]  = data['weather'] [0] ['description']

    output_data["temp"]         = int(data['main'] ['temp'] - 273.15) # convert from kelvin to celsius
    output_data["feel_temp"]    = int(data['main'] ['feels_like'] -273.15)
    output_data["humidity"]     = data['main'] ['humidity']
    output_data["wind_speed"]   = int(data['wind'] ['speed']) * 3.6 # convert from m/s to km/h

    output_data["country"]      = data['sys'] ['country']
    output_data["city_name"]    = data['name']

    output_data["dt"]           = dt.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    output_data['extract_date'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    return output_data

