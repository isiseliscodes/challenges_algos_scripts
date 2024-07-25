class Cell:  # Base cell class
    def __init__(self, value=None):
        self.value = value

class StringCell(Cell):  # For storing strings
    pass

class NumberCell(Cell):  # For storing numbers
    pass

class Sheet:
    def __init__(self, rows=11, cols=12):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def SetCell(self, cell_id, value):
        col = ord(cell_id[0].upper()) - ord('A')  
        row = int(cell_id[1:]) - 1
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if isinstance(value, (int, float)):
                self.cells[row][col] = NumberCell(value)
            else:
                self.cells[row][col] = StringCell(value)
        else:
            print("Invalid cell ID")

    def Command(self, command):
        if "=" in command:
            cell_id, value = command.split("=")
            self.SetCell(cell_id.strip(), int(value.strip()))

    def GetCell(self, cell_id):
        col = ord(cell_id[0].upper()) - ord('A')  
        row = int(cell_id[1:]) - 1
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col].value
        else:
            return None

    def DisplaySheet(self):
        for row in self.cells:
            for cell in row:
                print(cell.value if cell.value is not None else "", end="\t")
            print()

# Example usage:
sheet = Sheet()
sheet.SetCell("A1", "Hello")
sheet.SetCell("B2", 123)
sheet.Command("C3 = 456")

print(sheet.GetCell("A1"))  # Output: Hello
sheet.DisplaySheet()