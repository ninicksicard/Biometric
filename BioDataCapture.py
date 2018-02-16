class DataHolder:

    def __init__(self, max_history_length=10):

        self.raw_data_stack = {}

        self.data_history = []

        self.an_history = []

        self.max_history_length = max_history_length

    def update_data(self, key, value):

        self.raw_data_stack.update({key: value})

    def save_history(self):

        self.data_history.append(self.raw_data_stack)

        if len(self.data_history) > self.max_history_length:

            self.data_history.pop(0)

    def get_an_history(self, key, size, source="default"):
        self.an_history = []
        if source is "default":

            source = self.data_history

        while size:

            size -= 1
            try:
                self.an_history.append(source[size][key])

            except IndexError:
                size = 0
            except KeyError:
                size = 0

        return self.an_history
