def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    traversal_order = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

N = int(input( ))

graph = {}
for _ in range(N):
    house = input().strip()
    neighbors = input().strip().split()
    graph[house] = neighbors

start = input( ).strip()

order = bfs_traversal(graph, start)

print(" -> ".join(order))


'''
ALGORITMA

1. Mulai
2. Buat fungsi bfs_travesal dengan parameter (graph,start)
3. Inisialisasi variabel 
    - Buat set 'visited' untuk mengecek node-node yang sudah dikunjungi.
    - Buat queue 'queue' yang berisi start untuk menyimpan node-node yang akan dikunjungi selanjutnya.
    - Buat list 'traversal_order' untuk menyimpan urutan kunjungan.
4. Proses BFS nya 
    - selama queue tidak kosong maka Ambil elemen pertama dari queue dan set sebagai node.
    - Jika node belum dikunjungi:
        - Tambahkan node ke set visited.
        - Tambahkan node ke traversal_order.
        - Untuk setiap tetangga neighbor dari node yang belum dikunjungi maka tetangga diurutkan secara abjad dan Tambahkan neighbor ke queue.
5. Kembalikan traversal_order yang berisi urutan node yang dikunjungi dalam BFS.
6. Masukan inputan jumlah rumah
7. Buat dictionary graph untuk menyimpan peta rumah dan tetangganya
8. lakukan pengecekan 
    - Cek nama rumah (house)
    - cek tetangga (neighbors) dan simpan dalam dictionary (graph) dengan (house) sebagai kunci
9. lakukan pengecekan pada rumah pertama (start) yang akan di kunjungi
10.Jalankan BFS untuk mendapatkan urutan kunjungan
11.Mencetak urutan kunjungan
12.Selesai
'''
#KOMPLEKSITASNYA = O (V + E)