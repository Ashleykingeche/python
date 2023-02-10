
numbers = [45,67,34,76,23,45]

print(len(numbers))

for i in range(len(numbers)):
    print(numbers[i])
    #INSERT - inserts an element x at an index y
    numbers.insert(2,100)
    for i in range(len(numbers)):
        print(numbers[i])
    
    #SORT -arranges the list in order
    numbers.sort()
    #add a new line for formated output
    print("/n")
    
    for i in range(len(numbers)):
        print(numbers[i])
        
        for i in range (10):
            #insert elements into the list
            nums.append(i)
            
            even_nums = []
            
            for num in range(20):
                if(num%2==0):
                    even_nums.append(num)
            
            for i in range(len(even_nums)):
                print(even_nums[i])
                
                
                #
    