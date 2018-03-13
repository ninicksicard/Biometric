import ast
import time

class DataHolder:

    def __init__(self, max_history_length=50):
        self.history_saved = 1
        self.raw_data_stack = {}

        self.data_history = []

        self.an_history = []

        self.max_history_length = max_history_length

    def update_data(self, key, value):

        self.raw_data_stack.update({key: value})

        self.history_saved = 0

    def save_history(self):

        if self.history_saved == 0:

            self.data_history.append(str(self.raw_data_stack))

            self.history_saved = 1

        if len(self.data_history) > self.max_history_length:

            self.data_history.pop(0)

    def get_an_history(self, key, size, source="default"):

        self.an_history = []
        if source is "default":

            source = self.data_history

        timed = time.clock()
        while size:
            size -= 1

            if len(source) >= size+1:

                self.an_history.append(ast.literal_eval(source[size])[key])

            else: return self.an_history


            # except IndexError:
            #     print("indexerror")
            #     size = 0
            #
            # except KeyError:
            #     print("keyerror")
            #     size = 0
            #
            # except ValueError:
            #     print("VALUE ERROR IN BIODATACAPTURE LINE 48")
            #     print("VALUE ERROR IN BIODATACAPTURE LINE 48")
            #     print("VALUE ERROR IN BIODATACAPTURE LINE 48")
            #     print("VALUE ERROR IN BIODATACAPTURE LINE 48")
            #     print("VALUE ERROR IN BIODATACAPTURE LINE 48")
        # print("get an_history", (time.clock() - timed)*1000)
        return self.an_history
