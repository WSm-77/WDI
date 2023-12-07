def get_all_number_divs(number):
    tabOfDivs = []
    if number % 2 == 0:
        tabOfDivs.append(2)
        while number % 2 == 0:
            number //= 2
        #end while
    #end if
    div = 3
    while number > 1:
        if number % div == 0:
            tabOfDivs.append(div)
            while number % div == 0:
                number //= div
            #end while
        #end if
        div += 2
    #end while
    return tabOfDivs


def sum_of_products(number):
    divs = get_all_number_divs(number)
    N = len(divs)

    if N == 0:
        return 0
    #end if

    usedDivs = []

    def calc_sum_of_products(divs, used, index = 0, product = 1):
        nonlocal usedDivs
        if index == len(divs):
            if product > 1:
                usedDivs.append(used.rstrip('*'))
                return product
            else:
                return 0
        
        return calc_sum_of_products(divs, used + str(divs[index]) + '*', index + 1, product * divs[index]) + calc_sum_of_products(divs, used, index + 1, product)
    #end def
    
    reslut = calc_sum_of_products(divs, '')
    print(*usedDivs, sep=' + ')

    return reslut

if __name__ == "__main__":
    print(sum_of_products(60))
    print(sum_of_products(70))
