# ファイルパスの設定
input_file_path = "original/ghec.2022-11-28.json"
paths_output_file = "original/paths.json"
components_output_file = "original/components.json"

import json

# JSONファイルを読み込む関数
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# JSONオブジェクトをファイルに書き出す関数
def write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

try:
    # JSONのロード
    data = load_json(input_file_path)

    # paths と components の抽出とファイル書き出し
    if "paths" in data:
        write_json(paths_output_file, data["paths"])
        print(f"Paths data was written to {paths_output_file}")
    else:
        print("No 'paths' found in the JSON file.")

    if "components" in data:
        write_json(components_output_file, data["components"])
        print(f"Components data was written to {components_output_file}")
    else:
        print("No 'components' found in the JSON file.")

except FileNotFoundError:
    print(f"Error: File {input_file_path} not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please check the input file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
