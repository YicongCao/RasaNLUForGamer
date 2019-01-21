import re
import sys
import codecs


def filte(input_file):
    p1 = re.compile('（）')
    p2 = re.compile('《》')
    p3 = re.compile('「')
    p4 = re.compile('」')
    p5 = re.compile('<doc (.*)>')
    p6 = re.compile('</doc>')
    p7 = re.compile('===')
    p8 = re.compile('##')
    p9 = re.compile('###')
    outfile = codecs.open('std_' + input_file, 'w', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:
        for line in myfile:
            line = p1.sub('', line)
            line = p2.sub('', line)
            line = p3.sub('', line)
            line = p4.sub('', line)
            line = p5.sub('', line)
            line = p6.sub('', line)
            line = p7.sub('', line)
            line = p8.sub('', line)
            line = p9.sub('', line)
            outfile.write(line)
    outfile.close()


if __name__ == '__main__':
    input_file = sys.argv[1]
    filte(input_file)
