# No.2
# Budi memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus 
# semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut 
# dari terkecil ke terbesar. Bantu budi untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [7, 4, 9, 2, 5, 1]
# Output: [2, 4]

List=[7, 4, 9, 2, 5, 1]
filter =[]

for n in List:
    if n % 2 == 0:
        filter.append(n)
filter.sort()
print("Input : ",List)
print("Output : ",filter)