# A function that reverses the order of lines in a file

import stack_demo

def reverse_file( filename ):
    """overwrite given file with its contents line-by-line reversed."""
    
    s = stack_demo.ArrayStack()
    original = open( filename )
    
    for line in original:
        s.push( line.rstrip( '\n' ) )        #we will re-insert newlines when writing
                                             #rstrip is used to delete right characters'\n'
    original.close()

    #now we overwrite with contents in LIFO order
    
    output = open( filename, 'w' )           #reopening file overwrites original

    while not s.is_empty():
        output.write( s.top() + '\n' )       #re-insert newline characters
    output.close()
