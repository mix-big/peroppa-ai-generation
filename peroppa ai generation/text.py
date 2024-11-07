# peroppa_ai_generation/text.py

import openai

openai.api_key = 'your_openai_api_key'  # OpenAI APIキーを設定

def generate_text_from_prompt(prompt, model="gpt-4", max_tokens=150, temperature=0.7):
    """
    指定したプロンプトに基づいてテキストを生成する関数。
    
    :param prompt: テキスト生成のプロンプト（指示や質問など）
    :param model: 使用するOpenAIのモデル（デフォルトは"gpt-4"）
    :param max_tokens: 生成する最大トークン数（デフォルトは150）
    :param temperature: テキストの創造性の度合い（0.0〜1.0の範囲、デフォルトは0.7）
    :return: 生成されたテキスト
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        generated_text = response.choices[0].text.strip()
        return generated_text
    except Exception as e:
        print(f"テキスト生成中にエラーが発生しました: {e}")
        return None
