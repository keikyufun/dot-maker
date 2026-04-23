import os
import csv
import sys
from PIL import Image

def generate_image(folder_path):
    # パスの定義
    data_path = os.path.join(folder_path, 'data.csv')
    colors_path = os.path.join(folder_path, 'colors.txt')
    config_path = os.path.join(folder_path, 'config.txt')

    # ファイルチェック
    if not all(os.path.exists(p) for p in [data_path, colors_path, config_path]):
        print("エラー: 必要なファイル(data.csv, colors.txt, config.txt)が足りません。")
        return

    # 1. ピクセルサイズ取得
    with open(config_path, 'r') as f:
        p_size = int(f.read().strip())

    # 2. カラーリスト取得 (行番号と対応)
    color_map = {}
    with open(colors_path, 'r') as f:
        for i, line in enumerate(f, start=1):
            code = line.strip()
            if code:
                color_map[str(i)] = code

    # 3. CSVデータ読み込み
    grid = []
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            grid.append([cell.strip() for cell in row])

    # 4. 画像作成 (RGBAで透明背景)
    rows = len(grid)
    cols = len(grid[0])
    img = Image.new("RGBA", (cols * p_size, rows * p_size), (0, 0, 0, 0))

    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val == "0" or val not in color_map:
                continue # 0 または 色指定がない場合は描画しない(透明)
            
            # 塗りつぶし処理
            color = color_map[val]
            box = (c_idx * p_size, r_idx * p_size, (c_idx + 1) * p_size, (r_idx + 1) * p_size)
            img.paste(Image.new("RGBA", (p_size, p_size), color), box)

    # 保存
    out_name = os.path.join(folder_path, "output.png")
    img.save(out_name)
    print(f"成功: {out_name} を書き出しました。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python convert.py フォルダ名")
    else:
        generate_image(sys.argv[1])