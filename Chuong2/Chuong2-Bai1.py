import math
try: 
    r = float (input("Địt mẹ mày nhập bán kính đường tròn vào: "))
    cv = 2*math.pi*r
    dt = r**2
    print("Chu vi của mày bằng: ",cv)
    print("diện tích là: ", dt)
except:
    print("lỗi rồi!")