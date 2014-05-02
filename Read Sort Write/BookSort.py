######################################
# Program: BookSort.py
# Author: Dan Sarauer
# Purpose: Demonstrate use of file read and write and sort functions in python.
# Program will read in a list of books from a file and sort them by title, author, or page count
######################################

###writeFile###
def writeFile(i,sb): #i = type of sort sb = sorted list
    #write the sorted information to the file
    try:
        if i == 0: #title
            print'\nThe following will was written to file Books_by_Title.txt:'
            b = open('Books_by_Title.txt','w') #open file for writing
        elif i == 1: #page count
            print'\nThe following will was written to file Books_by_PageCnt.txt:'
            b = open('Books_by_PageCnt.txt','w') #open file for writing
        else: #author
            print'\nThe following will was written to file Books_by_Author.txt:'
            b = open('Books_by_Author.txt','w') #open file for writing

        for book in sb:
            b.write('|'.join(book)+'\n') #write info to file
            print '|'.join(book) #write file info to screen

        print '\n' #print some space before the menu gets re-prompted
        b.close()
    except IOError as e:
        print 'Failed to write information to file.\n\n'

###sortOption###
def sortStuff(x):
    #create some containers to hold information
    books = []
    booksSorted = []

    ## Build List
    #open the source file and read contents in
    try:
        with open('Books.txt') as bookSource: #open source file for reading
            for line in bookSource: #read each line of the source file
                #item = line.split('|')[x] #retreive item they are searching by
                line = line.rstrip('\n').split('|')
                if len(line) > 1: #only add lines with data
                    books.append(line) #add this item to the list
        
        booksSorted = sorted(books, key=lambda book: book[x]) #sort on entered item
        bookSource.close() #close the source file

        #write sorted list to file
        writeFile(x,booksSorted)
    except IOError as e: #catch file IO error
        print 'Failed to open file for reading.\n\n'

###Main###
c = True #Continue prompting until they are done running the program

while c:
    print '1:By Title\n2:By Author\n3:By Page Count\n4:Exit'
    opt = raw_input('Sort how: ')

    try:
        opt = int(opt)
    except ValueError as e:
        print 'Your selection must be a number between 1 and 4'
    else:
        if opt == 1:
            sortStuff(0) #sort by Title
        elif opt == 2:
            sortStuff(2) #sort by Author
        elif opt == 3:
            sortStuff(1) #sort by Page Count
        elif opt == 4:
            c = False
        else:
            print 'Your selection must be between 1 and 4. Please try again.\n\n'
