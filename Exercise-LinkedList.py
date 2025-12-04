class LinkedLists:
    def __init__(self):
        self.head = None  # Empty list

    def insert(self, name, adm, grades):
        new_node = Node(name, adm, grades)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

students = LinkedLists()

students.insert("Alice", "ADM001", [78, 85, 90])
students.insert("Brian", "ADM002", [65, 72, 81])
students.insert("Catherine", "ADM003", [88, 91, 94])

students.display()