num=input("");
if (num>='a' and num<='z') or (num>='A' and num<='Z'):
	if (num=='a' or num=='e' or num=='i' or num=='o' or num=='u' or num=='A' or num=='E' or num=='I' or num=='O' or num=='U'):
		print('Vowel')
	else:
		print('Consonant')
else:
	print('Invalid')

