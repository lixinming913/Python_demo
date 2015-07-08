#Create a queue class module
#reference to "data structures and algorithms in Python"

class ArrayQueue:
    """FIFO"""
    DEFAULT_CAPASITY = 10

    def __init__( self ):
        """queue initiation, empty queue"""
        
        self.data = [ None ] * ArrayQueue.DEFAULT_CAPASITY
        self.size = 0
        self.front = 0

    def __len__( self ):
        """the number of queue"""

        return self.size 

    def is_empty( self ):
        """Return True if Queue is empty"""

        return self.size == 0

    def enqueue( self, e ):
        """Add e in the queue"""

        self.data.append( e )
        self.size += 1
        

    def first( self ):
        """Return the element at the first of array queue.
        if empty queue, return -1.
        """

        if self.is_empty():
            raise Exception( ' Queue is empty ' )
            return -1
        else:
            return self.data[ self.front ]

    def dequeue( self ):
        """Remove and return the first element of the queue(i.e,FIFO).
        Raise empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception( ' Queue is empty ' )
            return
        answer = self.data[ self.front ]
        self.data[ self.front ] = False
        self.front = (self.front + 1) % len( self.data )
        self.size -= 1
        return answer
    
        
        
        
