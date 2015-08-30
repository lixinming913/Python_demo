#try select_sort algorithm

def SelectSort(array):
    n = len(array);
    for i in range(0, n):
        min = i;
        for j in range(i+1, n):
            if(array[j] < array[min]):
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
    
    print array
    

def main():
    numbers = [50, 10, 20, 40, 70, 30, 90, 80, 60]
    SelectSort(numbers)

if __name__ == '__main__':
    main()
