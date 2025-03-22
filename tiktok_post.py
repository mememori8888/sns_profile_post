import requests

url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
	"Authorization": "Bearer bda3c78f-ca73-4eb9-8da4-db3bd3e401a1",
	"Content-Type": "application/json",
}
params = {
	"dataset_id": "gd_lu702nij2f790tmv9h",
	"include_errors": "true",
	"type": "discover_new",
	"discover_by": "profile_url",
}
data = [
	{"url":"https://www.tiktok.com/@babyariel","num_of_posts":1,"posts_to_not_include":["7383783899308117249"],"start_date":"02-01-2025","end_date":"03-21-2025","what_to_collect":"Posts & Reposts","post_type":""},
	{"url":"https://www.tiktok.com/@sonyakisa8","num_of_posts":1,"posts_to_not_include":["7383783899308117249","7377955161429363999"],"start_date":"02-01-2025","end_date":"03-21-2025","what_to_collect":"Posts & Reposts","post_type":""},
	{"url":"https://www.tiktok.com/@smolfrenz","num_of_posts":1,"start_date":"02-01-2025","end_date":"03-21-2025","what_to_collect":"Posts & Reposts","post_type":""},
]

response = requests.post(url, headers=headers, params=params, json=data)
print(response.json())