# intersection


def intersection(lista, listb):
    return [item for item in lista if item in listb] 

print(intersection([1, 2, 3, 4, 5, True, False, "car", "auto"],[6, 7, 8, 3, 2, False, "auto"]))




def intersection(lista, listb):
    result= []
    for item in lista:
        if item in listb:
            result.append(item)
    return result

print(intersection([1, 2, 3, 4, 5, True, False, "car", "auto"],[6, 7, 8, 3, 2, False, "auto"]))
