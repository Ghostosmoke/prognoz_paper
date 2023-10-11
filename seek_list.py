seek_list=['20','россии']
import pymorphy2

morph=pymorphy2.MorphAnalyzer(lang='ru')

for i in range(len(seek_list)):
    seek_list[i]=morph.normal_forms(seek_list[i])[0]
seek_list_new=[]
for seek in seek_list:
    seek_list_new.append(seek[0].upper() + seek[1:])
    seek_list_new.append(seek.lower())
    seek_list_new.append(seek.upper())
seek_list=set(seek_list_new)
