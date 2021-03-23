# 1.使用方法修改字符串的大小写
# title() 首字母大写，空格之后的字母
str = 'hello world'
print(str.title())

# 全部字母大写
str = 'hello world'
print(str.upper())

# 全部字母小写
str = 'hello world'
print(str.lower())

# 2.字符串拼接
first_name = "he"
last_name = "runtian"
full_name = first_name+" "+last_name
print(full_name)
message = "Hello,"+full_name.title()+"!"
print(message)

# 3.使用制表符或换行符制造空白(\t:制表符 \n：换行符)
print("Python")
print("\tPython")
print("\nPython")
print("123")
print("提交演示")
print("提交演示2222")
