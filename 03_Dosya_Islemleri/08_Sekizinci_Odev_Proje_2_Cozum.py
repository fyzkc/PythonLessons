with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()
    
    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")

        else:
            bjk.append(satır + "\n")
    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
            
            

    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)