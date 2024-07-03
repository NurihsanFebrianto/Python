def matrix_chain_order(dimensions):
    num_matrices = len(dimensions) - 1
    min_operations = [[0] * num_matrices for _ in range(num_matrices)]
    optimal_order = [[0] * num_matrices for _ in range(num_matrices)]
    
    for length in range(2, num_matrices + 1):
        for i in range(num_matrices - length + 1):
            j = i + length - 1
            min_operations[i][j] = float('inf')
            for k in range(i, j):
                operations = min_operations[i][k] + min_operations[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if operations < min_operations[i][j]:
                    min_operations[i][j] = operations
                    optimal_order[i][j] = k
    
    return min_operations, optimal_order

num_matrices = int(input().strip())
dimensions = list(map(int, input( ).strip().split()))

min_operations, optimal_order = matrix_chain_order(dimensions)

print("Hasil: ", min_operations[0][num_matrices - 1])



'''
ALGORITMA

1. Mulai
2. lakukan penginputan
    - input jumlah matrix (num_matrices)
    - input dimensi matrixs dalam bentuk list (dimensions), dimna dimension[i] sebagai baris dan dimension[i+1] sebagai kolom
3. Buat fungsi matrix_chain_order(dimensions)
4. Inisialisasi num_matrices sebagai panjang dimensions dikurangi 1.
5. Buat dua matriks min_operations dan optimal_order dengan ukuran num_matrices x num_matrices, diisi dengan nilai awal 0.
6. lakukan Untuk setiap length dari 2 hingga num_matrices:
7. Iterasi melalui indeks i dari 0 hingga num_matrices - length.
8. Kalkulasi indeks j sebagai i + length - 1.
9. Atur min_operations[i][j] ke nilai tak hingga. Untuk setiap k dari i hingga j-1:
    - Lakukan pergitungan untuk jumlah operations sebagai min_operations[i][k] + min_operations[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1].
    - Jika operations lebih kecil dari min_operations[i][j], update min_operations[i][j] dan optimal_order[i][j] dengan nilai operations dan k secara berturut-turut.
10. Cetak min_operations[0][num_matrices - 1] sebagai jumlah minimum operasi matriks.
11. Selesai

'''

#KOMPLEKSITAS = O(N^3)