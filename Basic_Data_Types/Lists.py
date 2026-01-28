"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N = 4
append 1
append 2
insert 1 3
print

appned 1: Append 1 to the list, arr=[1].
append 2: Append 2 to the list, arr=[1,2] .
insert 1 3: Insert  at index , arr=[1,3,2].
print: Print the array.
Output:
[1, 3, 2]

Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Output Format
For each command of type print, print the list on a new line.

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1] """

if __name__ == '__main__':
    N = int(input()) # Read the number of commands
    lst = []         # Initialize the empty list
    
    for _ in range(N):
        # Split the input line into a list of strings
        command_input = input().split()
        cmd = command_input[0]
        
        if cmd == "insert":
            # command_input[1] is the index, [2] is the value
            lst.insert(int(command_input[1]), int(command_input[2]))
        
        elif cmd == "print":
            print(lst)
            
        elif cmd == "remove":
            lst.remove(int(command_input[1]))
            
        elif cmd == "append":
            lst.append(int(command_input[1]))
            
        elif cmd == "sort":
            lst.sort()
            
        elif cmd == "pop":
            lst.pop()
            
        elif cmd == "reverse":
            lst.reverse()
