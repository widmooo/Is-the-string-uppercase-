def is_uppercase(inp):
    banned = 'abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    banned_list = list(banned)
    x = list(inp)    
    print(x)
    for i in inp:
        if i in banned_list:
            return False
        else:
            return True
            
is_uppercase("hello I AM DONALD")  # OK
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") # NOT
is_uppercase("p(5eB`R"")  # OK
is_uppercase("1^`#_DviR5o>|_tL8$JC/+3V]! )h9n4Y") # NOT
is_uppercase("~^GP_JXbZq_+SjK:/rF;o!] {B"D0tH5hMf,1)%mus}(d")  # OK
is_uppercase("yoplg5v7D|)_e0V>kE:dGB3^9f? .&6}mTC\8SJt#P,Xbu!")  # OK
is_uppercase("T)k\_S^~m{_M6FhA[UPQs}g/H;Zv)B,9VRE"dtWq5&+xcKJ|7")  # NOT
