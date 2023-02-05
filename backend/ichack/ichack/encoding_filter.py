

def enc_filter(encoding, name, key):

    transfered = encoding.split('@')
    transfered[0] = transfered[0].split(';')
    transfered[1] = transfered[1].split(';')

    lowkey = str(key).lower()

    res = 0

    if lowkey == name.lower():
        res += 100
    
    if lowkey in transfered[0]:
        res += 10
    
    if lowkey in transfered[1]:
        res += 20
    
    for x in transfered[0]:
        if x in lowkey.split(' '):
            res+=2

    return res