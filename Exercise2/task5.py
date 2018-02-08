def watch():
    t1 = int(input("how much minutes?"))
    hours = t1//60
    
    if (hours>24):
      hours %= 24
    print("hours "+str(hours)) 

    minutes = t1%60
    print("minutes "+str(minutes))
watch()