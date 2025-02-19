# 运行 Python 脚本 data_multi30k.py，传递 4 个参数：
# --pair_dir: 目标数据存放目录
# --dest_dir: 预处理后数据存放目录
# --src_lang: 源语言
# --trg_lang: 目标语言
python data_multi30k.py --pair_dir $1 --dest_dir $2 --src_lang $3 --trg_lang $4

# 创建一个合并文件 train_l，将源语言和目标语言的训练数据合并到该文件
touch $1/train_l  # 新建 train_l 文件

# 将源语言的训练数据追加到 train_l
cat $2/train_src.cut.txt >> $1/train_l

# 将目标语言的训练数据追加到 train_l
cat $2/train_trg.cut.txt >> $1/train_l

# 使用 Subword-NMT 进行 BPE（Byte Pair Encoding）分词训练
# learn-joint-bpe-and-vocab：学习联合 BPE 规则并生成词表
# -i $1/train_l：输入合并的训练数据
# -s 20000：设定 BPE 规则数目为 20000
# -o $1/bpe.20000：输出 BPE 规则文件
# --write-vocabulary $1/vocab：生成词表并存储到 vocab 文件
subword-nmt learn-joint-bpe-and-vocab \
    -i $1/train_l \
    -s 20000 \
    -o $1/bpe.20000 \
    --write-vocabulary $1/vocab

# 遍历 train（训练集）、val（验证集）和 test（测试集）三种模式，应用 BPE 进行分词
for mode in train val test; do
    # 对源语言数据应用 BPE，输出分词后的文件
    subword-nmt apply-bpe -c $1/bpe.20000 < $2/${mode}_src.cut.txt > $1/${mode}_src.bpe

    # 对目标语言数据应用 BPE，输出分词后的文件
    subword-nmt apply-bpe -c $1/bpe.20000 < $2/${mode}_trg.cut.txt > $1/${mode}_trg.bpe

    # 打印提示信息，表示该模式（train/val/test）的 BPE 处理已完成
    echo "Finished applying bpe to ${mode} files."
done
