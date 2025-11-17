tuplee = ("apple", "hi", "banana", "a", "hello world")

string_list = list(tuplee)
string_list.sort(key=len, reverse=True)

result_tuple = tuple(string_list)

print(result_tuple)