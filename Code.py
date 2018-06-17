#language france have a lot of exceptions in verbs and will not work on them.

import re

print("1- for group ER\n2- for group IR and RE\n")

verb_group = input()

try:
    int(verb_group)
    if ValueError == True:
        print("Not valid ")
    elif verb_group == '1':
        verbask = input().upper()
        verbJe = re.sub('ER','E',verbask)
        verbTu = re.sub('ER','ES',verbask)
        verbElle = re.sub('ER','E',verbask)
        verbNous = re.sub('ER','ONS',verbask)
        verbVous = re.sub('ER','EZ',verbask)
        verbElles = re.sub('ER','ENT',verbask)
        
        if verbask == 'MANGER':
            print('Je',verbJe,'\nTu',verbTu,'\nIl/Elle/On',verbElle)
            verbNous = re.sub('ER','EONS',verbask)
            print('\nNous',verbNous,'\nVous',verbVous,'\nIls/Elles',verbElles)
        else:
            print('Je',verbJe,'\nTu',verbTu,'\nIl/Elle/On',verbElle)
            print('\nNous',verbNous,'\nVous',verbVous,'\nIls/Elles',verbElles)

    elif verb_group == '2':
        verbask = input().upper()
        verbJe = re.sub('IR','IS',verbask)
        verbTu = re.sub('IR','IS',verbask)
        verbElle = re.sub('IR','IT',verbask)
        verbNous = re.sub('IR','ISSONS',verbask)
        verbVous = re.sub('IR','ISSEZ',verbask)
        verbElles = re.sub('IR','ISSENT',verbask)   
        print('Je',verbJe,'\nTu',verbTu,'\nIl/Elle/On',verbElle)
        print('\nNous',verbNous,'\nVous',verbVous,'\nIls/Elles',verbElles)

except ValueError:
    print("Value Error")    
