class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, integer=0):
        self._side=integer
        
    def get_side(self):
        """Return the side of the Cube"""
        return abs(self._side)  # it's your choice 

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side