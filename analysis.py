import pandas as pd
import matplotlib.pyplot as plt

# pelicana
pelicana_table = pd.DataFrame.from_csv(
    '__result__/crawling/pelicana_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.gungu != '']
pelicana = pelicana_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(pelicana)

# nene
nene_table = pd.DataFrame.from_csv(
    '__result__/crawling/nene_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

nene_table = nene_table[nene_table.sido != '']
nene_table = nene_table[nene_table.gungu != '']
nene = nene_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(nene)

# kyochon
kyochon_table = pd.DataFrame.from_csv(
    '__result__/crawling/kyochon_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

kyochon_table = kyochon_table[kyochon_table.sido != '']
kyochon_table = kyochon_table[kyochon_table.gungu != '']
kyochon = kyochon_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(kyochon)

# goobne
goobne_table = pd.DataFrame.from_csv(
    '__result__/crawling/goobne_table.csv',
    encoding='utf-8',
    index_col=0,
    header=0).fillna('')

goobne_table = goobne_table[goobne_table.sido != '']
goobne_table = goobne_table[goobne_table.gungu != '']
goobne = goobne_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis='columns').value_counts() # 'SIDO GUNGU' 별 매장수
# print(goobne)

chicken_table = pd.DataFrame({'pelicana': pelicana, 'nene': nene, 'kyochon': kyochon, 'goobne': goobne}).fillna(0)
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '00 18'].index)
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '테스트 테스트구'].index)
chicken_sum_table = chicken_table.sum(axis=0)

plt.figure()
chicken_sum_table.plot(kind='bar')
plt.show()
