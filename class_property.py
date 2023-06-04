class Class_Property:
    """Descriptor for new class properties."""

    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        """Get property value that is stored in the instance dictionary."""
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """Set property value in the instance dictionary."""
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        """Set the property name, when set method is used."""
        self.name = name


