"""
Base value type for the Torchless autograd engine.
"""


class Value:
    """Wraps a scalar and tracks its gradient.

    Attributes:
        data: The underlying scalar data.
    """

    def __init__(self, data):
        """Wrap a scalar as a Value.

        Args:
            data: The numeric value to store (e.g. a float or int).
        """
        self.data = data

    def compute_grad(self):
        """Return the gradient of this value.

        The gradient of a constant is 0.

        Returns:
            0
        """
        return 0
