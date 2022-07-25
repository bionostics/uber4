import urllib.parse
import requests
from geopy.geocoders import Nominatim
import streamlit as st
from googleplaces import GooglePlaces, types, lang
st.set_page_config(page_title="Hospital Finder", page_icon="🏥")
st.markdown("# Locate the Nearest Hospital")
st.write(
    """Enter your current address as well the city/state. The algorithm uses geomapping to first find your latitude and longtitude, finds nearest hospitals, then converts them into addresses.""")
API_KEY = 'AIzaSyAiegc8hmrCGr2ip_hubPicHCaTHpjjrSE'
google_places = GooglePlaces(API_KEY)
address = st.text_input("Enter your address:")
if st.button('Find Hospital'):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    long = response[0]["lon"]
    query_result = google_places.nearby_search(
        lat_lng={'lat':lat,'lng':long},
        radius = 5000,
        types = [types.TYPE_HOSPITAL]
    )
    if query_result.has_attributions:
        print(query_result.html_attributions)
    if len(query_result.places)==0:
        st.write("There are no hospitals in a 5 KM proximity.")
    for place in query_result.places:
        st.subheader(place.name)
        lat = place.geo_location['lat']
        long = place.geo_location['lng']
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = str(lat) + ", " + str(long)
        location = locator.reverse(coordinates)
        st.write(location.address)
