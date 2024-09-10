import csv
from geopy.geocoders import Nominatim
import argparse
import ssl
import certifi
import time
import os

ssl_context = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="http", ssl_context=ssl_context)

def main(input_file, city_column, country_column):
    output_file = os.path.splitext(input_file)[0] + "_geocode.csv"  # Générer le nom du fichier de sortie
    with open(input_file, 'r', newline='') as inputFile, open(output_file, 'w', newline='') as outputFile:
        inputData = csv.DictReader(inputFile, delimiter=';')
        fieldnames = inputData.fieldnames + ['adresse', 'longitude', 'latitude']
        outputData = csv.DictWriter(outputFile, fieldnames=fieldnames, delimiter=';')
        outputData.writeheader()
        for ligne in inputData:
            to_geocode = ligne[city_column] + ", " + ligne[country_column]
            try:
                result = geolocator.geocode(to_geocode)
                ligne['adresse'] = result.address
                ligne['longitude'] = result.longitude
                ligne['latitude'] = result.latitude
                print(to_geocode+": "+result.address+" ("+str(result.longitude)+","+str(result.latitude)+")")
            except:
                print("Geocoding failed for:", to_geocode)
            outputData.writerow(ligne)
            time.sleep(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script python qui geocode un CSV avec Nominatim')
    parser.add_argument('-I', '--input', help='Input CSV file containing addresses', required=True)
    parser.add_argument('-c', '--city', help='Column name for cities', required=True)
    parser.add_argument('-p', '--country', help='Column name for countries', required=True)
    args = parser.parse_args()
    main(args.input, args.city, args.country)
