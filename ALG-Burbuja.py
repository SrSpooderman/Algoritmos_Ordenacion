array = [5234,234,6,1234,345,2,45,346,4]
cambio = True
while cambio:
    cambio = False
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            cambio = True
print(array)