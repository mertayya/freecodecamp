def arithmetic_arranger(myList, arg=False):

    firstList = []
    secondList = []
    thirdList = []
    fourthList = []

    if len(myList) > 5:
        return "Error: Too many problems."
    else:
        for each in myList:
            eachNum = each.split(" ")
            firstNum = eachNum[0]
            secondNum = eachNum[2]
            operator = eachNum[1]

            if firstNum.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif secondNum.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif operator == "/" and "*":
                return "Error: Operator must be '+' or '-'."
                quit()

            numWidth = 0

            if len(firstNum) + 2 >= len(secondNum) + 2:
                numWidth = len(firstNum) + 2
            elif len(firstNum) + 2 <= len(secondNum) + 2:
                numWidth = len(secondNum) + 2

            if numWidth > 6:
                return "Error: Numbers cannot be more than four digits."
                quit()

            spaceFirstList = []

            for eachSpace in range(numWidth - (len(firstNum) + 2)):
                spaceFirstList.append(" ")

            firstList.extend(["  "])
            firstList.extend(spaceFirstList)
            firstList.extend([firstNum, "    "])

            spaceSecondList = []

            for eachSpace in range(numWidth - (len(secondNum) + 2)):
                spaceSecondList.append(" ")

            secondList.extend([operator, " "])
            secondList.extend(spaceSecondList)
            secondList.extend([secondNum, "    "])

            for eachSpace in range(numWidth):
                thirdList.append("-")

            thirdList.extend(["    "])

            if arg == True:
                if operator == "+":
                    answer = int(firstNum) + int(secondNum)

                elif operator == "-":
                    answer = int(firstNum) - int(secondNum)

                spaceFourthList = []
                for eachSpace in range(numWidth - len(str(answer))):
                    spaceFourthList.append(" ")

                fourthList.extend(spaceFourthList)
                fourthList.extend([str(answer)])

            fourthList.extend(["    "])

        firstString = "".join(firstList).rstrip(" ")
        secondString = "".join(secondList).rstrip(" ")
        thirdString = "".join(thirdList).rstrip(" ")
        fourthString = "".join(fourthList).rstrip(" ")

    if arg == True:

        return_statement = firstString + "\n" + secondString + "\n" + thirdString + "\n" + fourthString
        return return_statement
    else:

        return_statement = firstString + "\n" + secondString + "\n" + thirdString
        return return_statement
