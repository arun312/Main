file1 = open('IMERG-HalfH-2001-21.txt', 'r')
Lines = file1.readlines()
PreMon=[]
Winter=[]

print(len(Lines))


for line in Lines:
    # month=int(line.split('/')[7]) #MERRA2

    dd=line.split('.')[9][:8] #GESDESC IMERG
    month = int(dd[4:6])
    try:
        # #CheckingforWinter
        # if (month==1 or month==2 or month==12):
        #     Winter.append(line)
        # #CheckingforPreMon
        if (month==3 or month==4 or month==5):
            PreMon.append(line)
    except Exception as e:
        print(e)

print(len(PreMon))
# file = open("E:\Arun-ACIML\Codes\PBLH_MERA2-Winter.txt", "w")
# for line in Winter:
#     file.write(f"{line}")
# file.close()

file = open("IMERG-HH_PreMon.txt", "w")

for line in PreMon:
    file.write(f"{line}")
file.close()



