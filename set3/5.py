##################
# first solution #
##################

def tenthMaxValue():
    values = set()
    while True:
        number = int(input("enter number: "))
        if 0 != number:
            values.add(number)
        else:
            break
        #end if
    #end while
    values = sorted(values)
    assert(len(values) > 9)

    return values[9]

###################
# second solution #
###################

def tenthMaxValueVersion2():
    values = []
    while True:
        number = int(input("enter number: "))
        if 0 == number:
            break
        #end if
        
        if values == []:
            values.append(number)
        else:
            for i in range(len(values)):
                if number == values[i]:
                    break
                #end if
                if number < values[i]:
                    values.insert(i, number)
                    break
                #end if
            else:
                values.append(number)
            #end for
        #end if
    #end while
    print(values)
    assert(len(values) > 9)

    return values[9]


if __name__ == "__main__":
    # print(tenthMaxValue())
    print(tenthMaxValueVersion2())
