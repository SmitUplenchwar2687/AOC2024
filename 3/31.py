with open('advcode3.txt', 'r') as file:
    lines1 = file.readlines()

lines = "".join(lines1)

#lines = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
res = 0

i = 0

while(i<len(lines)):
    if i + 3 < len(lines) and lines[i]=="m" and lines[i+1]=="u" and lines[i+2]=="l" and lines[i+3]=="(":
        j = 0
        i = i + 4
        temp1 = 0
        temp2 = 0
        flag = False
        while(j<3 and lines[i+j]!=","):
            if ord(lines[i+j])<=57 and ord(lines[i+j])>=48:
                print(lines[i+j], "line1")
                temp1 = temp1*10 + int(lines[i+j])
            else:
                temp1 = 0
                break
            j += 1
        print(temp1)
        if i + j < len(lines) and lines[i+j]==",":
            i += j + 1
        else:
            continue
        j = 0
        while(j<3 and lines[i+j]!=")"):
            if ord(lines[i+j])<=57 and ord(lines[i+j])>=48:
                print(lines[i+j], "line2")
                temp2 = temp2*10 + int(lines[i+j])
            else:
                temp2 = 0
                break
            j += 1
        if i + j < len(lines) and lines[i + j] == ")":
            flag = True
        print(temp2)
        if flag:
            res= res + (temp1 * temp2)
            print(res,"res")
        i = i + j
    else:
        i += 1
            

print(res)
