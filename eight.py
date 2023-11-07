#tipe data string
#

print ('Tipe data skalar => tipe data sederhana')
anak1 = 'arief'
anak2 = 'wicak'
anak3 = 'sono'
anak4 = 'ardika'
anak5 = 'pandu'

print(anak1)
print(anak2)
print(anak3)
print(anak4)
print(anak5)

print('\ntipe data list/daftar/aray')
anak = ['arief', 'wicak', 'sono', 'ardika', 'pandu']
print (anak)
anak.append('prastyo')
print((anak))

print ('\n sapa anak ke-2')
print (f'hai {anak[1]}!')

print('\n Sapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\n Sapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}')