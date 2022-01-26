#Xander Fermier
#1/25/22
#A file that manipulates and analyzes some data from information about powerplants

import csv, os

os.system("cls")

file = open("PowerPlantData\global_power_plant_database.csv", encoding="utf-8")

powerFile = csv.reader(file)
header = next(powerFile)

country_long = header.index("country_long")
latitude = header.index("latitude")
longitude = header.index("longitude")
source =  header.index("source")
url = header.index("url")
geolocation_source = header.index("geolocation_source")
wepp_id = header.index("wepp_id")
generation_data_source = header.index("generation_data_source")

header.pop(country_long)
header.pop(latitude)
header.pop(longitude)
header.pop(source)
header.pop(url)
header.pop(geolocation_source)
header.pop(wepp_id)
header.pop(generation_data_source)

powerData = []

for row in powerFile:
    row.pop(country_long)
    row.pop(latitude)
    row.pop(longitude)
    row.pop(source)
    row.pop(url)
    row.pop(geolocation_source)
    row.pop(wepp_id)
    row.pop(generation_data_source)
    powerData.append(row)

    # print(row)

#based on the names in index 7
powerDataSolar = []
powerDataHydro = []
powerDataGas = []
powerDataOil = []
powerDataWind = []
powerDataCoal = []
powerDataBiomass = []
powerDataPetcoke = []
powerDataWaste = []
powerDataStorage = []
powerDataNuclear = []
powerDataGeothermal = []
powerDataCogeneration = []
powerDataWaveAndTidal = []
powerDataOther = []

for row in powerData:
    if(row[header.index("primary_fuel")] == "Solar"):
        powerDataSolar.append(row)
    elif(row[header.index("primary_fuel")] == "Hydro"):
        powerDataHydro.append(row)
    elif(row[header.index("primary_fuel")] == "Gas"):
        powerDataGas.append(row)
    elif(row[header.index("primary_fuel")] == "Oil"):
        powerDataOil.append(row)
    elif(row[header.index("primary_fuel")] == "Wind"):
        powerDataWind.append(row)
    elif(row[header.index("primary_fuel")] == "Other"):
        powerDataOther.append(row)
    elif(row[header.index("primary_fuel")] == "Coal"):
        powerDataCoal.append(row)
    elif(row[header.index("primary_fuel")] == "Biomass"):
        powerDataBiomass.append(row)
    elif(row[header.index("primary_fuel")] == "Petcoke"):
        powerDataPetcoke.append(row)
    elif(row[header.index("primary_fuel")] == "Waste"):
        powerDataWaste.append(row)
    elif(row[header.index("primary_fuel")] == "Storage"):
        powerDataStorage.append(row)
    elif(row[header.index("primary_fuel")] == "Nuclear"):
        powerDataNuclear.append(row)
    elif(row[header.index("primary_fuel")] == "Geothermal"):
        powerDataGeothermal.append(row)
    elif(row[header.index("primary_fuel")] == "Cogeneration"):
        powerDataCogeneration.append(row)
    elif(row[header.index("primary_fuel")] == "Wave and Tidal"):
        powerDataWaveAndTidal.append(row)

