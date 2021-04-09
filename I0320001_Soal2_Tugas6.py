# Penghitung IPK
print('')
print('====== Program Penghitung IPK ======')
print('')
n = int(input('Masukkan semester berapa anda :'))
print('')

IPsemester = []
x = 1
while x <= n:
    IP = float(input('Masukkan IP semester ke-%d:' % x))
    IPsemester.append(IP)
    x += 1
IPK = sum(IPsemester)/n

print('')
print('IPK anda adalah',format(IPK))