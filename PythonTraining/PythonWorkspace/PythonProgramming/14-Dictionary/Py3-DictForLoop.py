colors = {'r' : 'red', 'b' : 'blue', 'g' : 'green', 'y' : 'yellow'}

#display only keys
for color in colors:
    print(color)

#pass keys to dictionary and display its values
for k in colors:
    print(colors[k])

#items() method returns key and values both in k,v
for k,v in colors.items():
    print('Key = {}, Value = {}'.format(k, v))