import os
import re

with open('gametitle.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

# 消去标点符号
with open('gamedict.txt', 'w', encoding='utf-8') as f:
    content = [x.strip() for x in content]
    for line in content:
        for word in (re.split(': |：| |,|，', line)):
            f.write(word + '\r\n')

# 消去英文和数字
with open('gamedict.txt', 'r+', encoding='utf-8') as f:
    content = str(f.read())
    f.seek(0)
    # 丑但能用=。=
    english_words = re.findall('[a-zA-Z0-9]+', content)
    for word in english_words:
        content = content.replace(word, '')
    # 匹配英文单词
    english_words = re.findall('[a-zA-Z0-9]+', content)
    for word in english_words:
        wordp = re.compile(word)
        content = wordp.sub('', content)
    lines = content.split('\n')
    # 去重
    lines = list(set(lines))
    for line in lines:
        # 3个字才算整词
        if line.strip() != '' and len(line.strip()) >= 3:
            f.write(line.strip() + '\r\n')
    f.truncate()
