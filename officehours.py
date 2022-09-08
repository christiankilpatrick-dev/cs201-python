weather = {"Antartica" : -89.20,
           "Russia": -67.80,
           "Greenland" : -66.10,
           "Canada" : -63.00,
           "China" : -58.00,
           "United States" : -57.00,
           "Mongolia" : -55.30,
           "Kyrgyzstan" : -53.60,
           "Sweden" : -52.60,
           "Afghanistan" : -52.20,
           "Finland" : -51.50,
           "Norway" : -51.40,
           "Italy" : -49.60,
           "Austria" : -47.10,
           "Turkey" : -46.40,
           "Germany" : -45.90,
           "North Korea" : -43.60,
           "Estonia" : -43.50,
           "Latvia" : -43.20,
           "Lithuania" : -42.90,
           "Belarus" : -42.20,
           "Czech Republic" : -42.20,
           "Armenia" : -42.00,
           "Ukraine" : -41.90,
           "Switzerland" : -41.80,
           "Japan" : -41.00,
           "France" : -41.00,
           "Poland" : -41.00,
           "Slovakia" : -41.00,
           "Serbia" : -39.50,
           "Romania" : -38.50,
           "Bulgaria" : -38.30,
           "Iceland" : -37.90,
           "Chile" : -37.00,
           "Iran" : -36.00}

def lookup_one(place):
    return weather.get(place)


def lookup_several(places):
    temps = []
    for i in places:
        temps.append(weather.get(i))
    return temps

        
print(lookup_several(["North Korea", "North Carolina", "Canada", "Norway"]))
print(lookup_one("serbia"))
