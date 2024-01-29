#Ex:1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("The factorial of 5 is:",result)

#Ex:2

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
result = fibonacci(7)
print("The 7th term in the Fibonacci sequence is:",result)

#Ex:3

def sum_of_digits(n):
    if n < 0:
        return "Please enter a non-negative integer."
    elif n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
result = sum_of_digits(987)
print("The sum of digits in the number 987 is:",result)

#Ex:4

def sum_of_digits_with_loop(n):
    if n < 0:
        return "Please enter a non-negative integer."
    digit_sum = 0
    for digit in str(n):
        digit_sum += int(digit)
    return digit_sum
result = sum_of_digits_with_loop(987)
print("The sum of digits in the number 987 (using a loop) is:",result)

#Ex:5

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
result=power(2,6) 
print(result)


 
def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
result=binary_search(1,'target',6,90)
print(result) 

#Ex:6

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
result=reverse_string('hema') 
print(result)

#Ex:7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) 
result=gcd(10,20) 
print(result)
    
#Ex:8
    
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
result=is_palindrome('prasad') 
print(result) 


def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)
def flood_fill(matrix, row, col, new_color, original_color):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] != original_color:
        return
    
    matrix[row][col] = new_color
    flood_fill(matrix, row + 1, col, new_color, original_color)
    flood_fill(matrix, row - 1, col, new_color, original_color)
    flood_fill(matrix, row, col + 1, new_color, original_color)
    flood_fill(matrix, row, col - 1, new_color, original_color) 



memo = {}
def factorial_memoized(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial_memoized(n - 1)
        memo[n] = result
        return result
    
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n) 

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
    
def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)
    
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def fibonacci_series(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_series(n - 1)
        series.append(series[-1] + series[-2])
        return series
    
def exponentiate(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = exponentiate(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = exponentiate(base, (exponent - 1) // 2)
        return base * half_power * half_power
    
def exponentiate(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = exponentiate(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = exponentiate(base, (exponent - 1) // 2)
        return base * half_power * half_power 
    
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    s = s.lower()
    if not s:
        return 0
    elif s[0] in consonants:
        return 1 + count_consonants(s[1:])
    else:
        return count_consonants(s[1:])
    
class TreeNode:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.value)
        result.extend(inorder_traversal(root.right))
    return result

def subset_sum(nums, target):
    if target == 0:
        return True
    elif not nums:
        return False
    else:
        return subset_sum(nums[1:], target - nums[0]) or subset_sum(nums[1:], target)
    
class ListNode:
    def init(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    if not head or not head.next:
        return head
    else:
        new_head = reverse_linked_list(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
def generate_pascals_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(n - 1)
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i - 1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)
        return triangle
    
def generate_pascals_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(n - 1)
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i - 1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)
        return triangle 