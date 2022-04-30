def temperature(scale=None, source_temp=None):
    if scale == "F":
        return 'C', (source_temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return 'F', (source_temp * (9.0/5.0)) + 32.0
    else:
        print("Please use uppercase!")

scale = input("Select (F) or (C): " )
source_temp = int(input("What is the temperature: " ))
s, m = temperature(scale, source_temp)
print(source_temp, "degrees", scale, "is", m, "degrees", s)