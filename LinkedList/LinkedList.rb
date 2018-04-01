load '../Miscellaneous/Node.rb'

class LinkedList
    def head
        @head  # of type Node
    end
    
    def append(data)
        # initialize the head if it's an empty LinkedList
        if @head.nil?
            @head = Node(data)
            return
        end

        # traverse until the last node (next is nil)
        current = @head
        current = current.next until current.next == nil
        current.next = Node(data)
    end
    
    def prepend(data)
        newHead = Node(data)
        newHead.next = @head
        @head = newHead
    end
    
    def delete_with_value(data)
        # proceed only if there are values in the LinkedList
        return nil if @head.nil?
        # special case if the head contains the value we wanted
        if @head.data == data then
            @head = @head.next
        end
    
        current = @head
        until current.next == nil
            if current.next.data == data then
                current.next = current.next.next
            end
            current = current.next
        end
    end
end