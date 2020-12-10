from classes.Logger import Logger

ITEM_QUANTITY = 5


class JobPouch(object):
    def __init__(self, pouch=None):
        if pouch is None:
            pouch = {}
        self.size = pouch.get('size', 0)
        self.gold = pouch.get('gold', 0)
        self.items = pouch.get('items', {})
        self.logger = Logger()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return self.total_items_count() == self.get_items_count()

    def get_items_count(self):
        total_count = 0
        for item in self.items:
            if item:
                total_count += item.get('quantity', 0)

        return total_count

    def total_items_count(self) -> int:
        return ITEM_QUANTITY * self.size
