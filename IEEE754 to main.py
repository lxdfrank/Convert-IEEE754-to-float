def IEEE754(data,len=23):
    x = [23-i for i in range(23)]
    return_data = 0.0
    for i,tmp in enumerate(x):
        if data&(0x1<<tmp)==(0x1<<tmp):
            return_data += 1/(math.pow(2,i))
    return return_data

red = master.execute(0x01, cst.READ_HOLDING_REGISTERS, 0x00, 2)  # 这里可以修改需要读取的功能码 

S = (red[0]>>15)
E = (red[0]&0x7FFF)>>7
F = ((red[0]&0x7F)<<16)+red[1]

print(math.pow(-1,S)*(1+IEEE754(F))*math.pow(2,E-127))    
