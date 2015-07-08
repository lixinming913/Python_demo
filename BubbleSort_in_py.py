#try buble algorithm

def bubbleSort(numbers):
    
    for i in xrange( 0, len(numbers), 1 ):
        for j in xrange( len(numbers) - 1, i , -1 ):
            if(numbers[ j ] < numbers[ j-1 ]):
                numbers[j],numbers[j-1] = numbers[j-1],numbers[j];
    print numbers

def main():
    numbers = [50, 10, 20, 40, 70, 30, 90, 80, 60]
    bubbleSort(numbers)

if __name__ == '__main__':
 main()
