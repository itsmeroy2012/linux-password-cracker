#!/usr/bin/python2.7
#submitted by itsmeroy2012
#A password cracker designed to crack linux hashes of the type SHA-512. 
#Save the file containing the hash in the same directory.
#Put the file that will be used as a dictionary to crack the passwords.
#usage:- 'python passcrack_ir.py -w shadow.txt -f dictionary.txt'
#sample files are provided in the repository
#Run in a linux or ubuntu terminal
import crypt
import optparse
def testPass(hashed,dictionary,salt,username):
	n=0
	dictFile = open(dictionary,'r')
	
	for word in dictFile.readlines():
		n=n+1
		print "[*] Testing "+str(n)+" passwords for username:- "+str(username)
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if(cryptWord == hashed):
			
			print "[+] Found Password: "+word+"\n"
			return
	
	print "[-] Password Not Found.\n"
	return
def main():
	parser=optparse.OptionParser('usage%prog '+'-w <file containing hash> -f <dictionary file>')
	parser.add_option('-w', dest="hash1" , type='string' , help='Specify file containing hash')
	parser.add_option('-f',dest='dictionary', type='string' , help='Specify dictionary file')
	(options,args)=parser.parse_args()
	hash1=options.hash1
	dictionary=options.dictionary
	if (hash1 == None) | (dictionary == None):
		print parser.usage
		exit(0)
	fn=open(hash1,'r')
	for line in fn.readlines():
		if(line!='\n'):
			string1=line.strip('\n')
			A=string1.split(':')
			hashed=A[1]
			username=A[0]
			concated=hashed.split('$')
			salt='$'+concated[1]+'$'+concated[2]+'$'
			testPass(hashed,dictionary,salt,username)


if __name__ == "__main__":
	main()
