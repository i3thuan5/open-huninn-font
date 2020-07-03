from 用字 import 教典
from 用字 import 教典名姓
from 用字 import 建議
from csv import DictWriter
from itertools import chain
from sys import stderr


def sng(huninnpio, mia, pio):
    jipio = set(chain.from_iterable(pio.全部分詞()))
    print('huninnpio', len(huninnpio))
    print('{}'.format(mia), len(jipio))
    print('{} - huninnpio'.format(mia), len(jipio - huninnpio))
    print(sorted(jipio - huninnpio), file=stderr)
    with open('{}.csv'.format(mia), 'w') as tong:
        writer = DictWriter(tong, fieldnames=['hanji', 'unicode'])
        writer.writeheader()
        for ji in sorted(jipio - huninnpio):
            writer.writerow({
                'hanji': ji,
                'unicode': hex(ord(ji)),
            })


if __name__ == '__main__':
    huninnpio = set()
    with open('huninn-pio') as tong:
        for tsua in tong.readlines():
            if tsua.rstrip():
                huninnpio.add(chr(int(tsua.rstrip(), 16)))
    for mia, pio in zip(['教典', '教典名姓', '建議'], [教典, 教典名姓, 建議]):
        sng(huninnpio, mia, pio)
