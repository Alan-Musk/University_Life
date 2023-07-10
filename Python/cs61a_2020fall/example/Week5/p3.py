def mysum(L):
    if L == []:
        return 0
    return L[0]+mysum(L[1:])

def classsum(n):
    if n==0:
        return 0
    return n+classsum(n-1)

def reverse_a_word(s):
    if s=="":
        return ""
    return reverse_a_word(s[1:])+s[0]

print(reverse_a_word("alan"))