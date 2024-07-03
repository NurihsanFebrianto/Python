def min_operations_to_sort(N, A, B):
    operations = 0
    A = list(A)
    B = list(B)

    i = 0
    while i < N:
        if A[i] > B[i]:
            j = i
            while j < N and A[j] > B[j]:
                j += 1
            A[i:j], B[i:j] = B[i:j], A[i:j]
            operations += 1
        i += 1
        
    return operations

N = int(input("Masukkan N: "))
A = input("Masukkan string A: ")
B = input("Masukkan string B: ")

if len(A) != N or len(B) != N:
    print("Panjang string A dan B harus sama dengan N.")
else:
    result = min_operations_to_sort(N, A, B)
    print(result)

'''
ALGORITMA

1. Mulai
2. Buat fungsi min_operations_to_sort dengan parameter (N, A, B):
3. Inisialisaikan Variabel 'operation dengan nilai 0 dan ubah string 'A' dan 'B' menjadi sebuah list
4. Iterasikan untuk menukan substring 
    - Gunakan index i untuk iterasi dari 0 hingga N-1
    - jika A[i] > B[i] maka cari index j sehingga A[j] <= B[j] sampai mencapai akhir string
        - lakukan Pertukaran A[i:j] dengan B[i:j]
        - tambahkan 1 ke vaiabel operations
5. Kembalikan Nilai operations sebagai hasil
6. Masukan inputan untuk nilai N, A, dan B.
7. lakukan pemeriksaan apakah Panjang A dan B sesuai dengan N
    - Jika panjng tidak sesuai maka cetak pesan kesalahan
    - jika panjang sesuai Panggil fungsi min_operations_to_sort dan cetak hasilnya
8. selesai
'''
# kOMPLEKSITAS WAKTU = O(N^2)
# KOMPLEKSITAS RUANG = O(N)