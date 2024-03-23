import tkinter as tk
from tkinter import ttk

class TableUpdater:
  def __init__(self, master):
    self.master = master
    master.title("Table Updater")
    
    # Initialize sets and counters
    self.sets = [
      # Using nested list comprehension to create each set with default values
      [{"value": None, "counter": None} for _ in range(8)]  # Each set contains 8 blocks
      for _ in range(4)  # There are 4 sets in total
    ]
    self.set_counters = [None, None, None, None, None, None, None, None]
    
    # Create a Treeview widget
    self.tree = ttk.Treeview(master, columns=("Block1", "Block2", "Block3", "Block4", "Block5", "Block6", "Block7", "Block8"))
    self.tree.heading("#0", text="Set")
    self.tree.heading("Block1", text="Block 1")
    self.tree.heading("Block2", text="Block 2")
    self.tree.heading("Block3", text="Block 3")
    self.tree.heading("Block4", text="Block 4")
    self.tree.heading("Block5", text="Block 5")
    self.tree.heading("Block6", text="Block 6")
    self.tree.heading("Block7", text="Block 7")
    self.tree.heading("Block8", text="Block 8")
    self.tree.pack(fill="both", expand=True)

    # Set column options to wrap content
    for column in self.tree["columns"]:
      self.tree.column(column, stretch=False, minwidth=0, width=70)

    self.tree.pack(fill="both", expand=True)
    
    # Button to update the table
    self.update_button = tk.Button(master, text="Update Table", command=self.update_table_with_array)
    self.update_button.pack()
    
    # Sample array
    # Define the length of the sequence
    sequence_length = 64
    # Generate the sequential sequence
    sequential_sequence = [i for i in range(sequence_length)]
    # Repeat the sequence four times
    self.final_array = sequential_sequence * 4
    # Current index in the array
    self.current_index = 0

    # Print initial table
    self.print_table()
  
  def update_table(self, set_num, new_value):
    for item in self.tree.get_children():
      self.tree.delete(item)

    # Update the value and counter
    set_data = self.sets[set_num]

    value_updated = False

    for index, block in enumerate(set_data):

      print("Set Data: ", set_data)

      if block["value"] is None:
        print("Running here in if")
        block["value"] = new_value
        if block["counter"] is None and self.set_counters[set_num] is None:
          self.set_counters[set_num] = 0
          block["counter"] = self.set_counters[set_num]
        else:
          self.set_counters[set_num] += 1
          block["counter"] = self.set_counters[set_num]

        print("Set Data after: ", set_data)
        
        value_updated = True
      else:
        if self.is_block_full(self.sets[set_num]):
          print("Set Data in else: ", set_data)
          print("Block is full")

          lowest_counter, lowest_counter_index = self.get_lowest_counter(self.sets[set_num])

          self.set_counters[set_num] += 1
          self.sets[set_num][lowest_counter_index]["value"] = new_value
          self.sets[set_num][lowest_counter_index]["counter"] = self.set_counters[set_num]
          
          value_updated = True

          print("Lowest counter is: ", lowest_counter)
          print("Lowest counter index: ", lowest_counter_index)

      if value_updated:
        print("Value updated: ", value_updated)
        break
    
    # Print the updated table
    self.print_table()
    print("-------------------")

  def is_block_full(self, set):
    for block in set:
      if block["value"] is None:
        return False
    return True

  def get_lowest_counter(self, set_number):

    print("Block is: ", set_number)

    lowest_counter = float('inf')
    lowest_counter_block_index = None

    for block_index, block_info in enumerate(set_number):
      counter = block_info["counter"]

      if counter is not None and counter < lowest_counter:
        lowest_counter = counter
        lowest_counter_block_index = block_index

      print("Block is: ", block_info)
      print("Value is: ", block_info["value"])
      print("Counter is: ", counter)

    return lowest_counter, lowest_counter_block_index


  def print_table(self):
    for i, set_data in enumerate(self.sets):
      set_text = f"Set {i}"
      age_text = f"Age {i}"
      values = [block["value"] for block in set_data]
      counters = [block["counter"] for block in set_data]
      self.tree.insert("", "end", text=set_text, values=values)
      self.tree.insert("", "end", text=age_text, values=counters)

  def update_table_with_array(self):
    # Get the current value from the array
    value = self.final_array[self.current_index]
    
    # Update the table with the new value
    mod_result = value % 4
    self.update_table(mod_result, value)
    
    # Move to the next index in the array
    self.current_index = (self.current_index + 1) % len(self.final_array)

def main():
  root = tk.Tk()
  app = TableUpdater(root)
  root.mainloop()


if __name__ == "__main__":
  main()