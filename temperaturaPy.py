import glob   
import time
cont = 0
cont1 = 0

def porcentagem(number):
    output = number / 255
    output = output * 100
    #output = recebe_arg / 100
    return output

def manda_temp(number):
    output = number / 280
    output = int(output)
    return output

array = [ ]
temp = ''
for i in glob.glob("/sys/class/drm/card?/device/hwmon/hwmon?/pwm1_enable"): 
    with open(i, 'w') as f:
        f.write('1')
for i in glob.glob("/sys/class/drm/card?"):      #isso iria listar diretorios
    i = str(i[15:23])
    print (i)
    #print (type(i))
    #cont = cont + 1
    array.append(i)
    time.sleep(1)
    cont1 = cont1 +1      
while True:

    for i in glob.glob("/sys/class/drm/card?/device/hwmon/hwmon?/temp1_input"):      #isso iria listar diretorios
        with open(i, 'r') as d:
            for y in d:
                #print (y)
                y = int(y)
                #print (type(y))   
                temp = manda_temp(y)
                porcent = porcentagem(temp)
                porcent = int(porcent)
                temp = str(temp)
               
                print('mandando dados - ', array[cont], 'FAN',  porcent,'%')
                cont = cont + 1
                if cont == cont1:
                    cont = 0
                i = i[0:41]
    
                with open(i+'pwm1', 'w') as f:
                    f.write(temp)
                
                    print('contando........')
                    time.sleep(5)

'''
for i in (array):
    i = int(i)
    if i > 40:
        #i = int(i)
        #print (type(i))
        temp = manda_temp(i)
        print(temp)
    print(i)

#print (array)

cont1 = ''
print (int(cont))


if cont == 3:
    with open('/sys/class/drm/card0/device/hwmon/hwmon0/temp1_input', 'r') as d:
        for y in d:
            #cont1 = y[0:2]
            array.append(y)
            #cont1 = int(cont1)
if cont == 3:
    with open('/sys/class/drm/card1/device/hwmon/hwmon1/temp1_input', 'r') as d:
        for y in d:
            #cont2 = y[0:2]
            array.append(y)
            #cont2 = int(cont2)
if cont == 3:
    with open('/sys/class/drm/card2/device/hwmon/hwmon2/temp1_input', 'r') as d:
        for y in d:
            #cont3 = y[0:2]
            array.append(y)
            #cont3 = int(cont3)             
#print (int(cont))
#print (cont1)
#print (type(cont1))
#print (cont2)
# print (type(cont2))
#print (cont3)
#print (type(cont3))
 
def atualisa_temp(number):
    output = number * 255
    output = output / 100
    #output = recebe_arg / 100
    return output

def manda_temp(number):
    output = number / 306
    output = int(output)
    return output


#var = atualisa_temp(64)    
#print (var)
#print (type(var))

print (array)

for i in (array):
    i = int(i)
    if i > 40:
        #i = int(i)
        #print (type(i))
        temp = manda_temp(i)
        print(temp)
    print(i)

#var2 = manda_temp(cont1) 
#var2 = str(var2)   
#print (var2)
#print (type(var2))
'''
