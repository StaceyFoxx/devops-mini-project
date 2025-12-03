class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return " -> ".join(nodes) + " -> None"

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def insert_at_head(self, data):
        """Inserts a new node at the head of the list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Inserts a new node at the tail of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def size(self):
        """Returns the size of the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def search(self, data):
        """Searches for a node with the given data."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next_node
        return None

    def delete(self, target_data):
        """Deletes the first occurrence of the node with the given data."""
        current = self.head
        previous = None
        while current:
            if current.data == target_data:
                if previous is None:  # This lines means that our target is actually the head itself. We del the head next line
                    self.head = current.next_node
                else:
                    previous.next_node = current.next_node # here is were the actual del happens. Note the it done with just pointer changes
                return True
            previous = current
            current = current.next_node
        return False  # Data not found


# Example Implementation
# Create a new linked list
linked_list = LinkedList()

# Insert elements
linked_list.insert_at_head(30)
linked_list.insert_at_head(20)
linked_list.insert_at_head(10)
linked_list.insert_at_tail(666)

# Display the list
print("Linked List:")
print(linked_list)

# Size of the list
print("\nSize of the list:", linked_list.size())

# Search for a node
print("\nSearching for 20...")
node = linked_list.search(20)
print("Found node:", node.data if node else "Not found")

# Delete a node
print("\nDeleting 666...")
linked_list.delete(666)
print(linked_list)
