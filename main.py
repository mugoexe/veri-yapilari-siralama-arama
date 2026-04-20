import time
import random
import matplotlib.pyplot as plt

from search.linear_search import linear_search
from search.binary_search import binary_search

from sort.bubble_sort import bubble_sort
from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort


# 🎨 Renkler
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# ⏱️ ölçüm
def measure(func, data):
    start = time.time()
    func(data.copy())
    end = time.time()
    return end - start


# 📥 kullanıcı modu
mode = input("1- Manuel giriş\n2- Random veri\nSeçim: ")

if mode == "1":
    arr = list(map(int, input("Sayıları gir: ").split()))
else:
    size = int(input("Kaç elemanlı liste: "))
    arr = [random.randint(1, 1000) for _ in range(size)]

print(f"\n{BLUE}Veri:{RESET}", arr[:20], "..." if len(arr) > 20 else "")


# 🔄 algoritmalar
algorithms = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort
}

times = {}

print(f"\n{YELLOW}--- SIRALAMA SONUÇLARI ---{RESET}")

for name, func in algorithms.items():
    t = measure(func, arr)
    times[name] = t
    print(f"{name:<10} → {t:.6f} saniye")

# 🏆 en hızlı
fastest = min(times, key=times.get)
print(f"\n{GREEN}🏆 En hızlı: {fastest}{RESET}")


# 📊 GRAFİK
plt.figure()
plt.bar(times.keys(), times.values())
plt.title("Algoritma Performans Karşılaştırması")
plt.xlabel("Algoritmalar")
plt.ylabel("Süre (saniye)")
plt.show()


# 🔍 ARAMA TESTİ
print(f"\n{YELLOW}--- ARAMA ---{RESET}")
target = int(input("Aranacak sayı: "))

sorted_arr = merge_sort(arr.copy())

print("Linear:", linear_search(arr, target))
print("Binary:", binary_search(sorted_arr, target))