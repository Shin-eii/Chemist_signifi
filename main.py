# Program func
# 1. บอกจำนวน significant number 
# 2. + - x / ให้ถูกหลัก decimal
non_zero = [str(i) for i in range(1,10)]

def count_sig(num):
    # step 1: find decimal first 
    if '.' not in num:
        num = abs(int(num)) # do abs to get rid neg num
        num = str(num) # change it back to str
        num = num[::-1] # revert it
        num = str(int(num)) # to int to get rid of trailing 0 and change it back
        return len(num)
    
    else:
        # In this step we will take care of the FLOAT

        # Condition 4 : num > 1 then all zeros in the right side is count as significant figures too
        if float(num) > 1:
            num = num.replace('.','')
            ans = len(num)
            #print(ans)
            return ans
        
        # Condition 3 and 5 : num < 1 zeros in the end and between are significant 
        elif float(num) < 1:
            for i,n in enumerate(num):
                if n in non_zero:
                    break
            ans = len(num[i:])
            #print(ans)
            return ans

'''def add_sub(n1,n2,op):
    if op == "+":
        '''





def main():
    while True:
        input_num = input('Enter your number :')
        #print(type(input_num))
        ans = count_sig(input_num)
        #print(ans)
        print(ans)



main()




