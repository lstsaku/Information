def find_min_difference(A, C, n):

  
    min_val = A[0] - C[0]
    index = 0
    
   
    for i in range(1, n):
        diff = A[i] - C[i]
        
   
        if diff < min_val:
            min_val = diff
            index = i
    
    return min_val, index + 1

def main():
   
    n = int(input("Введите количество элементов n: "))
    
   
    print("Введите элементы массива A:")
    A = []
    for i in range(n):
        A.append(float(input(f"A[{i+1}] = ")))
    
    
    print("Введите элементы массива C:")
    C = []
    for i in range(n):
        C.append(float(input(f"C[{i+1}] = ")))
    
 
    min_val, index = find_min_difference(A, C, n)
    
    # Вывод результатов
    print("\n" + "="*40)
    print("РЕЗУЛЬТАТЫ:")
    print("="*40)
    print(f"Минимальная разность (Min_Val): {min_val}")
    print(f"Порядковый номер (Index): {index}")
    print("="*40)
    
 
    print("\nВсе разности A[i] - C[i]:")
    for i in range(n):
        diff = A[i] - C[i]
        marker = " <-- МИНИМУМ" if (i + 1) == index else ""
        print(f"  A[{i+1}] - C[{i+1}] = {A[i]} - {C[i]} = {diff}{marker}")

if __name__ == "__main__":
    main()
