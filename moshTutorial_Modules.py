# Abstraction can be achieved by importing thing with modules
# Method one imports everything on that page
import module_file
# # Method two imports specific things
# from module_file import weight_converter
from module_file import find_max, weight_converter

module_file.emoji_convertor()

weight_converter()

# If you are using an imported function, you must return it to use it in printing or something. It will not show if it only prints at the point of definition
array = [2, 4, 10, 99, 5, 70, 23]
print(find_max(array))
