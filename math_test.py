#--------------------------------------
# generate math test and give response
#--------------------------------------

import random
import play_wave
#------------------------
# get_operator
#------------------------
def get_operator(i):
    if i == 1:
        return ' + '
    elif i == 2:
        return ' - '
    elif i == 3:
        return ' x '
    elif i == 4:
        return ' / '
    else:
        print 'invalid operator index'
        raise
        
#------------------------
# do_caculate
#------------------------
def do_caculate(x1,x2,op):
    #print 'do_caculate:',x1,x2,op
    if op == 1:
        return x1 + x2
        
    elif op == 2:
        return x1 - x2
    elif op == 3:
        return x1 * x2
    elif op == 4:
        if x2 != 0:
            return x1 / x2
        else:
            print 'invalid divide zemo'
            raise
    else:
        print 'invalid operator index'
        raise
     

#------------------------
# caculate_result
#------------------------
def caculate_result(x1,x2,x3,x4,x5):
    if x5 == 3 or x5 == 4 and x4 != 3 and x4 != 4:
        y = do_caculate(x2,x3,x5)
        y = do_caculate(x1,y,x4)
        return y
        
    else:
        y = do_caculate(x1,x2,x4)
        y = do_caculate(y,x3,x5)
        return y
        
#------------------------
# main
#------------------------
    
i = 0
cnt_right = 0
cnt_wrong = 0

while(cnt_right < 20):
    try:
        x1 = None
        x2 = None
        x3 = None
        x4 = None
        x5 = None
        
        # operator
        
        x4 = random.randint(1,4)   
        x5 = random.randint(1,4)
        
        flag = 0
        if x4 == 3 or x4 == 4:
            flag += 1
        if x5 == 3 or x5 == 4:
            flag += 1
        if flag == 2:
            continue
        
        if x4 == 3:
            x1 = random.randint(1,9)
            x2 = random.randint(1,9)
        
        if x4 == 4:
            x2 = random.randint(1,9)
            x1 = x2 * random.randint(1,9)
            
            
        if x5 == 3:
            x2 = random.randint(1,9)
            x3 = random.randint(1,9)

        if x5 == 4:
            x3 = random.randint(1,9)
            x2 = x3 * random.randint(1,9)
            
        if x1 == None and x4 == 3 and x2 != None:
            x1 = random.randint(x2,19)

        if x1 == None:
            x1 = random.randint(1,19)
        if x2 == None:
            x2 = random.randint(1,19)
        if x3 == None:
            x3 = random.randint(1,19)

        if x4 == 4 and x1 < x2:
            temp = x1
            x1 = x2
            x2 = temp
        
        
            
        
        s = str(x1) + get_operator(x4) + str(x2) + get_operator(x5) + str(x3)
        expected_result = caculate_result(x1,x2,x3,x4,x5)
        if expected_result < 0:
            continue
            
        print '====================================================================='        
        input_result = raw_input(s + ' = ')
        
        print 'ipnut_result:',int(input_result)
        print 'expected_result:',expected_result
        
        if (expected_result == int(input_result)):
            cnt_right += 1
            play_wave.play('good.wav')
            print 'Great job done!!!', 'total right count:', cnt_right, ', total wrong count:', cnt_wrong
        else:
            cnt_wrong += 1
            play_wave.play('bad.wav')
            print 'Error, please try again', 'total right count:', cnt_right, ', total wrong count:', cnt_wrong
    
    except:
        pass

    


