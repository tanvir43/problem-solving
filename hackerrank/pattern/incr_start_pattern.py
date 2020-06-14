#OUTPUT

#*
#**
#***
#****
#*****

#SOULUTION

def incr_start_patt(v):
    my_list = []
    for i in range(1, v+1):
        my_list.append("*"*i)
    print("\n".join(my_list))

if __name__ == '__main__':
    incr_start_patt(6)
