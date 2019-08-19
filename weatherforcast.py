import requests,json

api_key="3970102be5b0eadb0abd32e2860e7bcc"

basic_url="http://api.openweathermap.org/data/2.5/weather?"

#getting ip address of the machie
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']

#getting current location
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
lon=geo_data['longitude']
lat=geo_data['latitude']


#zip_code=input("Enter zipcode of ur area\n")
#complete_url=basic_url+"appid=" + api_key+"&lat="+str(lat)+"&lon="+str(lon)
complete_final_url="{}appid={}&lat={}&lon={}".format(basic_url,api_key,lat,lon)


response=requests.get(complete_final_url)

x=response.json()

y=x.get('main')
print(geo_data['city'])
for key,value in y.items():
    print(key,":",value,"\n")
