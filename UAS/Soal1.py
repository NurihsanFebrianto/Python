import sys

def floyd(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u-1][v-1] = dist[v-1][u-1] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def count_shortest_paths(n, dist, a, b):
    def dfs(u, target, path, visited):
        if u == target:
            paths.append(path)
            return
        for v in range(n):
            if not visited[v] and dist[u][v] + dist[v][target] == dist[u][target]:
                visited[v] = True
                dfs(v, target, path + [v], visited)
                visited[v] = False

    paths = []
    visited = [False] * n
    visited[a] = True
    dfs(a, b, [a], visited)
    return paths

def solve(n, edges, a, b):
    dist = floyd(n, edges)
    paths = count_shortest_paths(n, dist, a-1, b-1)
    
    vertex_count = {}
    for path in paths:
        for v in path:
            vertex_count[v] = vertex_count.get(v, 0) + 1
    
    total_paths = len(paths)
    avg_visits = [0] * n
    for i in range(n):
        avg_visits[i] = (vertex_count.get(i, 0) / total_paths) * 2  
    
    return avg_visits

n, m, a, b = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

result = solve(n, edges, a, b)
for avg in result:
    if avg.is_integer():
        print(int(avg))
    else:
        print(f"{avg:.6f}")
        
'''
ALGORITMA

1. Mulai
2. Buat fungsi floyd(n, edges):
3. inisialisasi
    - Buat matriks dist dengan ukuran n x n yang diisi dengan nilai tak terhingga (inf),
    - Atur jarak setiap sisi (u,v,w) dalam 'edges' ke dalam 'dist'
4. lakukan 3 perulangan bersarang untuk menghitung jarak terpendek dari semua simpul
5. di setiap simpul perantara 'k' perbarui jarak menjadi 'dist[i][j] jika ada jalur yang kebih mpendek melalui simpul 'k'
6. retunt nilai 'dist' yang berisi jarak terpendeknya
7. Buat funsgi count_shortest_paths(n, dist, a, b):
8, inisialisasikan
    - Buat paths untuk menyimpan semua jalur yerpendek
    - Buat visited untuk melacak simpul yang telah di kunjungi
9. Buat Fusngi dfs(u, target, path, visited):
10. Gunakan rekursif dalam dfs untuk menjelajahi graph untuk mempertimbngkan simpul man ayang belum di kunjungi dan berapa pada jalur terpendek
11. Return 'paths'
12. Buat fungsi solve(n, edges, a, b):
13. Panggil Funsgi floyd untuk menghitung jarak terpendek antara semua simpul
14. panggil Fungsi count_shortest_paths untuk menghitung semua jalur terpendek dari a ke b.
15. setelah dapat semua dalur terpendek  dari a dan b hitung berapa kali setiap simpul berkunjung ke semua jalur
16. hitung rata-rata kunjungan untuk semua simpul dengan membagi jumpal kungjungan dengan total jalur dan di kali 2 untuk menghitung perjalanan pergi dan pulng
17. Return avg_visits
18. Lakukan penginputan
    - input nilai 'n' 'm' 'a' dan 'b'
    - input 'edges' 
20. panggil fungsi solve dengan parameter 'n' 'edges' 'a' dan 'b' 
21. cetak rata rata kunjungan
22. selesai 
'''

'''
KOMPLEKSITAS
Fungsi floyd = - Waktu : O(n^3)
               - Ruang : O(n^2)   
Fungsi count_shortest_paths = - Waktu : O(2^n * n)
                              - Ruang : O(n^2)
Fungsi Solve = - waktu : O(n^3 + 2^n * n)
               - Ruang :  O(n^2)
'''