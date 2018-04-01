class ArrayStack
    def initialize
        @data = []
    end
    
    def empty?
        return @data.empty?
    end
    
    def peek
        return @data.last
    end
    
    def push(data)
        @data << data
    end
    
    def pop
        return @data.pop
    end
end
