class Solution(object):
    def addStrings(self, num1, num2):
        char_to_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        myDict1 = {i: [] for i in range(10)}
        myDict2 = {i: [] for i in range(10)}
        subtotal1 = 0
        subtotal2 = 0

        for i in range(len(num1)):
            myDict1[char_to_num[num1[i]]].append(i)

        for i in range(len(num2)):
            myDict2[char_to_num[num2[i]]].append(i)      

        for key in list(myDict1.keys()):
            if len(myDict1[key]) == 0:
                myDict1.pop(key)

        for key in list(myDict2.keys()):
            if len(myDict2[key]) == 0:
                myDict2.pop(key)
        
        for key in myDict1:
            for value in myDict1[key]:
                subtotal1 += key * pow(10, len(num1) - 1 - value)
        
        for key in myDict2:
            for value in myDict2[key]:
                subtotal2 += key * pow(10, len(num2) - 1 - value)

        return str(subtotal1 + subtotal2)



         