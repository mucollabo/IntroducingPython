from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weakly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
