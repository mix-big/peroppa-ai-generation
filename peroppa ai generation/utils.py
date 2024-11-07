from peroppa_ai_generation.utils import setup_logger, validate_input, check_file_exists, create_file, get_current_timestamp, create_directory, dynamic_function_call

# ログの設定
logger = setup_logger()
logger.info("This is an info message.")
logger.error("This is an error message.")

# 入力検証
try:
    validate_input(10, int)  # 正しい
    validate_input("string", int)  # エラー
except ValueError as e:
    logger.error(e)

# ファイルの存在確認
try:
    check_file_exists("some_file.txt")
except FileNotFoundError as e:
    logger.error(e)

# ファイル作成
create_file("example.txt", "This is an example file content.")

# タイムスタンプの取得
timestamp = get_current_timestamp()
print(f"Current Timestamp: {timestamp}")

# ディレクトリ作成
create_directory("new_directory")

# 動的に関数を呼び出す
result = dynamic_function_call(logger, "info", "Dynamically called info message!")
print(result)
