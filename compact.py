# compact

def compact(collection):
        return [n for n in collection if n]

print(compact((1, 0, None, False, 3, "car", [])))


def compact(collection):
    truthy_ns = []
    for n in collection:
        if n: 
            truthy_ns.append(n)
    return truthy_ns

print(compact((1, 0, None, False, 3, "car", [])))