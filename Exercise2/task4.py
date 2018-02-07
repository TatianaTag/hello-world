def desks():
    pupil1 = int(input("Pupil1="))
    pupil2 = int(input("Pupil2="))
    pupil3 = int(input("Pupil3="))
    count = pupil1//2+pupil1%2+pupil2//2+pupil2%2+pupil3//2+pupil3%2
    print(count)


desks()