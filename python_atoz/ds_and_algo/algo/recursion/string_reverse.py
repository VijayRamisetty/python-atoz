def reverse(s):
    if s == '':
        return ''
    else:
        return reverse(s[1:]) + s[0]


if __name__ == '__main__':
    user_string = "This is Vijay"
    print(reverse(user_string))
