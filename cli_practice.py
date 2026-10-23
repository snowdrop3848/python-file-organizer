import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="练习接收文件夹路径")
parser.add_argument("folder", help="待整理文件夹的路径")

args = parser.parse_args()

print("解析结果：", args)
print("路径字符串：", args.folder)

folder = Path(args.folder)

print("路径是否存在：", folder.exists())
print("是否为文件夹：", folder.is_dir())