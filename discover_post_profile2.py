import requests

url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
    "Authorization": "Bearer API_TOKEN"  # API_TOKENを実際のトークンに置き換えてください
}
params = {
    "dataset_id": "gd_lu702nij2f790tmv9h",
    "include_errors": "true",
    "type": "discover_new",
    "discover_by": "profile_url"
}
files = {
    "data": open("path/to/your/file.csv", "rb")  # ファイルパスを実際のパスに置き換えてください
}

try:
    response = requests.post(url, headers=headers, params=params, files=files)
    response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
    print(response.json())  # レスポンスをJSONとして表示
except requests.exceptions.RequestException as e:
    print(f"リクエストエラーが発生しました: {e}")
except ValueError as e:
    print(f"JSONデコードエラーが発生しました: {e}")
except IOError as e:
    print(f"ファイル操作エラーが発生しました: {e}")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
finally:
    if "files" in locals():
      files["data"].close() #ファイルを閉じる。