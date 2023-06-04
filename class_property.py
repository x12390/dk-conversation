class Class_Property:
    """Descriptor for new class properties."""
    def __init__(self, value_type):
        self._type = value_type
    def __get__(self, instance, owner):
        """Get property value that is stored in the instance dictionary."""
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        """Set property value in the instance dictionary."""
        if self._type == "str":
            if type(value) is not str:
                raise ValueError(f"Property {self.name} allows string only.")
        elif self._type == "int":
            if type(value) is not int:
                raise ValueError(f"Property {self.name} allows integer only.")
        else:
            raise ValueError(f"Propery {self.name} does not allow type {type(value)}.")

        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        """Set the property name, when set method is used."""
        self.name = name


