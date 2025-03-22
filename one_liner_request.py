import requests
import csv


url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
    "Authorization": "Bearer bda3c78f-ca73-4eb9-8da4-db3bd3e401a1",
}
params = {
    "dataset_id": "gd_l1villgoiiidt09ci",
    "include_errors": "true",
}

# Use 'with' statement to open the file
with open("tiktok_urls.csv", "rb") as file:
    files = {"data": ("tiktok_urls.csv", file, "text/csv")}
    response = requests.post(url, headers=headers, params=params, files=files, verify=False)
    print(response.json())


# ステータスをチェック
url = "https://api.brightdata.com/datasets/v3/progress/s_m8iqwk2m27i8lm63nq"
headers = {
	"Authorization": "Bearer bda3c78f-ca73-4eb9-8da4-db3bd3e401a1",
}

response = requests.get(url, headers=headers)
print(response.json())

# スナップショットにアクセスしてダウンロード。
url = "https://api.brightdata.com/datasets/v3/snapshot/s_m8iqwk2m27i8lm63nq"
headers = {
	"Authorization": "Bearer bda3c78f-ca73-4eb9-8da4-db3bd3e401a1",
}
params = {
	"format": "csv",
}

response = requests.get(url, headers=headers, params=params)
# Check if the request was successful
# ステータスがランニングではなかったらに変更する。
if response.status_code == 200:
    # Write the content to a CSV file
    with open('output.csv', 'wb') as file:
        file.write(response.content)
    print("CSV file has been created successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")