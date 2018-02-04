#!/usr/bin/evn python
#G00940803 Robert Henderson isa562
"""simple_unix_pwd_cracker.py: a
 simple unix passwork cracker."""

import crypt
import getopt
import pdb
import sys

def read_file(filepath):
	file = open(filepath, 'r')
	return file.readlines()

def check_password(pwd_hash, p, salt):
    if(crypt.crypt(p, salt)!=pwd_hash):
        return 0
    else:
        return 1
 
#Reads out the password. Also returns the password. Returns null if there is no match
def pwd_crack_task1(salt, pwd_hash):
#read in the lines and strip the new line from the word
#then hash
#compare the hashes
#break out of the loop once we print the password. #Looks like its Zeus
    w=""
    f=read_file('web2')
    for line in f:
        poss_pass=line.strip("\n")
        match = check_password(pwd_hash, poss_pass, salt)
        if(match>0):
            w=poss_pass
            print("Password is: ", w)
            return w
    return w

def pwd_crack_task2(pwd_hash):

    w=""
#loop through all the words
    f=read_file('web2')
    for line in f:
        poss_pass=line.strip("\n")
        #going through the salts for a given word
        for i in range(65,123):
            if(i==91): #skip [
                 i+=6 #to get to 97 a
            
            a=chr(i)
            for j in range(65,123):
                if(j==91): #skip [
                    j+=6 #to get to 97 a
                b=chr(j)
                salt=a+b
                match = check_password(salt+pwd_hash, poss_pass, salt)
                if(match>0):
                    w=poss_pass
                    print("Password is: ", w)
                    return w
    return w


def pwd_crack_task3(salt, pwd_hash):
    """Please complete this function:
         1) find the concatenation of two words (password) in the given dictionary such that its hash is
            matched to the given hash
         2) print out the word (password) in plaintext
    """
    w=""
    with open('web2') as dictionary_file:
        words_list = dictionary_file.read().splitlines()

    for i in range(0,len(words_list)):
        for j in range(i+1,len(words_list)):
            concatenated_word=words_list[i]+words_list[j]
            #print(concatenated_word)
            match=check_password(pwd_hash, concatenated_word, salt)
            if(match>0):
                w=concatenated_word
                print("Password is: ", w)
                return w
    return w

def main(argv):
	input_file = ''
	task = ''
	try:
		opts, args = getopt.getopt(argv,"hi:t:",["infile=","task="])
	except getopt.GetoptError:
		print('python3 simple_unix_pwd_cracker.py -t <task number> -i <input_file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('python3 simple_unix_pwd_cracker.py -t <task number> -i <input_file>')
			sys.exit()
		elif opt in ("-i", "--infile"):
			input_file = arg
		elif opt in ("-t", "--task"):
			task = arg
	print("Input file: ", input_file)
	print("Task: ", task)

	lines = read_file(input_file);
	if(task == '1'):
		salt = lines[0].rstrip('\n')
		pwd_hash = lines[1].rstrip('\n')
		pwd_crack_task1(salt, pwd_hash)
	elif(task == '2'):
		pwd_hash = lines[0].rstrip('\n')
		pwd_crack_task2(pwd_hash)
	elif(task == '3'):
		salt = lines[0].rstrip('\n')
		pwd_hash = lines[1].rstrip('\n')
		pwd_crack_task3(salt, pwd_hash)

if __name__ == '__main__':
	main(sys.argv[1:])
