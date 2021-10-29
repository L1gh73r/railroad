# cars: 等待排序的车厢 k: 缓冲轨数量，
def get_cache_status(cache):
    print('轨道状态：\n')
    for list_item in cache:
        if not list_item:
            print('空轨道'+'\n')
        else:
            strr = ''
            for i in list_item:
                i = str(i)
                strr += i
            print(strr)
            print('\n')

def railroad(cars, k):
    cacheLists = []
    for i in range(k):
        cacheLists.append([])
    init = 1
    for i in cars:
        if i == init:
            print('{}号车厢入轨->出轨'.format(i))
            get_cache_status(cacheLists)
            init += 1
            continue
        else:
            for list_item in cacheLists:
                if not list_item:
                    list_item.append(i)
                    print('{}号车厢->进入缓冲轨道'.format(i))
                    get_cache_status(cacheLists)
                    break
                else:
                    if min(list_item) > i:
                        list_item.append(i)
                        print('{}号车厢->进入缓冲轨道'.format(i))
                        get_cache_status(cacheLists)
                        break

    for item in cacheLists:
        for i in range(len(item)):
            last = item.pop()
            if last == init:
                print('{}号车厢于缓冲轨道->出轨'.format(last))
                get_cache_status(cacheLists)
                init += 1


car = [5, 8, 1, 7, 4, 2, 9, 6, 3]
n = 3
print(railroad(car, n))
