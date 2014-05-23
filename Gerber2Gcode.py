import string

#输入文件
#打开的文件应该是GERBER_RS274X格式
f = open(r'C:\DRV8811_copper_bottom.gbr') 
#输出文件
fw = open(r'C:\DRV8811_copper_bottom.gcode','w')
#按行读出所有文本
lines = f.readlines()
for line in lines:
    str = ' Y '
    line = line.replace('Y',str)
    str = ' Z0'
    line = line.replace('D0',str)
    str = 'Z '
    line = line.replace('Z',str)
    str = 'G01 X '
    line = line.replace('X',str)
    str = ''
    line = line.replace('*',str)
    L = string.split(line)
    if(len(L)==7):
        line1=L[0] + ' '
        fw.writelines(line1)
        line2=L[1] 
        fw.writelines(line2)
        line3=string.atof(L[2] )/10000
        #print line3
        line3 = "%s" % line3
        #print line3
        #line3=str(line3)
        fw.writelines(line3)
        line4=' '+L[3]
        fw.writelines(line4)
        line5=string.atof(L[4])/10000
        line5 = "%s"%line5
        fw.writelines(line5)
        line6=' '+L[5]
        fw.writelines(line6)
        line7=L[6]
        fw.writelines(line7)
        fw.writelines('\n')
f.close()
fw.close()
