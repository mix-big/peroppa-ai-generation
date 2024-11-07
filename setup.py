# setup.py

from setuptools import setup, find_packages

setup(
    name='peroppa_ai_generation',    # パッケージ名
    version='0.1.0',                 # バージョン番号
    packages=find_packages(),        # パッケージを自動的に検出
    install_requires=[               # 必要な依存パッケージ
        'openai',                     # OpenAI APIを使用するため
        'pyttsx3',                    # 音声合成のため
        'requests',                   # 画像生成のため
        'opencv-python',              # ビデオ生成のため
        'python-dotenv',              # 環境変数の管理
    ],
    include_package_data=True,       # MANIFEST.in に従ってファイルを含める
    long_description=open('README.md').read(),  # README.md をパッケージに含める
    long_description_content_type='text/markdown',
    author='Peroppa Computer',       # 作者名を Peroppa Computer に変更
    author_email='mixbig3343@gmail.com',  # ご提供いただいたメールアドレス
    description='A library for generating AI-driven content like text, audio, images, and more.',
    url='https://github.com/mix-big/peroppa-ai-generation',  # GitHub リンク
    classifiers=[                    # パッケージの分類情報
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
