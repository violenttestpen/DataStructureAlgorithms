load '../Miscellaneous/Node.rb'

class TreeStack
    def initialize
        @top = nil
    end
    
    def empty?
        return @top.nil?
    end
    
    def peek
        return nil if @top.nil?
        return @top.data
    end
    
    def push(data)
        node = Node.new(data)
        node.next = @top
        @top = node
    end
    
    def pop
        data = @top.data
        @top = @top.next
        return data
    end
end
