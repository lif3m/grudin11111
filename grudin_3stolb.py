with open('materials_b_import.csv','r',encoding='utf-8') as file:
    data=file.readlines()
    no='нет'
    array = []
for i in range(1,len(data)):
    result = []
    arr=data[i].split(";")
    #Наименование
    title=arr[0].strip()
    #Тип материала
    type_mater=arr[1].strip()
    result.append(title)
    result.append(type_mater)
    #Изображение
    if "\\" in arr[2]:
        img=arr[2][11:]
    else:
        img="NULL"
    result.append(img)
    #Цена
    try:
        price=float(arr[3])
    except:
        price=arr[3].split()[0]
    result.append(price)
    #Кол-во на складе
    str = ''
    count_in_sklad=arr[4].strip()
    for char in count_in_sklad:
        if char.isdigit():
            str += char
    result.append(str)
    result.append(str)
    #Мин кол-во
    min_count=arr[5].strip()
    result.append(min_count)
    #Кол-во в упаковке
    count_in_box=arr[6].strip()
    result.append(count_in_box)
    #Ед. измерения
    ed_izmerenia=arr[7].strip()
    result.append(ed_izmerenia)
    array.append(result)
print(array)

