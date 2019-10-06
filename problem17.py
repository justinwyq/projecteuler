'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


def num_in_letters(x):
    # if len(str(x))>=2 and str(x)[-2]=='1':
    #     if x == 11:
    #         return('eleven')
    #     if x == 12:
    #         return('twelve')
    #     if x == 13:
    #         return('thirteen')
    #     if x == 14:
    #         return('fourteen')
    #     if x == 15:
    #         return('fifteen')
    #     if x == 16:
    #         return('sixteen')
    #     if x == 17:
    #         return('seventeen')
    #     if x == 18:
    #         return('eighteen')
    #     if x == 19:
    #         return('nineteen')
    dict_one = {1:'one' , 2:'two', 3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine', 0:''}
    dict_tens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen', 2:'twenty', 3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:'' }
    if len(str(x)) == 1:
        return dict_one[x]
    if len(str(x)) == 2:
        if str(x)[0] == '1':
            return dict_tens[x]
        else:
            return dict_tens[int(str(x)[0])] + dict_one[int(str(x)[1])]
    if len(str(x)) == 3:
        if str(x)[1:] == '00':
            return dict_one[int(str(x)[0])] + 'hundred'
        if str(x)[1] == '1':
            return dict_one[int(str(x)[0])] + 'hundredand' + dict_tens[int(str(x)[1:])]
        else:
            return dict_one[int(str(x)[0])] + 'hundredand' + dict_tens[int(str(x)[1])] + dict_one[int(str(x)[2])]
    if len(str(x)) == 4:
        return 'onethousand'

def countletters(x):
    return(len(x))


sumnumchars = 0

# print(countletters(num_in_letters(342)))

for x in range(1,1001):
    sumnumchars += countletters(num_in_letters(x))

    print(num_in_letters(x))
    print(countletters(num_in_letters(x)))

print(sumnumchars)
