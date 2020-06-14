#OUTPUT

#*
#**
#***
#****
#*****

def incr_star_patt(n):

    my_list = []
    for i in range(1, n+1):
        my_list.append("*"*i)
    print("\n".join(my_list))


if __name__ == '__main__':
    incr_star_patt(6)



