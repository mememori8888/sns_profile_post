
import requests
import csv
import json
import time

def get_api_key_from_snapshot(filepath="api_key.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            api_key = data.get("api_key")  # Use .get() to avoid KeyError
            if api_key is not None:
                return api_key
            else:
                print("Error: 'api_key' key not found in JSON.")
                return None
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from file: {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def profile_req(api_key):
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": f"Bearer {api_key}",
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
        json_data = response.json()

    # jsonファイルで出力
    with open("snapshot_id.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    print("Snapshot id has been saved to snapshot_id.json")

def get_snapshot_id(filepath = 'snapshot_id.json'):
    with open(filepath,'r',encoding='utf-8') as f:
        data = json.load(f)
        snapshot_id = data.get('snapshot_id')
        return snapshot_id

def status_check(snapshot_id):
    # ステータスをチェック
    url = f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"
    headers = {
        "Authorization": f"Bearer {api_Key}",
    }

    response = requests.get(url, headers=headers)
    print(response.json())
    json_data = response.json()

    # jsonファイルで出力
    with open("snapshot_status.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    print("Snapshot status has been saved to snapshot_status.json")



def get_snapshot_info(filepath="snapshot_status.json"):
    """
    Reads the snapshot_status.json file, extracts the status and snapshot_id,
    and returns them as a dictionary.

    Args:
        filepath (str): The path to the snapshot_status.json file.
                        Defaults to "snapshot_status.json" in the current directory.

    Returns:
        dict: A dictionary containing the status and snapshot_id, or None if an error occurs.
              Example: {"status": "completed", "snapshot_id": "s_m8iqwk2m27i8lm63nq"}
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            status = data.get("status")  # Use .get() to avoid KeyError
            snapshot_id = data.get("snapshot_id")  # Use .get() to avoid KeyError
            if status is not None and snapshot_id is not None:
                return {"status": status, "snapshot_id": snapshot_id}
            else:
                print("Error: 'status' or 'snapshot_id' key not found in JSON.")
                return None
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from file: {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# スナップショットにアクセスしてダウンロード。
def download_file(snapshot_id,api_key):
    url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    params = {
        "format": "csv",
    }

    response = requests.get(url, headers=headers, params=params)
    print(response)
    # Check if the request was successful
    # ステータスがランニングではなかったらに変更する。
    if response.status_code == 200:
        # Write the content to a CSV file
        with open('profile.csv', 'wb') as file:
            file.write(response.content)
        print("CSV file has been created successfully.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

#proflileをリクエストしてゲット

api_Key = get_api_key_from_snapshot()

if api_Key:
    print(f"API Key found: {api_Key}")
else:
    print("API Key not found.")

profile_req(api_Key)
#jsonファイルが出力される。
# 完了までに時間がかかるため、30分待機
time.sleep(1800)
# スナップショットを確認し、ファイルダウンロード


# statuscheck
snapshot_id = get_snapshot_id()
#snapshot_statusファイルの出力
status_check(snapshot_id)
snapshot_info = get_snapshot_info()
status = snapshot_info["status"]
snapshot_id = snapshot_info["snapshot_id"]
print(f"Status: {status}")
print(f"Snapshot ID: {snapshot_id}")
if status == 'ready':
    download_file(snapshot_id,api_Key)
elif status == 'running':
    print("still running...")    
else:
    print("Failed to retrieve snapshot information.")

