def rle_byt_img(data):
    newdata = []
    for i in range(0, len(data) - 2, 3):
      newdata.append((data[i]*256 + data[i+1])*256 + data[i+2])
    data = newdata
    encoding = []
    prev_char = -1
    count = 1
    if not data: return []
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding.append(count)
                encoding.append(prev_char)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding.append(count)
        encoding.append(prev_char)
        return encoding
