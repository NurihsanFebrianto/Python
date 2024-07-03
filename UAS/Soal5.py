def island_vocation(v, start=None, memo=None):
    if memo is None:
        memo = {}
        
    if start is None:
        a = island_vocation(v, 0, memo)
        b = island_vocation(v, 1, memo)
        return max(a, b)
    
    if start in memo:
        return memo[start]

    if start >= len(v):
        return 0

    result = v[start] + island_vocation(v, start + 2, memo)
    memo[start] = result

    return result

n = int(input())
v = list(map(int, input().split()))
print( island_vocation(v))

'''

ALGORITMA 

1. Mulai
2. Baca bilangan bulat n
3. Baca daftar bilangan bulat v
4. Fungsi island_vocation(v, start=None, memo=None):
    a. Jika memo adalah None, maka
        i. Inisialisasi memo sebagai kamus kosong
    b. Jika start adalah None, maka
        i. Panggil island_vocation(v, 0, memo) -> a
        ii. Panggil island_vocation(v, 1, memo) -> b
        iii. Kembalikan max(a, b)
    c. Jika start ada di memo, maka
        i. Kembalikan memo[start]
    d. Jika start >= panjang v, maka
        i. Kembalikan 0
    e. Hitung hasil sebagai v[start] + island_vocation(v, start + 2, memo)
    f. Simpan hasil di memo[start]
    g. Kembalikan hasil

5. Panggil island_vocation(v)
6. Cetak hasilnya
7. Selesai
'''

# Kopleksitas = O(N)