import csv

text_list = []

with open("Cookclub_Application.csv","r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 24)
        text_list.append(" "+"\n".join(line))
        #text_list.append("\n".join(line))

with open('Cookclub_Application.txt', "w") as my_output_file:

    my_output_file.write("No.")
    #my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line+ "\n" + "__________________________________________________________" +"\n"  )
        my_output_file.write("No.")
    print('File Successfully written.')
