# Typecasting - converting a variable from one data type to another
#int() - converts to integer (truncates floats)
#float() - converts to float
#str() - converts to string
#bool() - converts to boolean (0, empty, None = False; everything else = True)
#list() - converts to list
#tuple() - converts to tuple
#set() - converts to set (removes duplicates)

name = 'Patricia Zan'
age = 25
float_exemple = 2.5
is_online = False

string_decimal = "42"
string_float = "3.14"

#print(type(name))

float_exemple = int(float_exemple)
print(float_exemple)

age = float(age)
print(age)


# String to Integer
typecast_string_decimal = int(string_decimal)
print(typecast_string_decimal)

# String to Float
typecast_string_float = float(string_float)
print(typecast_string_float)

# String to Boolean
bool_value = bool(name)
print(bool_value)  # Output: True if it's only "" it will be false

# Integer to String
typecast_age_int = str(age)
print(typecast_age_int)

# Integer to Float
typecast_age_float = float(age)
print(typecast_age_float)

# Integer to Boolean
typecast_age_bool = bool(age)
print(typecast_age_bool)

# Float to Integer
typecast_float_exemple = int(float_exemple)
print(typecast_float_exemple)

# Float to String
typecast_float_exemple_str = str(float_exemple)
print(typecast_float_exemple_str)

# Float to Boolean
decimal = 0.0
bool_value = bool(decimal)
print(bool_value)  # Output: False (0.0 is falsy)

# Boolean to Integer
bool_val = True
int_num = int(bool_val)
print(int_num)  # Output: 1

# Boolean to String
bool_val = False
str_val = str(bool_val)
print(str_val)  # Output: "False"

# List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Tuple to List
my_tuple = (4, 5, 6)
my_list = list(my_tuple)
print(my_list)  # Output: [4, 5, 6]

# List to Set
my_list = [1, 2, 2, 3, 3]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3} (removes duplicates)

# String to List
text = "hello"
char_list = list(text)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']