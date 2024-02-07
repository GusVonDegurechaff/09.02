tale_count = 0
road_count = 0
tale_and_road_count = 0

while True:
    line = input().strip()
    if line == "ARRIVED":
        break

    if "tale" in line:
        tale_count += 1
    if "road" in line:
        road_count += 1
    if "tale" in line and "road" in line:
        tale_and_road_count += 1

print(tale_count, road_count, tale_and_road_count)