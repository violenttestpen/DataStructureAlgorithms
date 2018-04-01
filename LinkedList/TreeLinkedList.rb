load '../Miscellaneous/Node.rb'

class TreeLinkedList
    def initialize
        @head  # of type Node
    end
    
    def append(data)
        # initialize the head if it's an empty LinkedList
        if @head.nil?
            @head = Node(data)
        else
            # traverse until the last node (next is nil)
            current = @head
            current = current.next until current.next.nil?
            current.next = Node(data)
        end
    end
    
    def prepend(data)
        new_head = Node(data)
        new_head.next = @head
        @head = new_head
    end
    
    def delete_with_value(data)
        # proceed only if there are values in the LinkedList
        return nil if @head.nil?
        # special case if the head contains the value we wanted
        if @head.data == data then
            @head = @head.next
        end
    
        current = @head
        until current.next.nil?
            if current.next.data == data then
                current.next = current.next.next
            end
            current = current.next
        end
    end
end
