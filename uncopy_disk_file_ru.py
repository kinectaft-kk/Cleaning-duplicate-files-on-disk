import hashlib, os
def radar(p,typ=[]):
    js=[]
    if len(typ) == 0:
        for i in os.listdir(p+'/'):
            _,g=os.path.splitext(i)
            if g == '':
                try:js=radar(p+'/'+i,js=js)
                except:js.append(p+'/'+i)
            else:js.append(p+'/'+i)
    else:
        for i in os.listdir(p+'/'):
            _,g=os.path.splitext(i)
            if g == '':
                try:js=radar(p+'/'+i,typ,js)
                except:
                    if g in typ:js.append(p+'/'+i)
            else:
                if g in typ:js.append(p+'/'+i)
    return js
print('''Программа по очистке твердотельных накопителей
Версия: 1''')
name=input('Введите полный путь до папки которую нужно очистить:')
typ=input('Введите типы файлов в виде .тип_файла,.тип_файла Оставте строку пустой для очистки всех типов файлов:')
if typ == '':typ = []
else:typ = typ.split(',')
print('Поиск файлов...')
f=radar(name,typ)
del(name,typ)
old=0
al=len(f)
fil={}
print(f'''{al} файлов найдено
Запуск первого этапа сканирования...''')
for n,i in enumerate(f):
    if n == old:
        print(f"{n/al*100}%   {n}/{al}")
        old+=al//100
    try:
        h=str(os.path.getsize(i))
        if h in fil:fil[h].append(i)
        else:fil[h]=[i]
    except Exception as e:print(f'''Ошибка получения размера файла:{fil}
Ошибка:
{str(e)}''')
del(f)
s=[]
remov=[]
old=0
al=len(fil)
print(f'''{al} дубликатов файлов после первого сканирования
Запуск второго этапа сканирования...''')
for n,i in enumerate(fil):
    if n == old:
        print(f"{n/al*100}%   {n}/{al}")
        old+=al//100
    if len(fil[i]) >= 2:
        for n in fil[i]:
            try:
                with open(n,'rb') as f:
                    h=hashlib.md5(f.read()).hexdigest()
                if h in s:
                    remov.append(n)
                else:s.append(h)
            except Exception as e:print(f'''Ошибка хеширования файла:{n}
Ошибка:
{str(e)}''')
del(fil)
print(f'''{len(remov)} дубликатов файлов после второго сканирования
Запуск удаления дубликатов...''')
for i in remov:
    try:os.remove(i)
    except Exception as e:print(f'''Ошибка удаления файла:{i}
Ошибка:
{str(e)}''')
del(remov)
print('''Дубликаты файлов удалены
Для выхода нажмите enter''')
input()
