resultStr = ''
for row in range(7):
    for column in range(5):
        if(((column == 0 or column == 4) and row != 6) or (row == 6 and column > 0 and column < 4)):
            resultStr = resultStr + "*"
        else:
            resultStr = resultStr + " "
    resultStr = resultStr + "\n"
print(resultStr)