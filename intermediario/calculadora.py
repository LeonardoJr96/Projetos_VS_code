import math 

def more(a,b):
    result = a + b
    print(result)

def less(a,b):
    result = a - b
    print(result)

def mult(a,b):
    result = a * b
    print(result)

def div(a,b):
    result = a / b
    print(result)
    
def raiz(a,b):
    if a == 2:
        result = math.sqrt(b)
    else:
        result = b ** 1 / a
        
    print(result)
    
def single_operation(a,b,oper):
    match oper:
        case '+':
            return more(a,b)
        case '-':
            return less(a,b)
        case '/':
            return div(a,b)
        case '*':
            return mult(a,b)
        case 'v':
            return raiz(a,b)       

def mult_operation(a):
    print(a)
    return a    

def reset_calc(finished_var, a): #tornar para o var_b e var _oper
    if a == 00.0:
        finished_var = True
        return finished_var                    
    else:   
        oper = str(input(""))
        b = float(input(""))
                
        single_operation(a,b,oper)
                    
def priorite(a):#arrumar
    list_convert = []
    lists = list(a)

    for element in lists:
        for i in range(11):
            match element:
                case element:
                    try:
                        float(element[i])
                    finally:                       
                        match element:
                            case '+':
                                list_convert.append('+')
                            case '-':
                                list_convert.append('-')
                            case '*':
                                list_convert.append('*')
                            case '**':
                                list_convert.append('**')
                            case '/':
                                list_convert.append('/')
                            case 'v':
                                list_convert.append('v')     
    print(list_convert)   

def operation():
    finished_select = False
    finished_var = False
    
    while finished_select != True:
        select = int(input("single-calc (1) or multi-calc (2): "))
        
        while finished_var != True:
            if select == 1:
                a = (input(""))
                
                priorite(a)
                
                reset_calc(finished_var,a)
                
            elif select == 2:
                a = (eval(input()))
                mult_operation(a)
                
                if a == "":
                    finished_var = True
                
        if select == "":
            finished_select = True

operation()