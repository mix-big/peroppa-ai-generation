import openai
import pyttsx3
import random
import os
from pydub import AudioSegment
from io import BytesIO

# OpenAI APIキーの設定（APIキーを置き換えてください）
openai.api_key = 'your_openai_api_key'

def text_to_speech(text, filename='output.mp3'):
    """
    テキストを音声に変換し、MP3ファイルとして保存する。
    """
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print(f"音声ファイル '{filename}' が保存されました。")
    except Exception as e:
        print(f"音声合成エラー: {e}")

def generate_music(prompt, filename='music_output.mp3'):
    """
    OpenAIを使用して音楽を生成し、MP3ファイルとして保存する。
    ※現在は音楽生成に対応したAPIを使用する必要あり。
    """
    try:
        # OpenAIを使用してテキストベースで音楽を生成（仮の例）
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"次の音楽を作成してください: {prompt}",
            max_tokens=150,
            temperature=0.7,
        )
        music_data = response.choices[0].text.strip()
        # 音楽データのMP3変換処理を追加する場合（例: 外部の音楽生成APIを使う）
        with open(filename, 'w') as file:
            file.write(music_data)  # 実際には音楽データをMP3として保存
        return f"音楽が {filename} として保存されました。"
    except Exception as e:
        print(f"音楽生成エラー: {e}")
        return None

def generate_ambient_sound(filename='ambient_sound.mp3'):
    """
    身近な音を生成（例: 鳥のさえずり、風の音など）。
    仮にローカルファイルから音源を選んで保存する方法に変更。
    """
    ambient_sounds = [
        "風の音",
        "鳥のさえずり",
        "雨の音",
        "波の音",
        "街の雑音"
    ]
    
    sound = random.choice(ambient_sounds)
    
    # 環境音ファイルがローカルにあると仮定
    sound_files = {
        "風の音": "sounds/wind.mp3",
        "鳥のさえずり": "sounds/bird_chirping.mp3",
        "雨の音": "sounds/rain.mp3",
        "波の音": "sounds/waves.mp3",
        "街の雑音": "sounds/street_noise.mp3"
    }
    
    if sound in sound_files:
        sound_file = sound_files[sound]
        if os.path.exists(sound_file):
            # サウンドファイルをMP3としてコピー
            output_filename = os.path.join('output', filename)
            os.makedirs(os.path.dirname(output_filename), exist_ok=True)
            os.system(f"cp {sound_file} {output_filename}")
            return f"{sound}の音が {filename} として保存されました。"
        else:
            return f"サウンドファイル '{sound_file}' が見つかりません。"
    else:
        return "無効な音声タイプです。"

# サンプルの呼び出し
text_to_speech("こんにちは、元気ですか？", "hello.mp3")
generate_music("リラックスできるクラシック音楽", "relaxing_music.mp3")
generate_ambient_sound("ambient_sound.mp3")
