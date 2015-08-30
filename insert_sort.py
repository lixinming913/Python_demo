#try select_sort algorithm

def InsertSort(array):
    n = len(array);
    for i in range(2, n):
        if array[i] < array[i-1]:
            temp = array[i];
            index = i;         #记录待插入位置
            for j in range(i-1, 0, -1):
                if array[j] > temp:
                    array[j+1] = array[j]
                    index = j; #记录待插入位置
                else:
                    break;
            array[index] = temp;
    
    print array
    

def main():
    numbers = [0, 50, 10, 20, 40, 70, 30, 90, 80, 60]
    InsertSort(numbers)

if __name__ == '__main__':
    main()
