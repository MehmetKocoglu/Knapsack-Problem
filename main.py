import time

def read_knapsack_data_chunk(filename, chunk_size=1024):
    with open(filename, 'r') as file:
        # İlk satırı oku
        first_line = file.readline().strip().split()
        n = int(first_line[0])
        capacity = int(first_line[1])

        values = []
        weights = []

        while True:
            # Parça parça oku
            lines = []
            for _ in range(chunk_size):
                line = file.readline()
                if not line:
                    break
                lines.append(line)

            # Dosya sonuna gelindiyse veya herhangi bir veri kalmadıysa döngüyü sonlandır
            if not lines:
                break

            for line in lines:
                value, weight = map(int, line.strip().split())
                values.append(value)
                weights.append(weight)

    return values, weights, capacity


def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    max_value = dp[n][capacity]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    selected_items_binary = [1 if i in selected_items else 0 for i in range(n)]

    return max_value, selected_items_binary


# Dosyadan verileri parça parça oku
filename = "ks_19_0"  # Buraya dosya adını girin

# Okuma süresini ölç
start_time = time.time()
values, weights, capacity = read_knapsack_data_chunk(filename)
read_time = time.time() - start_time

# Knapsack algoritmasını çalıştırma süresini ölç
start_time = time.time()
max_value, selected_items_binary = knapsack(values, weights, capacity)
knapsack_time = time.time() - start_time

print("Maksimum Değer:", max_value)
print("Seçilen Öğeler (0/1):", selected_items_binary)
print("Veri Okuma Süresi: {:.6f} saniye".format(read_time))
print("Knapsack Çalışma Süresi: {:.6f} saniye".format(knapsack_time))