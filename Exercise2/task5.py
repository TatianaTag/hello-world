t1 = int(input("how much minutes? "))
hours = t1 // 60
    
hours %= 24
print('hours {:d}'.format(hours)) 

minutes = t1 % 60
print('minutes {:d}'.format(minutes))
