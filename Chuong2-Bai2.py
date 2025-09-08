t = int(input("Nhập vào số giây nhanh: "))
hour=(t//3600)%24
minute=(t%3600)//60
seconds=(t%3600)%60
print("hiện tại là: ",hour,"giờ, ",minute,"phút, ",seconds,"giây")