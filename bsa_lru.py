import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

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

    # Miss and Hit counters
    self.miss_counter = 0
    self.hit_counter = 0
    self.mem_access_count = 0
    
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

    self.hit_miss_table = ttk.Treeview(master, columns=("Value", "Set", "MemoryAccess", "HitCnt", "MissCnt", "HitRate", "MissRate", "AMAT", "TMAT"))
    self.hit_miss_table.heading("Value", text="Sequence")
    self.hit_miss_table.heading("Set", text="Set")
    self.hit_miss_table.heading("MemoryAccess", text="Memory Access")
    self.hit_miss_table.heading("HitCnt", text="Hit Count")
    self.hit_miss_table.heading("MissCnt", text="Miss Count")
    self.hit_miss_table.heading("HitRate", text="Hit Rate")
    self.hit_miss_table.heading("MissRate", text="Miss Rate")
    self.hit_miss_table.heading("AMAT", text="AMAT")
    self.hit_miss_table.heading("TMAT", text="TMAT")
    self.hit_miss_table.pack(fill="none")

    # Set hit_miss_table width
    for column in self.hit_miss_table["columns"]:
      self.hit_miss_table.column(column, stretch=False, width=100)

    # Set column options to fixed width
    for column in self.tree["columns"]:
      self.tree.column(column, stretch=False, minwidth=0, width=70)

    self.tree.pack(fill="both", expand=True)
    
    # Button to update the table
    self.update_button = tk.Button(master, text="Update Table", command=self.update_table_with_array)
    self.update_button.pack()

    self.choose_button = tk.Button(master, text="Choose a Sequence", command=self.show_alert)
    self.choose_button.pack()
    
    self.block_limit = 0
    self.selected_sequence = ""
    
    sequence_length = 64
    # Generate the sequential sequence
    sequential_sequence = [i for i in range(sequence_length)]
    # Repeat the sequence four times
    self.final_array = sequential_sequence * 4
    # Current index in the array
    self.current_index = 0

    # Print initial table
    self.print_table()

    self.disable_button(self.update_button)

  def show_alert(self):
    # Create a new window for the alert
    alert_window = tk.Toplevel(self.master)
    alert_window.title("Alert")

    # Add a text view
    text_view_label = tk.Label(alert_window, text="How many blocks?")
    text_view_label.pack(padx=3, pady=(0, 5))
    text_view = tk.Text(alert_window, height=1, width=20)
    text_view.pack(padx=3, pady=5)

    # Add a label for the dropdown menu
    dropdown_label = tk.Label(alert_window, text="Select a sequence:")
    dropdown_label.pack(padx=10, pady=(0, 5))

    # Add a dropdown menu
    dropdown_var = tk.StringVar(alert_window)
    dropdown_var.set("Sequential sequence")  # Default option
    dropdown = ttk.Combobox(alert_window, textvariable=dropdown_var, values=["Sequential sequence", "Random sequence", "Mid-repeat blocks"])
    dropdown.pack(padx=10, pady=5)

    # Add an OK button
    ok_button = tk.Button(alert_window, text="OK", command=lambda: self.close_alert(alert_window, text_view, dropdown_var))
    ok_button.pack(pady=10)
  
  def close_alert(self, alert_window, text_view, dropdown_var):
    entered_text = text_view.get("1.0", "end-1c")
    converted_text = int(entered_text)
    selected_value = dropdown_var.get()

    self.block_limit = converted_text
    self.selected_sequence = selected_value
    print("Entered integer:", converted_text)
    print("Entered text:", entered_text)
    print("Selected Sequence: ", self.selected_sequence)

    alert_window.destroy()  # Close the alert window
    self.enable_button(self.update_button)
    self.reset_data()

  def update_table(self, set_num, new_value):
    for item in self.tree.get_children():
      self.tree.delete(item)

    # Update the value and counter
    set_data = self.sets[set_num]

    value_updated = False

    self.mem_access_count += 1

    for index, block in enumerate(set_data):

      print("Set Data: ", set_data)

      if block["value"] is None:
        print("Running here in if")

        self.check_if_value_exists(new_value, set_data)  

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

          self.check_if_value_exists(new_value, set_data)

          lowest_counter, lowest_counter_index = self.get_lowest_counter(self.sets[set_num])

          self.set_counters[set_num] += 1
          self.sets[set_num][lowest_counter_index]["value"] = new_value
          self.sets[set_num][lowest_counter_index]["counter"] = self.set_counters[set_num]
          
          value_updated = True

          print("Lowest counter is: ", lowest_counter)
          print("Lowest counter index: ", lowest_counter_index)

      print("Mem Access Count: ", self.mem_access_count)
      print("Limit: ", self.block_limit)

      if self.mem_access_count > self.block_limit:
        self.end_of_loop_alert()
        self.disable_button(self.update_button)
        break

      if value_updated:
        print("Value updated: ", value_updated)
        break

    # Print the updated table
    self.print_table()
    self.update_hit_miss_table(new_value, set_num)
    print("-------------------")

  def check_if_value_exists(self, value, set):
    # Check if the value exists
    value_exists = any(entry['value'] == value for entry in set)

    # Print the result
    if value_exists:
      self.hit_counter += 1
    else:
      self.miss_counter += 1

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
      age_text = f"Set {i} Age"
      values = [block["value"] for block in set_data]
      counters = [block["counter"] for block in set_data]
      self.tree.insert("", "end", text=set_text, values=values)
      self.tree.insert("", "end", text=age_text, values=counters)

    with open("table_result.txt", "w") as f:
      f.write("Set, Block1, Block2, Block3, Block4, Block5, Block6, Block7, Block8\n")
      for i, set_data in enumerate(self.sets):
        set_text = f"Set {i}"
        age_text = f"Set {i} Age"
        values = [block["value"] for block in set_data]
        counters = [block["counter"] for block in set_data]
        f.write(f"{set_text}: {values}\n")
        f.write(f"{age_text}: {counters}\n")

  def update_hit_miss_table(self, value, set_num):
    # Clear existing table data
    for item in self.hit_miss_table.get_children():
      self.hit_miss_table.delete(item)
    
    # Insert new data into the table
    if (self.mem_access_count > self.block_limit):
      self.mem_access_count -= 1

    hit_rate = self.hit_counter / self.mem_access_count
    miss_rate = self.miss_counter / self.mem_access_count
    block_size = 8
    cache_access = 1
    cache_line = 16
    memory_access = 10

    miss_penalty = cache_access + (block_size * memory_access) + cache_access
    amat = (hit_rate * cache_access) + (miss_rate * miss_penalty)
    tmat = (self.hit_counter * cache_line * cache_access) + self.miss_counter * (cache_access + (block_size * memory_access) + block_size)

    self.hit_miss_table.insert("", "end", text="", values=(value, set_num, self.mem_access_count, self.hit_counter, self.miss_counter, round(hit_rate, 2), round(miss_rate, 2), round(amat, 2), round(tmat, 2)))
    
  def update_table_with_array(self):
    # Get the current value from the array
    value = self.final_array[self.current_index]
    
    # Update the table with the new value
    mod_result = value % 4
    self.update_table(mod_result, value)
    
    # Move to the next index in the array
    self.current_index = (self.current_index + 1)

  def end_of_loop_alert(self):
    messagebox.showinfo("End of Sequence", "The sequence has ended.")

  def disable_button(self, button):
    button.config(state=tk.DISABLED)

  def enable_button(self, button):
    button.config(state="normal")

  def reset_data(self):
    for item in self.tree.get_children():
      self.tree.delete(item)

    for item in self.hit_miss_table.get_children():
      self.hit_miss_table.delete(item)

    self.miss_counter = 0
    self.hit_counter = 0
    self.mem_access_count = 0
    self.current_index = 0

    self.sets = [
      [{"value": None, "counter": None} for _ in range(8)]  # Each set contains 8 blocks
      for _ in range(4)  # There are 4 sets in total
    ]
    self.set_counters = [None, None, None, None, None, None, None, None]

    if self.selected_sequence == "Sequential sequence":
      sequence_length = 64
      # Generate the sequential sequence
      sequential_sequence = [i for i in range(sequence_length)]
      # Repeat the sequence four times
      self.final_array = sequential_sequence * 4
    elif self.selected_sequence == "Random sequence":
      random_sequence = [random.randint(0, 127) for _ in range(128)]
      self.final_array = random_sequence
    elif self.selected_sequence == "Mid-repeat blocks":
      mid_sequences = []
      for _ in range(4):  # Repeat the entire sequence 4 times
          # First sequence: 0, 1, 2, 3
          mid_sequences.extend(range(4))
          # Second sequence: 4, 5, ..., 31 (repeated 2 times)
          mid_sequences.extend(range(4, 32))
          mid_sequences.extend(range(4, 32))
          # Third sequence: 32, 33, ..., 63
          mid_sequences.extend(range(32, 64))
      self.final_array = mid_sequences

    self.print_table()

def main():
  root = tk.Tk()
  app = TableUpdater(root)
  root.mainloop()

if __name__ == "__main__":
  main()
