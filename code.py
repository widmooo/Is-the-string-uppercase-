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
            
is_uppercase("hello I AM DONALD")
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")
is_uppercase("p(5eB`R"")
is_uppercase("1^`#_DviR5o>|_tL8$JC/+3V]! )h9n4Y")
is_uppercase("~^GP_JXbZq_+SjK:/rF;o!] {B"D0tH5hMf,1)%mus}(d")
is_uppercase(yoplg5v7D|)_e0V>kE:dGB3^9f? .&6}mTC\8SJt#P,Xbu!)
is_uppercase(T)k\_S^~m{_M6FhA[UPQs}g/H;Zv)B,9VRE"dtWq5&+xcKJ|7)
