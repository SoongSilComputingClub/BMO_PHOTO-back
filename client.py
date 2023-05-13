import requests

url = 'http://146.56.106.142/uploadfile/'
filename = 'Cyberpunk.png'

with open(filename, 'rb') as f:
	res = requests.post(url, files = {'file': f})
	if res.status_code == 200:
		print(res.status_code, "Image Upload Success")
	else:
		print(res.status_code, "Error Occured")
