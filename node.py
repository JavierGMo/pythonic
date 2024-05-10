class Node:
    value: any
    nextNode: "Node" = None
    def __init__(self, value=None, nextNode: "Node" = None) -> None:
        self.value = value
        self.nextNode = nextNode
