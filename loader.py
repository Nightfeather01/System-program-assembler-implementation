import sys

def byteToBinary(text):
    asciiBinaryMap = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
                      '4': "0100", '5': "0101", '6': "0110", '7': "0111",
                      '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
                      'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}

    result = "".join([asciiBinaryMap[i] for i in text])
    return result

def outputModified(text, endlines):
    endlineIndex = 0
    for i in range(len(text)):
        print(text[i], end="")
        if endlineIndex < len(endlines) and i == endlines[endlineIndex] - 1:
            print()
            endlineIndex += 1

    temp = ""
    endlineIndex = 0
    print("binary form: ", end="")
    for i in range(len(text)):
        temp += text[i]
        if endlineIndex < len(endlines) and i == endlines[endlineIndex] - 1:
            print(byteToBinary(temp))
            print()
            temp = ""
            endlineIndex += 1

def modification(text, modificationPos, address):
    print(f"here's the original text: {text}")
    print(f"here's the address(hex): {address}")
    
    text_list = list(text)
    pos_str = text[modificationPos * 2 + 1: modificationPos * 2 + 6]
    print(f"where to modify in text: {pos_str}")
    
    pos = int(pos_str, 16)
    print(f"where to modify in text(dec): {pos}")
    
    startingAddress = int(address, 16)
    print(f"starting address: {startingAddress}")
    
    pos += startingAddress
    modificationResult = hex(pos)[2:].upper()
    
    print(f"result: {modificationResult}")
    
    for j in range(5):
        text_list[modificationPos * 2 + 1 + j] = modificationResult[j]

    return "".join(text_list)

def main():
    text = ""
    textStartingAddress = []
    modificationPoslist = []
    endlines = []
    texts = []
    previousEndline = -1
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'T':
                length = int(line[1:7], 16)
                textStartingAddress.append(length)
                text = line[9:].strip()  # 去掉換行符
                texts.append(text)
                endlinePlace = int(line[7:9], 16)
                if previousEndline == -1:
                    endlines.append(endlinePlace * 2)
                else:
                    endlines.append(endlinePlace * 2 + endlines[previousEndline])
                previousEndline += 1
            elif line[0] == 'M':
                length = int(line[1:7], 16)
                modificationPoslist.append(length)

        startingAddress = hex(id(text))[-5:].upper()
        for i in range(len(modificationPoslist)):
            for j in range(len(textStartingAddress)):
                index = -1
                if modificationPoslist[i] < textStartingAddress[j]:
                    if j != 0:
                        index = j - 1
                    else:
                        index = 0
                    break
            if index == -1:
                index = len(textStartingAddress) - 1
            modificationPoslist[i] -= textStartingAddress[index]
            texts[index] = modification(texts[index], modificationPoslist[i], startingAddress)

        text = "".join(texts)
        outputModified(text, endlines)

if __name__ == "__main__":
    main()