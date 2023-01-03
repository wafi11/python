p = int(input('masukkan angka : '))

# for i in range(p):
#     print(' ')
# # 4-1 * 4
# for i in range(p):
#     print((p-i) * ' *')

# mengulang sampe p
# for i in range(0,p):
#     # mengulang dimulai dari 0 ,i selesai dengan menghilangkan outputnya
#     for j in range(0, i):
#         print ('*',end='')
#     #  bary disini diulang dengan cara ditambahkan lalu dikasih bintangs
#     for k in range (0,p):
#         print (' ',end='')
#     p-=1
#     print('')

# for i in range (0,p):
#     for j in range (0,i):
#         print ('*',end='')

#     print('')

for i in range (0,p):
    for j in range (1,p+1):
        print ('0',end='')
    for k in range (0,i+1):
        print ('*',end='')
    for l in range (0,i):
        print('*',end='')
    for m in range (0,p):
        print ('0',end='')
    p-=1
    print('')

