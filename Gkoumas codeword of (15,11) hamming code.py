import random
for k in range(1,2049):# 2048=2**11 codewords
    list=[]
    for i in range(15):# the lenght of each codeword
        cdw=random.randint(0,1)
        list.append(cdw)
    print( "Number",k," Codeword is : ",list)



