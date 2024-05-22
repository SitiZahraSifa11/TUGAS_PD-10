# No.4
# Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan 
# kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, 
# dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

List1 = ["apel", "jeruk", "mangga"]
List2 = ["apel", "anggur", "nanas"]

buah=List1.copy()
buah.extend(List2)
saring= set(buah)
buahDewi=sorted(saring)
print("Buah Dewi sekarang = ",buahDewi)

