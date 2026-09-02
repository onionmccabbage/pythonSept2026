# read text from a file

def readTextFile():
    '''retrieve the contents of a text file'''
    fin = False
    try:
        # there is an alternative syntx for file access objects
        with open('my_text.txt', 'rt') as fin: # 'rt' means read text 
            # .read() retrieves the entire contents
            # .readlines() retrieves the entire contents as a list of single lines
            r = fin.read()
            return r
        # NB using 'with' will automatically close the file access object

    except Exception as err:
        print(f'problem: {err}')
    finally:
        if fin:
            fin.close() # tidy up in case there was an exception

if __name__ == '__main__':
    p = readTextFile()
    print(p)