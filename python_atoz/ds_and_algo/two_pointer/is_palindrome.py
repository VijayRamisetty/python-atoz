def is_palindrome(s):
    s_len = len(s)
    i = 0
    j = s_len - 1
    while i <= j:
        print(s[i], s[j])
        while not s[i].isalpha():
            i += 1
        while not s[j].isalpha():
            j -= 1
        if s[i].lower() != s[j].lower():
            print(s[i], s[j])
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))
