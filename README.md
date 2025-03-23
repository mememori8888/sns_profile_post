
profile.pyはtiktok_urls.csvからAPIリクエストして、30分後にprofile.csvを出力します。
recent_post.pyはtiktok_post.csvからAPIにリクエストして、30分後にpost.csvを出力します。

csvファイルのダウンロードがうまくいかなかった場合は、公式ページのステータスを確認後、
tiktok_profile_donwload.pyおよびtiktok_post_download.pyを実行することで直前のリクエストした内容のcsvファイルをダウンロードできます。


