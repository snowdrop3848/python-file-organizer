import argparse
from pathlib import Path
print("文件整理工具开始运行")
document_extensions = [".txt",".pdf",".docx"]
photo_extensions = [".jpg",".png"]
music_extensions= [".mp3",".wav"]
programs = [".py",".cpp"]

parser = argparse.ArgumentParser(description="按扩展名整理文件")
parser.add_argument("folder", help="待整理文件夹的路径")
args = parser.parse_args()
folder = Path(args.folder)
print(folder)
def classify_file(suffix):
    suffix = suffix.lower()
    if suffix in document_extensions:
        return "文档"
    elif suffix in photo_extensions:
        return "图片"
    elif  suffix in music_extensions:
        return "音频"
    elif suffix in programs:
        return "程序"
    else:
        return "其他"

for item in list(folder.iterdir()):
    if item.is_file():
        category = classify_file (item.suffix)
        target_folder = folder / category
        target_path = target_folder / item.name
        #print(item.name , "->" , target_path)

        if(target_path.exists()):
            print("跳过：目标已存在")
            continue
        target_folder.mkdir(exist_ok=True)
        item.rename(target_path)
        print(f"已移动：{item.name} -> {target_path}")
