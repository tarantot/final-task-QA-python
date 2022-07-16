import sqlite3
import datetime
 
def final_task_DB():
    
    conn = sqlite3.connect("final_task_DB.db") 
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE employees ('personal ID' integer PRIMARY KEY, 
                                              'full name' text NOT NULL, 
                                              'sex' text NOT NULL, 
                                              'age' text NOT NULL,
                                              'phone number' integer NOT NULL)""")
    
def add_to_final_task_DB():
    for personal_ID = 0:
        personal_ID+=1
    emp_age = datetime.emp_bdate - datetime.date.today()
    emp_sex = emp_sex.upper()
    if emp_sex is not 'М' is not 'Ж':
        print('Пожалуйста выберите корректное значение!')
    for emp_phonenumber != 0:
        data = json.load(open('countries&codes.json'))
        for name in data['countries&codes'].items():
            if emp_phonenumber==dial_code:
                reply = input('Are you from {0}? Y / N'.format(name))
                if reply=='Y':
                    emp_phonenumber = input('Please type your phone number with the country code +XXX : ')
                else:
                    emp_phonenumber = input('Please type your valid phone number! ')
    
    conn = sqlite3.connect("final_task_DB.db") 
    cursor = conn.cursor()
    cursor.execute("""INSERT into employees VALUES (personal_ID, emp_full_name, emp_sex, emp_age, emp_phonenumber)""" )    
    
    conn.commit()
    cursor.close()
    conn.close()
    
final_task_DB()

import re

def srch_final_task_DB():
    input_filename = '../final_task_DB.db'
    results_filename = '../results.txt'

    inputfile = (input_filename, mode='r', encoding='UTF-8')
    resultfile = (results_filename, mode='w', encoding='UTF-8')
    mytext = inputfile.read()

    srch_parameter = srch_parameter.casefold()
    if srch_parameter is not 'full name' is not 'phone number':
        print('Please choose a correct option!')
    srch = srch.casefold()
    results = re.findall(srch, mytext)
    
    if srch_parameter=='full name':
        for title, in cursor.execute('SELECT "full name" FROM employees WHERE "full name" LIKE ?', [srch]):
        print(title)
        resultfile.write(results)
    else:
        for title, in cursor.execute('SELECT "phone number" FROM employees WHERE "phone number" LIKE ?', [srch]):
        print(title)
        resultfile.write(results)
    
    for result in results:
        regex = re.compile(result)
        match = re.search(regex, inputfile)
        if match:
            print('Found "{}" in "{}"'.format(result))
            text_pos = match.span()
            print(text[match.start():match.end()])
            resultfile.write(results)
        else:
            print('Did not find "{}"'.format(srch))