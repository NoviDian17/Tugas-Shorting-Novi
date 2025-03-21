#Nama   = Novi Dian Safitri
#NIM    = 242410101037
#Kelas  = A

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Menentukan titik tengah array
        left_half = arr[:mid]  # Membagi bagian kiri
        right_half = arr[mid:]  # Membagi bagian kanan

        merge_sort(left_half)  # Rekursi pada bagian kiri
        merge_sort(right_half)  # Rekursi pada bagian kanan

        i = j = k = 0  # Indeks untuk left_half, right_half, dan array utama

        # Menggabungkan dua bagian yang sudah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan sisa elemen dari left_half (jika ada)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menambahkan sisa elemen dari right_half (jika ada)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [7, 2, 6, 8, 3, 1]
merge_sort(arr)
print("Hasil pengurutan:", arr)  

