def password_checker(str1, n):
    if n < 4:
        return 0
    if str1[0].isdigit():
        return 0
    
    num_count = 0
    cap_count = 0
    for char in str1:
        if char.isdigit():
            num_count += 1
        if char.isupper():
            cap_count += 1
        if char == " " or char == "/":
            return 0
    
    if num_count >= 1 and cap_count >= 1:
        return 1
    else:
        return 0


str1 = "Abjhbjhbhbjh"
check = password_checker(str1, len(str1))
print(check)