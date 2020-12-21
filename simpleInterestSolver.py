def simple_interest(**kwargs):
    key_list = list(kwargs.keys())
    if len(list(kwargs())) > 3 or len(list(kwargs())) < 3:
        return Exception("Three parameters are needed")
    print(key_list)
    if 'I' not in key_list:
        I = (kwargs['P']*kwargs['T']*kwargs['R']) / 100
        return f"The simple interest is {I}"
    elif 'P' not in key_list:
        P = (kwargs['I'] * 100) / ((kwargs['R'])*(kwargs['T']))
        return f"The Principal is {P}"
    elif 'R' not in key_list:
        R = ((kwargs['I'] * 100) / (kwargs['P']*kwargs['T']))
        return f"The Rate is {R}"
    else:
        T = ((kwargs['I'] * 100) / (kwargs['R']*kwargs['P']))
        return f"The Time is {T}"
