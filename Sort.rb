def swap(array, x, y)
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
end

# insertion sort [O(n**2)]
def isort(array, debug = false)
    a = array.clone
    i = 1 # start from the second element
    
    while i < array.length
        # move left
        x = i - 1
        while x >= 0
            swap(array, x, x + 1) if array[x] > array[x + 1]
            x -= 1
        end
        
        i += 1
        puts array.inspect if debug
    end
    
    return a
end

def ssort(array)
    i = 0
    j = 1
    while i < array.length - 1
        while j < array.length
            
        end
    end
end