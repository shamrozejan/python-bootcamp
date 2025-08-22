speeds  = []
while True:
    raw = input("Enter the speed:").strip()
    if not raw:
        break
    try:
        val = float(raw)
    except ValueError:
        print ("Enter a number:")
        continue
    speeds.append(val)
avg = speeds / len(speeds)
print(len(speeds))
print(min(speeds))
print(max(speeds))
print(f"{avg:2f}")