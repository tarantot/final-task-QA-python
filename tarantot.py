import json
import datetime

def welcome():
    name = str(input('Please type your name: '))
    surname = str(input('Please type your surname: '))
    patronymic = str(input('Please type your father\'s name: '))
    sex = input('Please choose your gender: М / Ж ')
    sex = sex.upper()
    if sex is not 'М' is not 'Ж':
        print('Please choose a correct option')
    marital_status = input('Are you married? ДА / НЕТ ')
    marital_status = marital_status.upper()
    if marital_status is not 'ДА' is not 'НЕТ':
        print('Please choose a correct option')
    if sex=='M' and patronymic[-1]=='ж''ш''ч''щ''ц''а''у''ы''о''а''и' :
        patronymic+='евич'
        print ('Welcome on-board, Mr. '+name+' '+patronymic+' '+surname+'!')
    elif sex=='M' and patronymic[-1]=='б''г''д''з''к''л''м''н''п''р''с''т''ф''х':
        patronymic+='ович'
        print ('Welcome on-board, Mr. '+name+' '+patronymic+' '+surname+'!')
    elif sex=='M' and patronymic[-1]=='й':
        patronymic = str(patronymic[-1:]+'евич')
        print ('Welcome on-bard, Mr. '+name+' '+patronymic+' '+surname+'!') 
    elif patronymic=='Василий':
            patronymic = str('Васильевич')
            print ('Welcome on-board, Mr. '+name+' '+patronymic+' '+surname+'!') 
    elif sex=='F' and  marital_status=='N':
        if patronymic[-1]=='ж''ш''ч''щ''ц''а''у''ы''о''а''и' :
            patronymic+='евна'
            print ('Welcome on-board, Ms. '+name+' '+patronymic+' '+surname+'!')
        elif patronymic[-1]=='б''г''д''з''к''л''м''н''п''р''с''т''ф''х':
            patronymic+='овна'
            print ('Welcome on-board, Ms. '+name+' '+patronymic+' '+surname+'!')
        elif patronymic[-1]=='й':
            patronymic = str(patronymic[-1:]+'евна')
            print ('Welcome on board, Ms. '+name+' '+patronymic+' '+surname+'!') 
        elif patronymic=='Василий':
            patronymic = str('Васильевна')
            print ('Welcome on-bard, Ms. '+name+' '+patronymic+' '+surname+'!') 
    elif sex=='F' and  marital_status=='Y':
        if patronymic[-1]=='ж''ш''ч''щ''ц''а''у''ы''о''а''и' :
            patronymic+='евна'
            print ('Welcome on board, Mrs. '+name+' '+patronymic+' '+surname+'!')
        elif patronymic[-1]=='б''г''д''з''к''л''м''н''п''р''с''т''ф''х':
            patronymic+='овна'
            print ('Welcome on-board, Mrs. '+name+' '+patronymic+' '+surname+'!')
        elif patronymic[-1]=='й':
            patronymic = str(patronymic[-1:]+'евна')
            print ('Welcome on-board, Mrs. '+name+' '+patronymic+' '+surname+'!') 
        elif patronymic=='Василий':
            patronymic = str('Васильевна')
            print ('Welcome on board, Mrs. '+name+' '+patronymic+' '+surname+'!') 
    
#def age():
#    dob_input = input("Please type your date of birth yyyy.mm.dd : ")
#    dob_input = dob_input.split('.')
#    dob = datetime.date(int(dob_input[0]),int(dob_input[1]),int(dob_input[2]))
#    today = datetime.date.today()
#    user_age = dob - today
#    if user_age.split()[0]<0:
#        print('Are you a ghost?????????????')
#    else:
#        print('For now you are {2} years old, {1} months old, {0} days old!'.format(yyyy,mm,dd))
#    data = json.load(open('zodiac.json'))
#    for sign, direction, element, unicode_symbol, info in data['eastern_zodiac'].items():
#        if year in info['years']==user_age.split()[2]:
#            print ("Your Chinese zodiac sign is {0};\n - direction is {1};\n - nature element is {2};\n - unicode symbol is {3}!".format(sign, direction, element, unicode_symbol))