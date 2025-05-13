# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    object_count = 0   #class variable

    def __init__(self):
        Counter.object_count += 1  # every object will be increased by 1

    @classmethod
    def dispaly_count(cls):
        print(f"There are {cls.object_count} objects created.")

obj_1 = Counter()

obj_2 = Counter()

obj_3 = Counter()

obj_1 = Counter()

obj_2 = Counter()

obj_3 = Counter()

Counter.dispaly_count()