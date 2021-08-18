
try:
    my_file = open('newpy.txt','a')
    my_num = int('w')
    my_list = [1,"two",3]
    my_temp = {"w":1,'z':2}
    my_file.write(str(my_num))

except ValueError as ve:
    with open(newpy.txt,'a') as error_log:
        error_log.write("you tachat")
        raise ValueError("you tacht mesparrr ata lo yahcol lechtov")
    

finally:
    my_file.close()