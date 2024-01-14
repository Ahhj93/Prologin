class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def addAfter(self, nextdata):
        stock = self.next
        nextNode = Node(nextdata)
        self.next = nextNode
        nextNode.prev = self
        stock.prev = nextNode
        nextNode.next = stock

    def deleteAfter(self):
        stock = self.next
        self.next = self.next.next
        self.next.prev = self
        return stock

    def addBefore(self, prevdata):
        stock = self.prev
        prevNode = Node(prevdata)
        self.prev = prevNode
        prevNode.next = self
        stock.next = prevNode
        prevNode.prev = stock

    def deleteBefore(self):
        stock = self.prev
        self.prev = self.prev.prev
        self.prev.next = self
        return stock
    
    def affiche(self, sens):
        print_text = ""
        tmp_node = self
        if sens == 1:
            while tmp_node.next != self:
                print_text += tmp_node.data + "\n"
                tmp_node = tmp_node.next
            print_text += tmp_node.data
        else:
            while tmp_node.prev != self:
                print_text += tmp_node.data + "\n"
                tmp_node = tmp_node.prev
            print_text += tmp_node.data
        print(print_text)


def simulate_jormungandr(initial, actions):
    current_node = initial
    sens = 1
    eat = []

    for action in actions:
        if action == 'A':
            if sens == 1:
                current_node = current_node.next
            else:
                current_node = current_node.prev
        elif action == 'M':
            if sens == 1:
                eat.append(current_node.prev.deleteAfter().data)
                current_node = current_node.next
            else:
                eat.append(current_node.next.deleteBefore().data)
                current_node = current_node.prev
        elif action == 'R':
            sens *= -1
            if sens == 1:
                current_node = current_node.next
            else:
                current_node = current_node.prev
        elif action == 'C':
            if sens == 1:
                current_node.addBefore(eat.pop())
                current_node = current_node.prev
            else:
                current_node.addAfter(eat.pop())
                current_node = current_node.next
        #current_node.affiche(sens)

    current_node.affiche(sens)


def situation_finale(n, m, villes, actions):
    start_node = Node(villes[0])
    start_node.next = start_node
    start_node.prev = start_node
    current_node = start_node

    for i in range(1, n):
        current_node.addAfter(villes[i])
        current_node = current_node.next
        #start_node.affiche(1)

    simulate_jormungandr(start_node, actions)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    situation_finale(n, m, villes, actions)
