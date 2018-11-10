#!./env/bin/python3.5
with open('stop_words', 'r') as stopFile: stopWords = stopFile.read().replace('\n', ',').split(',')
testStr = 'Строка в которой будем искать'
for word in stopWords:
    if word in testStr:
        print('Найдено совпадение')
    else:
        print('Совпадений не найдено')
print(stopWords)
