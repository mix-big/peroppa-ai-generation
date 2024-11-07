import requests
import os
import uuid
from datetime import datetime

def generate_image_from_text(text, api_key, output_dir='images', file_format='png'):
    """
    テキストから画像を生成し、保存する関数。
    
    :param text: 画像生成のためのテキストプロンプト
    :param api_key: DeepAI APIキー
    :param output_dir: 画像を保存するディレクトリ（デフォルトは'images'）
    :param file_format: 画像のファイル形式（デフォルトは'png'）
    :return: 画像の保存パス（成功した場合）
    """
    url = 'https://api.deepai.org/api/text2img'
    headers = {'api-key': api_key}
    
    # リクエストを送信
    try:
        response = requests.post(url, data={'text': text}, headers=headers, timeout=30)
        response.raise_for_status()  # ステータスコードが200でない場合に例外を発生させる
        
        # 画像URLを取得
        image_url = response.json().get('output_url')
        if not image_url:
            raise ValueError("画像のURLが返されませんでした。")
        
        # 画像データをダウンロード
        img_data = requests.get(image_url, timeout=30).content
        
        # 保存ディレクトリがなければ作成
        os.makedirs(output_dir, exist_ok=True)
        
        # ファイル名を動的に生成（ユニークな名前を使う）
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{uuid.uuid4()}.{file_format}"
        file_path = os.path.join(output_dir, unique_filename)
        
        # 画像ファイルを保存
        with open(file_path, 'wb') as handler:
            handler.write(img_data)
        
        print(f"画像を保存しました: {file_path}")
        return file_path
    
    except requests.exceptions.RequestException as e:
        print(f"HTTPリクエストエラー: {e}")
    except ValueError as ve:
        print(f"データエラー: {ve}")
    except Exception as e:
        print(f"予期しないエラー: {e}")
    
    return None

# サンプルの呼び出し
api_key = 'your_deepai_api_key_here'  # APIキーを設定
image_path = generate_image_from_text("A beautiful sunset over the ocean", api_key)
