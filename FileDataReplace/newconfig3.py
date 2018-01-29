# Script to read template config file to replace the contents into ini_config file data
# After this script is run, run a command to delete the current file and then rename the new file created here as current file

config_new = open("config_write_new.txt",'w')
config_cur = open("config_write.txt","r")
template   = open("ini_template.txt","r")

# for copying arcot1 lines from template file
def write_from_template_arcot1():
    for line in template:
        if '[copy:arcot1]' in line:
            for line in template:
                if not '[copy:arcot2]' in line:
                    config_new.write(line)
                else:
                    return()

# for copying arcot2 lines from template file
def write_from_template_arcot2():
    template   = open("ini_template.txt","r")
#    print "in arcot2 function"
    for line in template:
        if '[copy:arcot2]' in line:
#            print "in 1arcot2 lines"
            for line in template:
#                print "in 2arcot2 lines"
                if not '[copy:arcot3]' in line:
#                    print "in 3arcot2 lines"
                    config_new.write(line)
                else:
                    return()

# for copying arcot3 lines from template file
def write_from_template_arcot3():
    template   = open("ini_template.txt","r")
    for line in template:
        if '[copy:arcot3]' in line:
            for line in template:
                if not '[copy:arcot4]' in line:
                    config_new.write(line)
                else:
                    return()


# for handling arcot1 lines
str_found = False
for line in config_cur:
    if '[copy:arcot1]' in line:
        str_found = True
        config_new.write(line)
        write_from_template_arcot1()
        break
    if not str_found:
        config_new.write(line)

# for handling arcot2 lines
str_found = False
for line in config_cur:
    if '[copy:arcot2]' in line:
        str_found = True
        config_new.write(line)
#        print "calling arcot2 function"
        write_from_template_arcot2()
        break
#    if not str_found:                 -->assuming arcot2 comes immidiately after arcot1 lines
#        config_new.write(line)

str_found = False
for line in config_cur:
    if '[copy:arcot3]' in line:
        str_found = True
        config_new.write(line)
#        print "calling arcot3 function"
        write_from_template_arcot3()
        break
#    if not str_found:                 -->assuming arcot3 comes immidiately after arcot1 lines
#        config_new.write(line)

print "Happy Ending!!!"            
