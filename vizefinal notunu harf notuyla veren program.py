vize=int(input("vize notonu giriniz"))
final=int(input("final notunu giriniz"))
ort= vize*0.4 + final * 0.6
print (ort)
if ort >= 80:
    print ("AA")
elif 60 >= ort <= 79:
    print ("BA")
elif 59 <= ort >= 50:
    print ("BB")
elif 49 <= ort >= 40:
    print ("CC")
else:
    print ("FF")
