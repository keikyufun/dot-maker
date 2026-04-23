import os
import csv
import json
import sys
from PIL import Image

def generate_image_from_folder(folder_path):
    # 1. ファイルパスの設定
    data_file = os.path.join(folder_path, 'data.csv')
    color_file = os.path.join(folder_path, 'colors.json')
    config_file = os.path.join(folder_path, 'config.txt')

    # 2. ピクセルサイズの読み込み
    with open(config_file, 'r') as f:
        pixel_size = int(f.read().strip())

    # 3. カラー設定の読み込み
    with open(color_file, 'r') as f:
        color_map = json.load(f)

    # 4. 数値データの読み込み
    grid = []
    with open(data_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            grid.append([cell.strip() for cell in row])

    # 5. 画像サイズの計算
    rows = len(grid)
    cols = len(grid[0])
    img_width = cols * pixel_size
    img_height = rows * pixel_size

    # 6. 画像の生成
    # "RGB" モードで新しい画像を作成
    new_img = Image.new("RGB", (img_width, img_height), "white")
    
    for r_idx, row in enumerate(grid):
        for c_idx, value in enumerate(row):
            color_code = color_map.get(value, "#FFFFFF") # 定義がない場合は白
            
            # 指定されたピクセルサイズで塗りつぶす
            left = c_idx * pixel_size
            top = r_idx * pixel_size
            right = left + pixel_size
            bottom = top + pixel_size
            
            new_img.paste(color_code, [left, top, right, bottom])

    # 7. 保存
    output_path = os.path.join(folder_path, 'output.png')
    new_img.save(output_path)
    print(f"画像を作成しました: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python script.py [フォルダ名]")
    else:
        generate_image_from_folder(sys.argv[1])