# Peroppa AI Generation

Peroppa AI Generation は、音声生成、画像生成、ビデオ生成、プログラム生成、テキスト生成など、様々なAI生成機能を提供するPythonライブラリです。このライブラリは、OpenAI APIを利用して、テキストに基づいた多様なコンテンツを生成することができます。

## 機能

- **音声生成** (`audio.py`): テキストから音声を合成したり、音楽や身近な音を生成します。
- **画像生成** (`image.py`): テキストプロンプトを基に画像を生成します。
- **ビデオ生成** (`video.py`): 画像リストを基に動画を作成します。
- **プログラム生成** (`program.py`): 指定したプログラミング言語でコードを生成します。
- **テキスト生成** (`text.py`): 与えられたプロンプトを基にテキストを生成します。

## インストール

1. リポジトリをクローンします：

    ```bash
    git clone https://github.com/mix-big/peroppa-ai-generation/
    cd peroppa_ai_generation
    ```

2. 必要なパッケージをインストールします：

    ```bash
    pip install -r requirements.txt
    ```

    `requirements.txt` には以下の依存パッケージが含まれています：

    - `openai` (テキスト生成)
    - `pyttsx3` (音声合成)
    - `requests` (画像生成)
    - `opencv-python` (ビデオ生成)
    
3. OpenAI APIキーを設定します：
    - `.env` ファイルをプロジェクトルートに作成し、`OPENAI_API_KEY` 環境変数を設定してください。
    
    例:
    
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## 使用方法

### 1. 音声生成
音声合成、音楽生成、または身近な音を生成することができます。

```python
from peroppa_ai_generation import pag

# 音声合成
pag.a.s("こんにちは、私はAIです。")

# 音楽生成
pag.a.m("ロマンチックなピアノ曲")

# 身近な音生成
pag.a.n()
