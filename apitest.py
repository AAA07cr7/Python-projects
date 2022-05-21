import requests
url="https://www.flickr.com/services/rest/"

parameters={
      "method":"flickr.photos.getPopular",
      "api_key":"811912e5a76fe0dedf78603a25527bb6",
      "user_id":"195655609@N02",
      "format":"json",
      "nojsoncallback":1
}
    
r=requests.get(url=url,params=parameters)
print(r.status_code)
json_response=r.json()
print(json_response)

if(r.status_code==200 and json_response['stat']=='ok'):
    
    print("API is working")
else:
    print("Not working")
    print("Error found",json_response['message'])
