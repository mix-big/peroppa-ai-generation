import openai

openai.api_key = 'your_openai_api_key'

def generate_code_from_prompt(language, prompt, model="gpt-4", max_tokens=150, temperature=0.7):
    """
    指定されたプログラミング言語に応じて、コードを生成する関数。
    
    :param language: プログラミング言語 ('java', 'html', 'css', 'py' など)
    :param prompt: コード生成のためのテキストプロンプト
    :param model: 使用するOpenAIのモデル（デフォルトはgpt-4）
    :param max_tokens: 生成するトークンの最大数
    :param temperature: 出力のランダム性を決めるパラメータ（デフォルトは0.7）
    :return: 生成されたコード
    """
    
    # 言語ごとのプロンプトをカスタマイズ
    language_prompts = {
        "java": f"Javaで以下の機能を実現するコードを生成してください:\n{prompt}",
        "html": f"HTMLで以下の内容を表現するコードを生成してください:\n{prompt}",
        "css": f"CSSで以下のデザインを実現するコードを生成してください:\n{prompt}",
        "py": f"Pythonで以下の機能を実現するコードを生成してください:\n{prompt}",
    }

    if language not in language_prompts:
        raise ValueError("サポートされていない言語です。'java', 'html', 'css', 'py' のいずれかを指定してください。")

    prompt_with_language = language_prompts[language]

    try:
        # OpenAI APIリクエストの送信
        response = openai.Completion.create(
            model=model,
            prompt=prompt_with_language,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        # APIレスポンスから生成されたコードを返す
        generated_code = response.choices[0].text.strip()
        return generated_code
    except openai.error.OpenAIError as e:
        print(f"OpenAI APIのエラー: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

    return None
