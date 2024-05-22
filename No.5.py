# No.5
# Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus 
# semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai 
# tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.
# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]


List=[105, 20, 8, 150, 30, 5, 200]
hasil=[]
for n in List:
    if 10 <= n <= 100:
       hasil.append(n)
hasil.sort()      
print("Output :",hasil)