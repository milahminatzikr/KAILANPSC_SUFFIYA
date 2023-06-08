jenis_komponen = ["control horn", "Push rod wire","Brushless motor", "Linkage stopper", "ESC(SW50A)", "Receiver(LA10B RX)", "Carbon fiber rod 3mm", "Servo 9g", "RC LIPO battery", "Propeller", "FLYSKY-i6x REMOTE CONTROL", "MPPF FORM 5x1000x900m"]
harga_komponen = [3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161,23]
Jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("HARGA KOMPONEN CONTROL HORN=RM3,PUSH ROD WIRE=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER=RM12,ESC(SW50A)=RM67,RECEIVER(LA10B RX)=RM61,CARBON FIBER RODE 3MM=RM25.30,SERVO 9G=RM5.20,RC LIPO BATTERY=RM57.56,PROPELLER=RM5.50,FLYSKY-I6X REMOTE CONTROL=RM161,MPPF FORM 5X1000X900MM=RM23") 
a=int(input("Maukkan tempahan untuk control horn:"))   
b=int(input("Masukkan tempahan untuk push rode wire:"))     
c=int(input("Masukkan tempahan untuk brushless motor:"))   
d=int(input("Masukkan tempahan untuk linkage stopper:"))
e=int(input("Masukkan tempahan untuk ESC(SW50A):"))
f=int(input("Masukkan tempahan untuk receiver(LA10B RX):"))
g=int(input("Masukkan tempahan untuk carbon fiber rod 3mm:"))
h=int(input("Masukkan tempahan untuk servo 9g:"))
i=int(input("Masukkan tempahan untuk rc lipo battery:"))
j=int(input("Masukkan tempahan untuk propeller:"))
k=int(input("Masukkan tempahan untuk flysky-16x remote control:"))
l=int(input("Masukkan tempahan untuk mppf form 5x1000x900mm:"))

tempahan = [a,b,c,d,e]

def jumlah_harga() :
    for i in range(5):
        Jumlah[i] = harga_komponen[i]*tempahan[i]
    return(Jumlah)

def cetak() :
        print("\n\n Tempahan anda ialah:")
        print(a,"komponen", jenis_komponen[0])
        print(b,"komponen", jenis_komponen[1])
        print(c,"komponen", jenis_komponen[2])
        print(d,"komponen", jenis_komponen[3])
        print(e,"komponen", jenis_komponen[4])
        print(f,"komponen", jenis_komponen[5])
        print(g,"komponen", jenis_komponen[6])
        print(h,"komponen", jenis_komponen[7])
        print(i,"komponen", jenis_komponen[8])
        print(j,"komponen", jenis_komponen[9])
        print(k,"komponen", jenis_komponen[10])
        print(l,"komponen", jenis_komponen[11])

        print("\n Jumlah harga untuk tempahan ialah RM",sum(Jumlah))
jumlah_harga()
cetak()
    
       
