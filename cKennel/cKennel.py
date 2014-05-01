#! usr/bin/env python

#Program: cKennel.py
#Author: Dan Sarauer (pronounced Sar-are)
#Modified: 4/29/2014
#Description: Trying my hand at a bit of python code and used the example of a kennel.
#  The program will get input from the user as to what they would like to do:
#    1. See who the kennel has available
#    2. Put a pet up for adoption
#    3. Adopt a pet
#    4. Exit the program
#  I've done my set to sanitize all input so that we don't have weird values going all over the place or into the file where I'm storing the
#  "inventory" that is our list of pets at the kennel.

def listPets():
        #if the kennel has pets to give it will list them
        try:
                cKennel = open('CodingKennels.txt', 'r') #open the file
                guestsOfTheKennel = cKennel.read() #read file contents into a variable named guestsOfTheKennel
                cKennel.close() #close the file

                availableFriends = guestsOfTheKennel.split(',') #split the guests into their own kennels
                
        except IOError:
                print 'I/O error({0}): {1}'.format(e.errno, e.strerror)

        if len(availableFriends) >= 1:
                print '\n///////////////////////////'
                print '// OUR AVAILABLE FRIENDS //'
                print '///////////////////////////\n'

                for friend in availableFriends:
                        name, race, sex, age, breed, note = friend.split(':') #split the pets stats into easily referenced areas
                        if sex == 'm':
                                print 'We have a {0} named {1}.  He is a {2} year old {3}.\nNote: {4}\n'.format(race, name, age, breed, note)
                        else:
                                print 'We have a {0} named {1}.  She is a {2} year old {3}.\nNote: {4}\n'.format(race, name, age, breed, note)
        else: #if there is nothing to list it will exit and re-prompt the menu
                print '\n\nOops, looks like we don\'t have any pets right now!'
                print 'Try again later...maybe a friend will come along for you!\n\n'
	
def givePetUp():
	entryComplete = False
	validInput = False
	
	print 'Sorry to hear that, but we are glad to add another member to our family here!\n'
		
	print 'We\'ll need some information on the pet in question...'
	name = raw_input('Name (Alpha characters only please):')
	race = raw_input('Race of animal (example: cat):')
	sex = raw_input('Sex (m/f):')
	age = raw_input('Age:')
	breed = raw_input('Breed (example: Golden Retriever):')
	note = raw_input('Notes about them (example: Playful):')
	
	while not entryComplete:		
		#after prompting for all of this we should sanitize it before writing it to inventory
		
		#clean up string fields
		name = name.translate(None,'~`!@#$%^&*()_+=-|}{\][":\';?></.,1234567890') #remove symbols and numbers from name
		race = race.translate(None,'~`!@#$%^&*()_+=-|}{\][":\';?></.,1234567890') #remove symbols and numbers from race
		breed = breed.translate(None,'~`!@#$%^&*()_+=-|}{\][":\';?></.,1234567890') #remove symbols and numbers from breed
		note = note.translate(None,'~`!@#$%^&*()_+=-|}{\][":\';?></.,1234567890') #remove symbols and numbers from note
		
		while not validInput: #go through and re-prompt if necessary
			#validate number fields
			if sex == 'm' or sex == 'f': #sex must be either m or f
				try:
					int(age) #Age must be an integer
					validInput = True #if sex is m|f and age is an int, assume correct information
				except ValueError:
					print '\nAge must be a number...'
					age = raw_input('Age:') #re-prompt for the correct age
			else:
				print '\nPlease enter either m or f for sex...'
				sex = raw_input('Sex (m/f):')

		print '\nYou entered:'
		print 'Name: {0}\nrace: {1}\nSex: {2}\nAge: {3}\nBreed: {4}\nNote: {5}\n'.format(name,race,sex,age,breed,note)
		confirmEntry = raw_input('Is the entered information correct?(y/n):')

		if confirmEntry == 'y': #prep animal for admittance
			
			# join the elements together like name:race:sex:age:breed:note
			newFriend = ':'.join([name,race,sex,age,breed,note])
						
			cKennel = open('CodingKennels.txt', 'a') #open the file for appending
			cKennel.write(',' + newFriend) #write new friend to file
			cKennel.close() #close the file
			
			entryComplete = True #flag to end selection process
			
		elif confirmEntry == 'n':
			#which one is bad
			badData = raw_input('Sorry about that...\n\nWhich one would you like to change?(name,race,sex,age,breed,note):')
			
			#make sure they selected something available
			if badData == 'name':
				name = raw_input('Name (Alpha characters only please):') #re-enter name
			elif badData == 'race':
				race = raw_input('race of animal (example: cat):') #re-enter race
			elif badData == 'sex':
				sex = raw_input('Sex (m/f):') #re-enter sex
			elif badData == 'age':
				age = raw_input('Age:') #re-enter age
			elif badData == 'breed':
				breed = raw_input('Breed (example: Golden Retriever):') #re-enter breed
			elif badData == 'note':
				note = raw_input('Notes about them (example: Playful):') #re-enter note
			else:
				print 'Invalid entry! Try again...' #why can't you race?
		else:
			print '\nInvalid entry! Try again....\n' #really?!?! you can't race y or n? come on!

