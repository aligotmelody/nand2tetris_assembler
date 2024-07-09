dic = {
    "dest": "",
    "cmp": "",
    "jmp": "",
    }


new = {"dest": "55", "cmp": "23", "jmp":"11"}

dic.update(new)
dest = dic["dest"]
print(dic)
print(dest)