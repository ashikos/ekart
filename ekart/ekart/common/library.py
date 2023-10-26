import enum 


class ChoiceAdapter(enum.IntEnum):

    @classmethod
    def choices(self):
        return ((item.value, item.name.replace("_", " ")) for item in self)
    
    @classmethod 
    def values(self):
        return [item.vale for item in self]