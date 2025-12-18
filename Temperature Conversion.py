input_file=open('temperatures.txt','r') 
output_file=open('results.txt','w') 
list_of_lines=input_file.readlines() 

def fahrenheit_to_celsius(F_temp): 
    return (F_temp-32)*5/9 

def celsius_to_fahrenheit(C_temp): 
    return (C_temp*9/5)+32 


for line in list_of_lines: 
    line = line.strip() 
    if line.endswith('C'): 
        C_temp = float(line[:-1]) 
        F_temp = celsius_to_fahrenheit(C_temp) 
        output_file.write(f"{line}={F_temp:.2f} F\n") 
    elif line.endswith('F'):  
        F_temp = float(line[:-1]) 
        C_temp = fahrenheit_to_celsius(F_temp) 
        output_file.write(f"{line}={C_temp:.2f} C\n") 

input_file.close() 
output_file.close() 

print('Conversion complete. Check the file called results.txt') 
