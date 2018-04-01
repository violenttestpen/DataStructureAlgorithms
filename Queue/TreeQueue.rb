load '../Miscellaneous/Node.rb'

class TreeQueue
    def initialize
        @head = nil
        @tail = nil
    end
    
    def empty?
        return @head.nil?
    end
    
    def peek
        return nil if empty?
        return @head.data
    end
    
    def enqueue(data)
        node = Node.new(data)
        @tail.next = node unless @tail.nil?
        @head = @tail = node if @head.nil?
        @tail = @tail.next
    end
    
    def dequeue
        return nil if empty?
        
        data = @head.data
        @head = @head.next
        @tail = nil if @head.nil?
        
        return data
    end
end
