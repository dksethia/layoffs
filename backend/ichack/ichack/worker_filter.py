

def wor_filter(encoding, name, inlist, key):

    transfered = encoding.split(';')

    lowkey = str(key).lower()

    res = 0

    if inlist:
        res+=200

    if lowkey == name.lower():
        res += 100
    
    if lowkey in transfered:
        res += 10
    
    for x in transfered:
        if x in lowkey.split(' '):
            res+=2

    return res