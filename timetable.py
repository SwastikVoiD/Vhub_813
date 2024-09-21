with open("timetable.txt", "r") as fh:
    cl = fh.readlines()
    a = []
    for i in cl:
        s = i.removesuffix("\n")
        if len(s) > 0:
            a.append(s)
    # print(a)
    print(len(a))
    prop = list()
    for i in range(1,len(a)-1,16):
        prop.append([a[i],a[i+2],a[i+3],a[i+4],a[i+5],a[i+7],a[i+8],a[i+9],a[i+10],a[i+11]])

    for i in prop:
        print("Course Title:\t",i[1])
        print("CLASS Type:\t",i[2])
        print("Credits:\t", i[3][8:11])
        print("Course Type:\t",i[4][:-1])
        print("Class No:\t",i[5])
        print("Slot:\t",i[6])
        print("Venue:\t",i[7])
        print("Proff:\t",i[8])
        print("Prof School:\t",i[9])
        print("############################################")
            
