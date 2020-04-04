def correct(data, country):
    data = removeDuplicates(data)

    for i in range(0, len(data)):
        item = data[i]
        if item[0][1] == '/':
            data.remove(item)
            data.append(('2020-03-20', item[1]))
            break
    data.sort()

    if country == 'Poland':
        data.remove(data[5])
        data.remove(data[13])

    # elif country == 'MyCountry':
    #   necessary corrections

    return data


def removeDuplicates(data):
    return list(dict.fromkeys(data))
