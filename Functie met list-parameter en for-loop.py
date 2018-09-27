def kwadratensom(list):
    som = 0
    for char in list:
        if char >= 0:
        som = som + char**2
    print(som)


grondgetallen = [4, 5, 3, -81]

kwadratensom(grondgetallen)


