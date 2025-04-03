import requests
import json


url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
	"Authorization": "Bearer bda3c78f-ca73-4eb9-8da4-db3bd3e401a1",
	"Content-Type": "application/json",
}
params = {
	"dataset_id": "gd_lk5ns7kz21pck8jpis",
	"include_errors": "true",
	"type": "discover_new",
	"discover_by": "url",
}

with open('data.json', 'r') as f:
    raw_data = json.load(f)

# Create mapping of URLs to their corresponding IDs
id_mapping = {item['url']: {'ai_id': item['ai_id'], 'uc_id': item['uc_id']} for item in raw_data}

# Remove ai_id and uc_id from each item
data = []
for item in raw_data:
    filtered_item = {k: v for k, v in item.items() if k not in ['ai_id', 'uc_id']}
    data.append(filtered_item)

response = requests.post(url, headers=headers, params=params, json=data)
response_data = response.json()

# Add ai_id and uc_id to response data based on URL
if isinstance(response_data, dict) and 'data' in response_data:
    for item in response_data['data']:
        if 'url' in item and item['url'] in id_mapping:
            item.update(id_mapping[item['url']])

# Save response to JSON file
output_file = 'snapshot_id_post_insta.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(response_data, f, ensure_ascii=False, indent=4)

print(f"Response has been saved to {output_file}")