from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

api = SentinelAPI('*****', '*****', 'https://scihub.copernicus.eu/dhus')

footprint = geojson_to_wkt(read_geojson('testAPIpoly.geojson'))

products = api.query(footprint, cloudcoverpercentage = (0,10))

#this works
api.download_all(products)

https://gis.stackexchange.com/questions/289001/sentinelsat-python-api-error-in-download
https://gist.github.com/wavded/1200773?short_path=99c1af9