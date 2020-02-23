class CurrentListItem:
    def __init__(self, number: int, text: str):
        self.number = number
        self.text = text

    def __str__(self):
        return f"{self.number+1}. {self.text}"


class CurrentList:
    def __init__(self, name: str):
        self.id = 1
        self.name = name
        self.items = list()

    def add_item(self, text: str):
        self.items.append(CurrentListItem(len(self.items), text))

    def remove_item(self, number: int):
        item = self.items[number-1]
        for i in self.items[number:]:
            i.number -= 1
        self.items.remove(item)

    def __str__(self):
        return "\n".join(map(lambda i: str(i), self.items))


default_list = CurrentList("default")
default_list.add_item("abc")
default_list.add_item("efg")
default_list.add_item("hig")
