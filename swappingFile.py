def swapFileData () :
    file1 = input('Enter the name  of file1 : ')
    file2 = input('Enter the name  of file2 : ')
    enter = input('Enter which file is to opened  file1/file2 :')
    n = enter

    with open(file1, 'r' ) as a :
      data_a = a.read()
    with open(file2, 'r' ) as b :
      data_b = b.read()

    if enter== 'trick2.py':
        with open(file1, 'w' ) as a :
         a.write(data_b)
    else :
    
        with open(file2, 'w' ) as b :
         b.write(data_a)

swapFileData()

    