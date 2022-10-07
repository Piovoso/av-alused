dat_arr = ['liit','jag','korr','miin','vord','min','max']

def input_a(type, numb): #Funktsioon dat_arr pohjal asjadele
    try:
        a1=int(input('arv1: '))
        a2=int(input('arv2: '))
        if numb == 3: a3=int(input('arv3: '))
    except(ValueError):
        print(f'pizdets, njetu number, ainult taht')
        return
    
    match type: #Match case, algne info match taha.
        case 'liit': #Case on juhus mis voib olla vordne Match-iga
            if numb == 3: print(f'{a1}+{a2}+{a3}={a1+a2+a3}')
            else: print(f'{a1}+{a2}={a1+a2}')

        case 'jag':
            if numb == 3: print(f'{a1}/{a2}/{a3}={a1/a2/a3}')
            else: print(f'{a1}/{a2}={a1/a2}')

        case 'miin':
            if numb == 3: print(f'{a1}-{a2}-{a3}={a1-a2-a3}')
            else: print(f'{a1}-{a2}={a1-a2}')
        
        case 'korr':
            if numb == 3: print(f'{a1}*{a2}*{a3}={a1*a2*a3}')
            else: print(f'{a1}*{a2}={a1*a2}')
        
        case 'vord':
            if numb == 3:
                if a1>a2>a3: print(f'{a1} on suurem kui {a2} aga on suurem kui {a3}')
                elif a1<a2<a3: print(f'{a1} on vaiksem kui {a2} aga on vaiksem kui {a3}')
                elif a1<a2>a3: print(f'{a1} on vaiksem kui {a2} aga on suurem kui {a3}')
                elif a1>a2<a3: print(f'{a1} on suurem kui {a2} aga on vaiksem kui {a3}')
                else: print(f'{a1}=={a2}=={a3}')
            else:
                if a1>a2: print(f'{a1} on suurem kui {a2}.') #if taha panen printi kuna see on kompaktsem ja meil ainult yks rida koodi if sees
                elif a1<a2: print(f'{a1} on vaiksem kui {a2}')
                else: print(f'{a1}=={a2}')
        
        case 'max':
            if numb == 3:
                if a1>=a2>=a3: print(f'{a1} on max')
                elif a1<=a2>=a3: print(f'{a2} on max')
                else: print(f'{a3} on max')
            else:
                if a1>=a2: print(f'{a1} on max')
                else: print(f'{a2} on max')
        
        case 'min':
            if numb == 3:
                if a1<=a2<=a3: print(f'{a1} on max')
                elif a1>=a2<=a3: print(f'{a2} on max')
                else: print(f'{a3} on max')
            else:
                if a1<=a2: print(f'{a1} on min')
                else: print(f'{a2} on min')

while True: #alustab proge uuesti kui eelnev saab tehtud.
    dat = input('liit/jag/miin/korr/vord/min/max\ntype:') #\n on uue rea loomine ilma uue print() statementita.
    numb_count = input('numb amount [int][max:3/min:2]: ')
    
    try:
        if len(dat)>0 and dat in dat_arr: # and/or et vorrelda kahte asja yhes if-is. kompaktsem.
            if 2<=int(numb_count)<=3: input_a(dat, int(numb_count))
            else: print(f'err: {numb_count} not <= or >=. Pls buy glasses.')
        else: print(f'err: {dat} not in dat_arr array of acceptable inputs\nacceptable: {dat_arr}')
    except(ValueError): print(f'err: numb_count does not take str. Must be int.')
    # print(f'jutt {var}') annab voimaluse eemaldada komasid ja plusse, vahendab jutumarkide kasutust ja lihtdalt ilusam ja kergem arusaada.