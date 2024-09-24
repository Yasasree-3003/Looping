'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
n = int(input())
factorial = 1
k = 1
# Check if n is a factorial number
while factorial < n:
    k += 1
    factorial *= k
if factorial == n:
    print("Yes")
else:
    print("No")
