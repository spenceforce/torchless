"""Mutable scalar value node for use in a computational graph."""


class Value:
    """A scalar value that participates in automatic differentiation.

    Attributes:
      data: The numeric scalar held by this node.
    """

    def __init__(self, data):
        """Initializes the Value with a scalar.

        Args:
          data: The numeric scalar to store.
        """
        self.data = data

    def compute_grad(self):
        """Returns the local gradient of this node with respect to itself.

        Returns:
          Always 1, because d(x)/d(x) = 1.
        """
        return 1
