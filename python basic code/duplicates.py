vegetables = ['Carrot','Beetroot','Chilli','Carrot']
duplicate = []
for vegetable in vegetables:
    if vegetable not in duplicate:
        duplicate.append(vegetable)
print(duplicate)