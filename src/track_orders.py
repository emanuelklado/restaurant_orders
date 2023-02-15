from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dishes_result = [
            person[1] for person in self.orders if person[0] == customer
        ]
        most_requested_dish = Counter(dishes_result)
        return most_requested_dish.most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        never_ordered_dish = {
            item[1] for item in self.orders if item[0] == customer
        }
        all_dishes = {item[1] for item in self.orders}
        return all_dishes.difference(never_ordered_dish)

    def get_days_never_visited_per_customer(self, customer):
        days = {item[2] for item in self.orders if item[0] == customer}
        all_days = {item[2] for item in self.orders}
        return all_days.difference(days)
