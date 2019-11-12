class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.append(data)
    self._bubble_up(len(self) - 1)

  def delete(self):
    if len(self) > 2:
	    self.__swap(1, len(self) - 1)
	    max = self.heap.pop()
	    self.__bubbleDown(1)
    elif len(self.heap) == 2:
      max = self.heap.pop()
    else:
      max = False
    return max

  def get_max(self):
    return self.storage[0]
  
  def __swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = index//2
    if index <= 1:
      return
    elif self.heap[index] > self.heap[parent]:
      self.__swap(index, parent)
      self.__floatUp(parent)

  def _sift_down(self, index):
    left = index * 2
    right = index * 2 + 1
    largest = index
    if len(self.heap) > left and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
      largest = right
    if largest != index:
      self.__swap(index, largest)
      self.__bubbleDown(largest)
