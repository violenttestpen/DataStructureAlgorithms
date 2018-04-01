class ArrayQueue
    def initialize
        @data = []
    end
    
    def empty?
        return @data.empty?
    end
    
    def peek
        return @data.first
    end
    
    def enqueue(data)
        @data << data
    end
    
    def dequeue
        return @data.shift
    end
end
