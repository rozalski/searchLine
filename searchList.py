#!./env/bin/python3.5
with open('stop_words', 'r') as stopFile: stopWords = stopFile.read().replace('\n', ',').split(',')
print(stopWords)
stopWords = list(filter(None, stopWords))
print(stopWords)
testStr = 'Строка в которой будем искать'
res = any(word in testStr for word in stopWords)
print(res)
#for word in stopWords:
#    if word in testStr:
#        print('Найдено совпадение')
#    else:
#        print('Совпадений не найдено')
