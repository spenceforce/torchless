"""
Constant: a fixed numeric value whose gradient is always zero.
"""


class Constant:
    """A fixed numeric value.

    Attributes:
      data: The numeric value held by this constant.
    """

    def __init__(self, data):
        """
        Args:
          data: The numeric value to store.
        """
        self._data = data

    @property
    def data(self):
        """The numeric value."""
        return self._data

    def compute_grad(self):
        """
        Compute the gradient of this constant. Since a constant does not change, its gradient is
        always zero.

        Returns:
          0
        """
        return 0
