class CustomerCounter:
  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    if self.count < 100:
      self.count += 1
      return self.count
    else:
      raise StopIteration

customer_counter = CustomerCounter()

for count in customer_counter:
  print(count)