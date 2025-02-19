# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# 本代码受 Apache License 2.0 许可。
# 你只能在符合该许可证的情况下使用本代码。
# 许可证可在以下网址查看：
# http://www.apache.org/licenses/LICENSE-2.0
# 除非法律要求或书面同意，否则代码按“原样”提供，
# 不包含任何明示或暗示的保证。

import os  # 操作系统相关的文件路径、目录操作
from tqdm import tqdm  # 进度条显示库
import xml.etree.ElementTree as ET  # 处理 XML 文件
from sacremoses import MosesTokenizer  # 用于分词的 MosesTokenizer
from pathlib import Path  # 处理文件和目录路径的模块
import argparse  # 解析命令行参数


def moses_cut(in_file, out_file, lang):
    """
    使用 MosesTokenizer 对文本进行分词，并将结果保存到新的文件中。

    :param in_file: 输入文件路径（待分词的文本）
    :param out_file: 输出文件路径（分词后的文本）
    :param lang: 语言代码（如 'en' 表示英语，'de' 表示德语）
    """
    mt = MosesTokenizer(lang=lang)  # 初始化 Moses 分词器
    out_f = open(out_file, "w", encoding="utf8")  # 以 UTF-8 编码打开输出文件（写入模式）

    with open(in_file, "r", encoding="utf8") as f:  # 以 UTF-8 编码打开输入文件（读取模式）
        for line in f.readlines():  # 按行读取文件内容
            line = line.strip()  # 去除行首和行尾的空白字符
            if not line:  # 跳过空行
                continue
            cut_line = mt.tokenize(line, return_str=True)  # 使用 MosesTokenizer 进行分词
            out_f.write(cut_line.lower() + "\n")  # 转换为小写并写入输出文件

    out_f.close()  # 关闭输出文件


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser()

    # 定义 --pair_dir 参数（必须提供），表示包含语言对文件的目录
    parser.add_argument(
        "-p",
        "--pair_dir",
        default=None,
        type=str,
        help="The directory which contains language pair files.",
    )

    # 定义 --dest_dir 参数（必须提供），表示处理后数据的存放目录
    parser.add_argument(
        "-d",
        "--dest_dir",
        default=None,
        type=str,
        help="The destination directory to save processed train, dev and test file.",
    )

    # 定义 --src_lang 参数，表示源语言（默认为德语 'de'）
    parser.add_argument("--src_lang", default="de", type=str, help="source language")

    # 定义 --trg_lang 参数，表示目标语言（默认为英语 'en'）
    parser.add_argument("--trg_lang", default="en", type=str, help="target language")

    # 解析命令行参数
    args = parser.parse_args()

    # 检查 pair_dir 参数是否提供，若未提供，则抛出错误
    if not args.pair_dir:
        raise ValueError("Please specify --pair_dir")

    # 如果目标目录不存在，则创建该目录
    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)

    # 获取本地数据存放路径
    local_data_path = Path(args.pair_dir)

    # 获取目标数据存放路径
    data_dir = Path(args.dest_dir)

    # 遍历 ['train', 'val', 'test'] 三个数据集模式，分别进行分词
    for mode in ["train", "val", "test"]:
        # 对源语言文本进行分词
        moses_cut(
            local_data_path / f"{mode}.{args.src_lang}",  # 读取源语言文件
            data_dir / f"{mode}_src.cut.txt",  # 目标文件名（分词后）
            lang=args.src_lang,  # 设定源语言
        )
        print(f"[{mode}] 源语言文本分词完成")

        # 对目标语言文本进行分词
        moses_cut(
            local_data_path / f"{mode}.{args.trg_lang}",  # 读取目标语言文件
            data_dir / f"{mode}_trg.cut.txt",  # 目标文件名（分词后）
            lang=args.trg_lang,  # 设定目标语言
        )
        print(f"[{mode}] 目标语言文本分词完成")

    # 以下代码用于创建文件夹并移动处理后的文本，但被注释掉了
    # 这部分代码的逻辑是：
    # 1. 如果目标目录不存在，则创建目录
    # 2. 遍历本地数据路径下的所有 .txt 文件，并将其移动到目标目录
    #
    # if not data_dir.exists():
    #     data_dir.mkdir(parents=True)
    # for fpath in local_data_path.glob("*.txt"):  # 遍历所有分词后的文件
    #     fpath.rename(data_dir / fpath.name)  # 移动文件到目标目录
