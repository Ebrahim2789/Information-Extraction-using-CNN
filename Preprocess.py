def Preprocessing(file_name_1 ,file_name_2,file_name_3):
    # f = open("myfile.txt", "r", encoding="utf-8")
    with open(file_name_1, 'r') as f:
        with open(file_name_2, 'r') as f2:
             with open(file_name_3, 'w') as f3:
                datafile = f.readlines()
                datafile2 = f2.readlines()
                data=len(datafile)

                for line in datafile: 
                    value = line.strip().split(' ')
    #                 print(len(line))
    #                 len1=len(line)
                    for l in value: 
                        print(l,',',1, file=f3)
                f4 = open(file_name_3, "a", encoding="utf-8")
                for line2 in datafile2: 
                    values = line2.strip().split(' ')
    #                 print(len(line2))
                    len2=len(line2)
                    for l2 in values: 
                        print(l2,',',0, file=f4)