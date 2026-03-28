"""Fixed numeric value whose gradient is always zero."""


class Constant:
    """A fixed numeric value whose gradient is always zero."""

    def __init__(self, data):
        """Initializes the constant with a fixed numeric value.

        Args:
          data: The numeric value to store.
        """
        self._data = data

    @property
    def data(self):
        """The numeric value."""
        return self._data

    def compute_grad(self):
        """Computes the gradient of this constant.

        Since a constant does not change, its gradient is always zero.

        Returns:
          Always 0.
        """
        return 0
