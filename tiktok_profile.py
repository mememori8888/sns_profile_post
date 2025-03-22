import requests
import csv
import json
import time
from datetime import datetime

API_TOKEN = "bda3c78f-ca73-4eb9-8da4-db3bd3e401a1"

def read_urls_from_csv(input_file):
    """CSVファイルからTikTokのURLを読み込む"""
    urls = []
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダーをスキップ
        for row in reader:
            if row and row[0].strip():  # 空行でない場合
                urls.append({"url": row[0].strip()})
    return urls

def fetch_tiktok_profiles(urls):
    """Bright Data APIを使用してTikTokプロフィール情報を取得"""
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "dataset_id": "gd_l1villgoiiidt09ci",
        "include_errors": "true",
    }
    data = {
        "deliver": {
            "type": "immediate"  # 即時レスポンスを要求
        },
        "input": urls
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"APIリクエストエラー: {e}")
        return None

def save_to_csv(data, output_file):
    """結果をCSVファイルに保存"""
    if not data or 'results' not in data:
        print("保存するデータがありません")
        return

    # 結果から必要なフィールドを抽出
    fieldnames = [
        'username', 'nickname', 'bio', 'followers_count', 
        'following_count', 'likes_count', 'video_count',
        'verified', 'private_account', 'fetch_time'
    ]

    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for result in data['results']:
            if 'data' in result:
                profile = result['data']
                row = {
                    'username': profile.get('username', ''),
                    'nickname': profile.get('nickname', ''),
                    'bio': profile.get('bio', ''),
                    'followers_count': profile.get('followers_count', 0),
                    'following_count': profile.get('following_count', 0),
                    'likes_count': profile.get('likes_count', 0),
                    'video_count': profile.get('video_count', 0),
                    'verified': profile.get('verified', False),
                    'private_account': profile.get('private_account', False),
                    'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                writer.writerow(row)

def main():
    input_file = 'tiktok_urls.csv'  # 入力CSVファイル
    output_file = f'tiktok_profiles_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'  # 出力CSVファイル

    print("TikTokプロフィール情報取得を開始します...")
    
    # URLの読み込み
    urls = read_urls_from_csv(input_file)
    if not urls:
        print("URLが見つかりませんでした。CSVファイルを確認してください。")
        return

    print(f"{len(urls)}件のURLを読み込みました。APIリクエストを実行します...")

    # APIリクエスト
    results = fetch_tiktok_profiles(urls)
    if not results:
        print("データの取得に失敗しました。")
        return

    # 結果の保存
    save_to_csv(results, output_file)
    print(f"処理が完了しました。結果は{output_file}に保存されました。")

if __name__ == "__main__":
    main()