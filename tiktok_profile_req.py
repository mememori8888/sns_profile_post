
import requests
import csv
import json


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
        json_data = response.json()

    # jsonファイルで出力
    with open("snapshot_id.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    print("Snapshot id has been saved to snapshot_id.json")


#proflileをリクエストしてゲット

api_Key = get_api_key_from_snapshot()

if api_Key:
    print(f"API Key found: {api_Key}")
else:
    print("API Key not found.")

profile_req(api_Key)
#jsonファイルが出力される。
# 完了までに時間がかかるため、brightdataの画面で確認してもらう？
# ファイルをpfofile_reqとstatuscheck,downloadに分ける。

