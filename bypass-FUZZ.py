import requests
import random
import sys
import time

palyloadEN = "ABCDEFGHIZKLMNOPQRSTUVWSYZ"
palyloaden = "abcdefghizklmnopqrstuvwsyz"
playloadnu = "0123456789"
playloadsy = "<>(){}[]''""/,.;:'\\~`!@#$%^&*-_=+"

def password(length):
    pw = str()
    characters = palyloadEN + palyloaden + playloadnu + playloadsy   #设置fuzz复杂度

    for i in range(length):
        pw = pw +  random.choice(characters) #根据提供的fuzz种类性，生成随机字符
    
    payload = pw
    #print (payload)

    with open("text.txt","a") as file:  #写入py脚本当前目录test.txt文件中
	    file.write(payload + "\n")

def process_bar(precent, width=50): #显示任务进度模块，不需要可以删除，不影响脚本主要功能，只是为了好看
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    # print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True)
    sys.stdout.write("[%s%s]%d%%\r"%(use_num*"=", space_num*' ',precent))
    sys.stdout.flush()
 

number = 0
innumber = input("\n请输入输出fuzz次数：")
inlength = input("请输入输出fuzz长度：")


while number < int(innumber):         
	number = number + 1
	password(int(inlength))

if __name__ == '__main__':  #显示任务进度模块，不需要可以删除，不影响脚本主要功能，只是为了好看
    for i in range(21):
        precent = i/20
        process_bar(precent)
        time.sleep(0.1)
    print('\n')
           
print ("\n数据已写入完成")     


    
