from dataclasses import dataclass

@dataclass
class MultiDisplay:
    message : str = "string"
    count : int = 0
    

    def set_message(self, message):
        self.message = message
    

    
    def set_count(self, count):
        self.count = count

    

    def to_string(self):
        string = (f"Message: {self.message}, Count: {self.count}")
        return string

    
    def display(self):
        for i in range(self.count):
            print(self.message)


    
    def set_display(self, string, count):
        self.message = string
        self.count = count
        self.display()

    
    
    def get_message(self):
        return self.message


