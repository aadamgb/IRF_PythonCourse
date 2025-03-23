from example_package_Adam_ElGhaib import OneList

def intervale(l1, l2):
    l3 = []
    if isinstance(l1, str):  
        l1 = OneList.reverseString(l1)
    else:
        l1 = OneList.reverseNumber(l1)

    s1, e1 = 0, len(l1) - 1
    s2, e2 = 0, len(l2) - 1

    while (s1 <= e1) or (s2 <= e2):
        if s1 <= e1:
            l3.append(l1[s1])
            s1 += 1
        if s2 <= e2:
            l3.append(l2[s2])
            s2 += 1

    if isinstance(l1, str) and isinstance(l2, str) :  
        return ''.join(l3)
    else:
        return l3

