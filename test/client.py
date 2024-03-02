import requests

url = 'http://{server ip}/uploadfile/'
filedirectory = '{file directory}'

with open(filedirectory, 'rb') as f:
	res = requests.post(url, files = {'file': f})
	if res.status_code == 200:
		print(res.status_code, "Image Upload Success")
	else:
		print(res.status_code, "Error Occured")
