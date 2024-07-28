"""
given a list of strings, return a new list in which every vowel in a string is
in uppercase and the list is sorted in ascending order by number of uppercase
letters

given ["abcde", "fghij", "klmnop", "qrstuv", "wxyz", "WXYZ"]
expect ['wxyz', 'fghIj', 'klmnOp', 'qrstUv', 'AbcdE', 'WXYZ']

I: list
O: list

Rules:
- new list
- uppercase vowels
- list is in ascending order by the number of uppercase letters
- Implicit: there are already consonants that are capitalized, will matter for sorting

** Sorting happens on ALL uppercase letters **

DS:
- lists
- strings

Algo:
- iterate over the input list --> ["abcde", "fghij", "klmnop", "qrstuv", "wxyz", "WXYZ"]
    - with each run --> "abcde"
        - modify element to have uppercase vowels --> "AbcdE"

- sort based on uppercase letters


"""

def vowel_ct(seq):
    vowel_count = 0

    for ch in seq:
        if ch.isupper():
            vowel_count += 1

    return vowel_count

def process_strings(iterable):
    for idx, text in enumerate(iterable):
        iterable[idx] = ''.join([ch.upper() if ch in 'aeiouAEIOU' else ch for ch in text ])

    new_order = sorted(iterable, key=vowel_ct)

    return new_order



# Test Case 1: Basic Example
input_1 = ["abcde", "fghij", "klmnop", "qrstuv", "wxyz", "WXYZ"]
expected_output_1 = ['wxyz', 'fghIj', 'klmnOp', 'qrstUv', 'AbcdE', 'WXYZ']
print(process_strings(input_1))# == expected_output_1)

# # Test Case 2: All Lowercase Letters
# input_2 = ["hello", "world", "python", "programming"]
# expected_output_2 = ['wOrld', 'hEllO', 'pythOn', 'prOgrAmmIng']
# print(process_strings(input_2) == expected_output_2)

# # Test Case 3: Mixed Case Letters
# input_3 = ["HELLO", "world", "PyThOn", "ProGrAmMiNg"]
# expected_output_3 = ['wOrld', 'PyThOn', 'PrOGrAmMiNg', 'HELLO']
# print(process_strings(input_3) == expected_output_3)

# # Test Case 4: No Vowels
# input_4 = ["bcdfg", "hjklm", "npqrst", "vwxyz"]
# expected_output_4 = ['bcdfg', 'hjklm', 'npqrst', 'vwxyz']
# print(process_strings(input_4) == expected_output_4)

# # Test Case 5: Single Character Strings
# input_5 = ["a", "b", "c", "A", "E", "I", "O", "U"]
# expected_output_5 = ['b', 'c', 'a', 'A', 'E', 'I', 'O', 'U']
# print(process_strings(input_5) == expected_output_5)

# # Test Case 6: Strings with Punctuation
# input_6 = ["hello!", "world?", "this.is", "a,test"]
# expected_output_6 = ['wOrld?', 'thIs.Is', 'hEllO!', 'A,tEst']
# print(process_strings(input_6) == expected_output_6)

# # Test Case 7: Empty Strings
# input_7 = ["", "a", "E", "xyz"]
# expected_output_7 = ['', 'xyz', 'a', 'E']
# print(process_strings(input_7) == expected_output_7)

# # Test Case 8: Identical Strings
# input_8 = ["abc", "abc", "abc"]
# expected_output_8 = ['Abc', 'Abc', 'Abc']
# print(process_strings(input_8) == expected_output_8)