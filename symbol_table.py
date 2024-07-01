class SymbolTable:

  def __init__(self):
    self.symbols = {}  # Dictionary to store symbol table entries

  def add_symbol(self, symbol, symbol_type):
    """
    Adds a symbol to the symbol table.

    Args:
        symbol: The name of the symbol (string).
        symbol_type: The type of the symbol (e.g., "label", "variable").
    """
    if symbol in self.symbols:
      raise ValueError(f"Symbol '{symbol}' already defined in the symbol table.")
    self.symbols[symbol] = (None, symbol_type)  # Address initially None

# Example usage (assuming you have a function to identify labels)
symbol_table = SymbolTable()
for line in assembly_code:
  if is_label(line):
    symbol_name = extract_symbol_name(line)
    symbol_table.add_symbol(symbol_name, "label")