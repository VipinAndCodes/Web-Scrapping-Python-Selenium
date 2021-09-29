from pprint import pprint
import os
import googlemaps # pip install googlemaps
#import win32com.client as win32

API_KEY = open('API_KEY.txt').read()
map_client = googlemaps.Client(API_KEY)
