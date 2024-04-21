"""
Alyssa was asked to write an implementation of a rolling buffer.
You can add and remove elements from a rolling buffer.
However, once the buffer becomes full, any new elements will displace
the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer (see below)

Is there a difference between these implementations,
other than the way she is adding an element to the buffer?

"""
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

# the difference is that .append() function mutates the caller. This means, we are passing the arugment by referene
# and thus altering the original object.

# the second option on the other hand, uses concatenation which does not mutate the original object
# but rather returns a new string