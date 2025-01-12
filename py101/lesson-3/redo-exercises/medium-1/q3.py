# Alyssa was asked to write an implementation of a rolling buffer.
# You can add and remove elements from a rolling buffer. However,
# once the buffer becomes full, any new elements will displace the
# oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to
# the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# SOLUTION
# the main differnce is the first implementation uses .append() which is a mutatin method
# this means that we are mutating the original list each time we addd an element
# we later are mutating the list again when we use pop once the max size is reached
# The second solutuon uses concatenation, which creates a new list with each addition
# this means that by the time we reach max size, we are mutating the last created list whioch contains the second
# to logest size, and the original list that was passed remains intact.