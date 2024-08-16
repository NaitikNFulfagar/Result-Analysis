import sqlite3

# Connect to the database
conn = sqlite3.connect('./data.db')  # Replace with your database file or connection details
cursor = conn.cursor()
dic = {
       "210241": ["DISCRETE MATHEMATICS", True, False, False, False],
       "210242": ["FUND. OF DATA STRUCTURES", True, False, False, False],
        "210243": ["OBJECT ORIENTED PROGRAMMING", True, False, False, False],
        "210244": ["COMPUTER GRAPHICS", True, False, False, False],
        "210245": ["DIGITAL ELEC. & LOGIC DESIGN", True, False, False, False],
        "210246": ["DATA STUCTURES LABORATORY", False, True, True, False],
        "210247": ["OOP & COMP. GRAPHICS LAB.", False, True, True, False],
        "210248": ["DIGITAL ELEC. LABORATORY", False, True, False, False],
        "210249": ["BUSINESS COMMUNICATION SKILLS", False, True, False, False],
        "210250": ["HUMANITY & SOCIAL SCIENCE", False, True, False, False],
        "207003": ["ENGINEERING MATHEMATICS 3", True, True, False, False], 
        "210252": ["DATA STRUCTURES & ALGO.", True, False, False, False],
        "210253": ["SOFTWARE ENGINEERING", True, False, False, False],
        "210254": ["MICROPROCESSOR", True, False, False, False],
        "210255": ["PRINCIPLES OF PROG. LANG.", True, False, False, False],
        "210256": ["DATA STRUCTURES & ALGO. LAB.", False, True, True, False],
        "210257": ["MICROPROCESSOR LABORATORY", False, True, False, True],
        "210258": ["PROJECT BASED LEARNING 2", False, True, False, False],
        "210259": ["CODE OF CONDUCT", False, True, False, False]}
# Define the queries
with open("divwise.txt", 'w') as file:
    for MYDIV in ['A','B']:
        
        file.write("-------------------------------------------------------------------------------------------------------------\n")
        file.write(f"\n\n{MYDIV} Division\n\n")
        
        q = f'''SELECT name,SGPA FROM SE_COMPUTER_2024_JUNE WHERE div='{MYDIV}' and SGPA!='--' ORDER by SGPA DESC LIMIT 5;'''
        cursor.execute(q)
        result = cursor.fetchall()
        
        file.write(f"{'Name':<30} {'SGPA':<8} \n")
        for res in result:
            print(f'{res[0]} {res[1]}')
            file.write(f"{res[0]:<30} {res[1]:<8} \n")

        file.write("\n\n")

        
        file.write(f"{'Sub Name':<40} {'PRESENT':<8}  {'ABSENT':<8} {'PASS':<8} {'FAIL':<8}\n")
        for key,values in dic.items():
            if values[1] ==True:
                query0 = f"SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _{key}_end!='AB' and div='{MYDIV}';"
                query1 = f"SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _{key}_end='AB' and div='{MYDIV}';"
                query2 = f"SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _{key}_tot>=40 and div='{MYDIV}';"
                query3 = f"SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE _{key}_tot<40 and div='{MYDIV}';"

            # Execute the queries
                cursor.execute(query0)
                result0 = cursor.fetchone()[0]
            
                cursor.execute(query1)
                result1 = cursor.fetchone()[0]

                cursor.execute(query2)
                result2 = cursor.fetchone()[0]

                cursor.execute(query3)
                result3 = cursor.fetchone()[0]

                # Print the results
                print(f"{values[0]:<40} {result0:<8}  {result1:<8} {result2:<8} {result3:<8}")
                
                file.write(f"{values[0]:<40} {result0:<8}  {result1:<8} {result2:<8} {result3:<8}\n")
                
        file.write("\n\n")
        
        file.write(f"{'Sub Name':<40} {'Name':<50}  {'Marks':<8}\n")

        for key,values in dic.items():
            if values[1] ==True:
                query1 = f'''SELECT name,_{key}_tot FROM SE_COMPUTER_2024_JUNE WHERE _{key}_end!="AB" and div='{MYDIV}' ORDER by _{key}_tot DESC LIMIT 1;'''

            # Execute the queries
                cursor.execute(query1)
                result1 = cursor.fetchone()

                # Print the results
                print(f"{key} _ {values[0]}: {result1}")
                file.write(f"{values[0]:<40} {result1[0]:<50}  {result1[1]:<8}\n")


                print("")
        file.write("\n\n")


        query1 = f"""SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div='{MYDIV}' and SGPA!='--' and SGPA>=7.75;"""
        query2 = f"""SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div='{MYDIV}' and SGPA!='--' and SGPA<7.75 and SGPA>=6.75;"""
        query3 = f"""SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div='{MYDIV}' and SGPA!='--' and SGPA<6.75;"""
        query4 = f"""SELECT count(name) FROM SE_COMPUTER_2024_JUNE WHERE div='{MYDIV}' and SGPA='--' ;"""

            # Execute the queries
            
        cursor.execute(query1)
        result1 = cursor.fetchone()[0]     
            
        cursor.execute(query2)
        result2 = cursor.fetchone()[0]

        cursor.execute(query3)
        result3 = cursor.fetchone()[0]

        cursor.execute(query4)
        result4 = cursor.fetchone()[0]
        
        # Print the results
        print(f"{result1:<8} {result2:<8} {result3:<8} {result4:<8}")
        file.write(f"{'Distincation':<15} {'First':<15} {'Higher Second':<15} {'Fail':<15}\n")
                
        file.write(f"{result1:<15} {result2:<15} {result3:<15} {result4:<15}\n")


    # Close the connection
conn.close()
