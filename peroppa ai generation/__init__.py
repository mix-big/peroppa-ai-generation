# peroppa_ai_generation/__init__.py

from .audio import text_to_speech, generate_music, generate_ambient_sound
from .image import generate_image_from_text, generate_image_from_prompt
from .video import generate_video_from_images
from .program import generate_code
import openai

class Pag:
    """
    Peroppa AI Generationのアクションを管理するクラス。
    各アクションはこのクラスを通じて呼び出すことができます。
    """
    
    def __init__(self):
        # 各アクションのショートカットを設定
        self.a = self.AudioActions()
        self.i = self.ImageActions()
        self.v = self.VideoActions()
        self.p = self.ProgramActions()
        self.t = self.TextGenerationActions()  # テキスト生成を追加
    
    class AudioActions:
        def __init__(self):
            pass
        
        def s(self, *args):
            """ 音声合成 """
            if len(args) < 1:
                print("音声合成のテキストが指定されていません。")
                return
            text_to_speech(*args)

        def m(self, *args):
            """ 音楽生成 """
            if len(args) < 1:
                print("音楽生成のプロンプトが指定されていません。")
                return
            generate_music(*args)

        def n(self, *args):
            """ 身近な音生成 """
            generate_ambient_sound(*args)

    class ImageActions:
        def __init__(self):
            pass
        
        def t(self, *args):
            """ 画像生成 """
            if len(args) < 1:
                print("画像生成のプロンプトが指定されていません。")
                return
            generate_image_from_text(*args)

    class VideoActions:
        def __init__(self):
            pass
        
        def t(self, *args):
            """ ビデオ生成 """
            if len(args) < 1:
                print("ビデオ生成の画像リストが指定されていません。")
                return
            generate_video_from_images(*args)

    class ProgramActions:
        def __init__(self):
            pass
        
        def t(self, *args):
            """ プログラム生成 """
            if len(args) < 2:
                print("プログラム生成に必要な引数が不足しています。")
                return
            generate_code(*args)
    
    class TextGenerationActions:
        def __init__(self):
            pass
        
        def t(self, prompt, model="gpt-4", max_tokens=150):
            """ テキスト生成 """
            try:
                openai.api_key = 'your_openai_api_key'  # OpenAI APIキーの設定
                
                response = openai.Completion.create(
                    model=model,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=0.7
                )
                generated_text = response.choices[0].text.strip()
                print(f"生成されたテキスト:\n{generated_text}")
                return generated_text
            except Exception as e:
                print(f"テキスト生成中にエラーが発生しました: {e}")
                return None


# インスタンスを作成
pag = Pag()
