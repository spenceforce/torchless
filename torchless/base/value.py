#| filename: torchless/base/value.py
class Value:

    def __init__(self, data):
        self.data = data

    def compute_grad(self):
        return 1
