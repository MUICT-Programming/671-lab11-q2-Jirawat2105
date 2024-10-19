def summation(lst1, lst2):
    updated_list = [x + y for x, y in zip(lst1, lst2)]
    return updated_list

def find_min_max(lst):
    min_val = min(lst)
    max_val = max(lst)
    return min_val, max_val

def main():
    n = int(input())
    lst1 = [int(input()) for i in range(n)]
    lst2 = [int(input()) for i in range(n)]
    updated_list = summation(lst1, lst2)
    print(updated_list) 
    min_val, max_val = find_min_max(updated_list)
    print((min_val, max_val))  
main()
