#operaso aritmatika
a = 10
b = 3

# operasi tambah
hasil = a + b
print (a, '+',b,'=',hasil)

# operasi pengurangan
hasil = a - b
print (a, '-',b,'=',hasil)

# operasi perkalian
hasil = a * b
print (a, '*',b,'=',hasil)

# operasi pembagian
hasil = a / b
print (a, '/',b,'=',hasil)

# operasi pangkat (eksponen)
hasil = a ** b
print (a, '**',b,'=',hasil)

# operasi modulus
hasil = a % b
print (a, '%',b,'=',hasil)

# operasi floor division
hasil = a // b
print (a, '//',b,'=',hasil)

# prioritas operasi (Operational precendence):
# - ()
# - exponen
# - perkalian, bagi
# - jumlah, kurang

x = 3
y = 2
z = 4

hasil = x ** y *z + x / y - y % z // x
print (hasil)

hasil = x + y * z
print (x, '+' ,y, '*' ,z, '=',hasil)