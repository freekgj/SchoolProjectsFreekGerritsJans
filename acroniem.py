def acroniem(volledige_woord):
    words = volledige_woord.split()

    res = ''
    for w in words:
        res = res + w[0].upper()
    return res

acroniem("beer tap")