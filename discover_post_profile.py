import requests
import json
url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
	"Authorization": "f518572c-5a23-42d9-b30c-f93632f129c5",
}
params = {
	"dataset_id": "gd_lu702nij2f790tmv9h",
	"include_errors": "true",
	"type": "discover_new",
	"discover_by": "profile_url",
}
# files = {"data": ("url.csv", open("url.csv", "rb"), "text/csv")}
with open("url.csv", "rb") as f:
    files = {"data": ("data.csv", f, "text/csv")} #url.csvの内容をdata.csvという名前で送信する。
print(files)
response = requests.post(url, headers=headers, params=params, files=files)
print(response.json())
json_data = response.json()
print(json_data)  # デバッグ用

with open("output.json", mode='w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)  # json.dumps()を使用
# # Set API key in headers
# # f518572c-5a23-42d9-b30c-f93632f129c5 自分用の為、使わないこと。
# headers = {
#     'Authorization': 'f518572c-5a23-42d9-b30c-f93632f129c5',
#     'Content-Type': 'application/json'
# }




# filepath = "url.csv"
# first_column = []
# with open(filepath, 'r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row:  # 空行をスキップ
#             first_column.append(row[0])


# for account_url in first_column:
#     # Request payload
#     payload = {
#         "profile_url": f"{account_url}",
#         "num_of_posts": 1,  # Number of posts to retrieve
#         "start_date":"02-01-2025",
#         "end_date":"03-01-2025",
#         "what_to_collect":"Posts",
#     }
    
#     # Send API request
#     response = requests.post(url, headers=headers, json=payload, verify=False)

#     # Get response in JSON format
#     data = response.json()

#     # Display results
#     print(data)
