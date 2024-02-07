def calculate_health_needed(data, target):
    health_needed = []

    for col in range(len(data[0])):
        col_sum = sum(row[col] for row in data)
        needed = target[col] - col_sum

        if needed < -1:
            print("WARNING!")
            return []

        if needed > -1:
            health_needed.append(needed)

    return list(set(health_needed))

datas = []
while True:
    line = input().strip()
    if not line:
        break
    datas.append([int(num) for num in line.split()])

target_values = [int(num) for num in input().strip().split()]

result = calculate_health_needed(datas, target_values)
result = sorted(result, reverse=True)
for val in result:
    print(val)