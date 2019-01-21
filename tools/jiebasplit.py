import sys
import jieba
import re


def fenci(input_file):
    filename = 'jieba_' + input_file
    fileneedCut = str(input_file)
    fn = open(fileneedCut, "r", encoding="utf-8")
    f = open(filename, "w+", encoding="utf-8")
    jieba.load_userdict('gamedict.txt')
    for line in fn.readlines():
        words = jieba.cut(line)
        for w in words:
            f.write(str(w) + ' ')
    f.close()
    fn.close()


if __name__ == '__main__':
    input_file = sys.argv[1]
    fenci(input_file)
