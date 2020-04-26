filename = input("请输入文件名称：")
split = input("编码分割符：")
file_response = []
file = []
with open(filename, "r") as f:
    file_response.append(f.read().split(split))
for i in file_response[0]:
    file.append(i)
file.remove("")
enc = []
for i in file:
    enc.append(chr(int(i)))
response = ''.join(enc)
print("解码字符", response)