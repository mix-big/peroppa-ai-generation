# peroppa_ai_generation/video.py
import cv2
import numpy as np

def generate_video_from_images(images, output_filename='output_video.mp4', fps=24):
    """
    画像リストから動画を生成する関数。
    
    :param images: 画像のリスト（NumPy配列形式）
    :param output_filename: 出力する動画のファイル名
    :param fps: 動画のフレームレート（デフォルトは24）
    """
    height, width, layers = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4形式
    video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
    
    for image in images:
        video.write(image)
    
    video.release()
    print(f"動画を保存しました: {output_filename}")
