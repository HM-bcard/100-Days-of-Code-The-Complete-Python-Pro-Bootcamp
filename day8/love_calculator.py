def calculate_love_score(name1,name2):
    names = name1 + name2 #concat
    lower_names = names.lower()

    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')
    e = lower_names.count('e')
    first_digit = t + r + u + e
    
    
    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')
    second_digit = l + o + v + e
        
    love_score = int(str(first_digit) + str(second_digit))
    print(love_score)
