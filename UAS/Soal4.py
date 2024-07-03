def read_and_sort_job(num_jobs, jobs):
    jobs.sort(key=lambda job: (job[3], -job[1]), reverse=True)   
    return jobs

def schedule_jobs(num_jobs, jobs):
    sorted_jobs = read_and_sort_job(num_jobs, jobs)
    
    total_profit = 0
    job_sequence = []
    used_times = []
    
    for job in sorted_jobs: 
        customer, profit, sewing_time, delivery_time = job
        if sewing_time + delivery_time in used_times:
            continue
        job_sequence.append(customer)
        used_times.append(sewing_time + delivery_time)
        total_profit += profit
        
    return job_sequence, total_profit

num_jobs = int(input().strip())
jobs = []
for _ in range(num_jobs):
    customer, profit, sewing_time, delivery_time = input().strip().split()
    profit, sewing_time, delivery_time = int(profit), int(sewing_time), int(delivery_time)
    jobs.append((customer, profit, sewing_time, delivery_time))

job_sequence, total_profit = schedule_jobs(num_jobs, jobs)

print(" ".join(job_sequence))
print(total_profit)


'''
ALGORITMA

1. Mulai
2. Lakukan penginputan
    - input jumlah num_jobs
    - Input detail setiap pekerjaan, customer, profit, sewing_time, dan delivery_time untuk masing-masing pekerjaan.
3. Buat funsgi read_and_sort_job(num_jobs, jobs)
    - Urutkan 'jobs' berdasarkan 'delivery_time' dalam urutan menurun.
    - Jika 'delivery_time' sama, urutkan berdasarkan 'profit' dalam urutan menurun.
    - Kembalikan daftar pekerjaan yang sudah diurutkan.
4. Buat fungsi schedule_jobs(num_jobs, jobs)
5. Panggil prosedur read_and_sort_job(num_jobs, jobs) untuk mengurutkan pekerjaan.
6. Insisialisasikan 
    - total_profit dengan 0.
    - job_sequence sebagai daftar kosong untuk menyimpan urutan pelanggan.
    - used_times sebagai daftar kosong untuk menyimpan kombinasi sewing_time + delivery_time yang telah digunakan.
7. lakukan pengurutan dalam daftar  pekerjaan
    - Ambil customer, profit, sewing_time, dan delivery_time.
    - periksa jika kombinasi sewing_time + delivery_time sudah ada di used_times, lanjutkan ke pekerjaan berikutnya.
    - Lalu Tambahkan 
        - customer ke job_sequence
        - sewing_time + delivery_time ke used_times
        - profit ke total_profit.
    - Kemablikan job_sequence dan total_profit
8. Cetak 
    - job_sequence sebagai urutan pelanggan yang optimal.
    - total_profit sebagai jumlah total keuntungan yang dapat diperoleh.
9. Selesai


'''
#KOMPLEKSITAS =  O(n^2) 
 