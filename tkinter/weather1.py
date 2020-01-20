from boxes import daily,weekly

print('Daily forecast:',daily.forecast())
print("Weekly forecast:")
for index,outlook in enumerate(weekly.forecast(),1):
    print(index,':', outlook)