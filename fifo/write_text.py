# we can usse a file access object to write and read text files
# I/O is always via the O/S
# we talk about 'IO-bound' operations

def writeToFile(c):
    '''Persist the entire contents of 'c' into a text file'''
    fout = False # we will need this variale in a bit
    try:
        # we need a file access object ( 't' is the default meaning text files )
        fout = open('my_text.txt', 'at') # 'a' will append file is created if it does not already exist
        fout.write(c) # pass the entire contents of 'c' to the file to be appended
        # we may choose to append a new line character
        fout.write('\n')
        fout.close()  # tidy up
    except Exception as err:
        print(f'Problem: {err}')
    finally:
        # if the file access object has not been cleared away, close it now
        if fout:
            fout.close()


if __name__ == '__main__':
    # \n inserts a new line, \t inserts a tab    \\ inserts a \
    mytext = 'this is some dead clever content we need to store...'
    writeToFile(mytext) 