def adoptPet():
	#if the kennel has pets to give it will list them
	try:
		cKennel = open('CodingKennels.txt', 'r') #open the file for reading
		guestsOfTheKennel = cKennel.read() #read file contents into a variable named guestsOfTheKennel
		cKennel.close() #close the file
		
		availableFriends = guestsOfTheKennel.split(',') #split the guests into their own kennels
			
		
		print '\nFantastic!  You are going to make some special animal very happy!' #Yay we have a customer!
		
		cleanInput = False #Assume user will enter something wrong
		
		while cleanInput ==  False:
			headCount = 1 #simple counter for a list of our animals
			
			for friend in availableFriends: #list animals available
				name, race, sex, age, breed, note = friend.split(':') #split the pets stats into easily referenced areas
				print '{0}:{1} is a {2} year old {3}.'.format(headCount, name, age, breed) #personalized listing for our furry-friends
				headCount += 1 #advance count for list reasons
			
			print '{0} Go back...'.format(headCount)
			
			choice = raw_input('\nWhich one of these lovely animals would you like to make friends with?:') #who will be the chosen one?
			
			try: #time to validate user input
				choice = int(choice) #attempt to parse the choice to an integer
				
				if 1 <= choice <= len(availableFriends):				
					choice -= 1 #convert choice to the index they chose
					
					name, race, sex, age, breed, note  = availableFriends[choice].split(':') #get their choice animals stats
					print '\nYou chose {0}!'.format(name) #confirm their selection
					
					confirm = raw_input('Is this correct? (y/n)') 
					if confirm == 'y':
						print '\n\nGreat! {0} is very excited to go home with you today!\n'.format(name) #prep their animal for the trip
						
						del availableFriends[choice] #remove friend from our inventory
						
						if len(availableFriends) > 1:
							updateFriends = ','.join(availableFriends) #string together the list of furry-friends for writing to the file
						else:
							updateFriends = ''.join(availableFriends) #convert the last element into a string to write to the file
						
						cKennel = open('CodingKennels.txt', 'w') #open the file for writing
						cKennel.write(updateFriends) #write list back to file to update inventory
						cKennel.close() #close the file
						
						cleanInput = True #flag to end selection process
						
					elif confirm == 'n':
						print '\nOh, sorry about that. Let\'s try again...\n' #start the selection process over
					else:
						print '\nInvalid entry! Please start your selection process over.\n' #stop messing with the program input people!
				elif choice == (len(availableFriends)+1):
					print '\nSecond thoughts?\n\n' #you are making kittens cry!
					cleanInput = True #flag to end selection process
				else:
					# print 'Index out of range.'
					print '\nInvalid entry detected. Please choose an option 1-{0}...\n'.format(headCount) #people always be messin' with my inputz
			except ValueError:
				# print 'Can\'t parse integer'
				print '\nInvalid entry detected. Please choose an option 1-{0}...\n'.format(headCount) #people always be messin' with my inputz	
	except: #if there is nothing to list it will exit and re-prompt the menu
		print '\n\nOops, looks like we don\'t have any pets right now!'
		print 'Try again later...maybe a friend will come along for you!\n\n'
	
ans = True #boolean flag to keep things running smooth
greeting = True #enable the greeting for first time visitors

while ans:
	if greeting: #if greeting is set to true display the greeting sign
		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		print '!! WELCOME TO CODING KENNELS !!'
		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		
	print '\nHow can we help you today?:' 
	print '1. Display a list of pets available.' #Who needs some love
	print '2. Put pet up for adoption.' #Share the love with others
	print '3. Adopt a pet.' #Let's get a friend
	print '4. Exit' #Option to exit
	
	option = raw_input('\nPlease enter you selection:') #Get the users option and assign it to the option variable
	
	#sanitize the input
	try: #attempt to cast input as integer
		option = int(option)
		
		#make sure input is between 1-4 (our options)
		if option == 1: #Who needs some love
			listPets() #list our available friends
			greeting = False #disable the greeting for the duration of our users visit
		elif option == 2: #Share the love with others
			givePetUp() #someone will need a hug
			greeting = False
		elif option == 3: #Let's get a friend
			adoptPet() #tail wagging everywhere
			greeting = False
		elif option == 4: #Option to exit
			print '\nThank you for visiting.  Come again!'
			raw_input('Press enter to continue')
			ans = False
		else:
			print '\nValue must be between 1 and 4...\n'
	except ValueError:
		print '\nInvalid entry detected. Please choose an option 1-4...\n'
