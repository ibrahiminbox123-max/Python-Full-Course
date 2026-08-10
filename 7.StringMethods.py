# =========================================================
# 1. upper()
# String ko CAPITAL LETTERS mein convert karta hai
# =========================================================

name = "ibrahim"

print(name.upper())

# OUTPUT:
# IBRAHIM


# =========================================================
# 2. lower()
# String ko small letters mein convert karta hai
# =========================================================

name = "IBRAHIM"

print(name.lower())

# OUTPUT:
# ibrahim


# =========================================================
# 3. capitalize()
# Sirf string ke first character ko capital karta hai
# =========================================================

name = "ibrahim"

print(name.capitalize())

# OUTPUT:
# Ibrahim


# =========================================================
# 4. title()
# Har word ka first letter capital karta hai
# =========================================================

text = "python full course"

print(text.title())

# OUTPUT:
# Python Full Course


# =========================================================
# 5. swapcase()
# Capital ko small aur small ko capital karta hai
# =========================================================

text = "PyThOn"

print(text.swapcase())

# OUTPUT:
# pYtHoN


# =========================================================
# 6. strip()
# Start aur end ke extra spaces remove karta hai
# =========================================================

text = "   Hello World   "

print(text.strip())

# OUTPUT:
# Hello World


# =========================================================
# 7. lstrip()
# Sirf LEFT side ke spaces remove karta hai
# =========================================================

text = "   Hello"

print(text.lstrip())

# OUTPUT:
# Hello


# =========================================================
# 8. rstrip()
# Sirf RIGHT side ke spaces remove karta hai
# =========================================================

text = "Hello   "

print(text.rstrip())

# OUTPUT:
# Hello


# =========================================================
# 9. replace()
# String ke kisi part ko doosre text se replace karta hai
# =========================================================

text = "I like Java"

print(text.replace("Java", "Python"))

# OUTPUT:
# I like Python


# =========================================================
# 10. split()
# String ko pieces ki LIST mein divide karta hai
# Default mein spaces ke according split karta hai
# =========================================================

text = "I love Python"

print(text.split())

# OUTPUT:
# ['I', 'love', 'Python']


# =========================================================
# 11. join()
# Multiple strings ko ek string mein join karta hai
# =========================================================

words = ["I", "love", "Python"]

print(" ".join(words))

# OUTPUT:
# I love Python


# =========================================================
# 12. find()
# Kisi word/character ki position find karta hai
# Agar na mile to -1 deta hai
# =========================================================

text = "Hello Python"

print(text.find("Python"))

# OUTPUT:
# 6


# =========================================================
# 13. index()
# Kisi word/character ki position find karta hai
# Difference: agar na mile to error deta hai
# =========================================================

text = "Hello Python"

print(text.index("Python"))

# OUTPUT:
# 6


# =========================================================
# 14. count()
# Batata hai koi character/word kitni baar aaya hai
# =========================================================

text = "banana"

print(text.count("a"))

# OUTPUT:
# 3


# =========================================================
# 15. startswith()
# Check karta hai string kis text se START ho rahi hai
# Answer True ya False hota hai
# =========================================================

text = "Python Programming"

print(text.startswith("Python"))

# OUTPUT:
# True


# =========================================================
# 16. endswith()
# Check karta hai string kis text par END ho rahi hai
# =========================================================

text = "Python Programming"

print(text.endswith("Programming"))

# OUTPUT:
# True


# =========================================================
# 17. isalpha()
# Check karta hai ke string mein sirf letters hain ya nahi
# =========================================================

text = "Python"

print(text.isalpha())

# OUTPUT:
# True


# =========================================================
# 18. isdigit()
# Check karta hai ke string mein sirf digits hain ya nahi
# =========================================================

text = "12345"

print(text.isdigit())

# OUTPUT:
# True


# =========================================================
# 19. isalnum()
# Check karta hai ke string mein sirf letters aur numbers hain
# =========================================================

text = "Python123"

print(text.isalnum())

# OUTPUT:
# True


# =========================================================
# 20. isspace()
# Check karta hai ke string mein sirf spaces hain ya nahi
# =========================================================

text = "   "

print(text.isspace())

# OUTPUT:
# True


# =========================================================
# 21. islower()
# Check karta hai ke letters lowercase hain ya nahi
# =========================================================

text = "hello"

print(text.islower())

# OUTPUT:
# True


# =========================================================
# 22. isupper()
# Check karta hai ke letters uppercase hain ya nahi
# =========================================================

text = "HELLO"

print(text.isupper())

# OUTPUT:
# True


# =========================================================
# 23. istitle()
# Check karta hai ke string Title Case mein hai ya nahi
# =========================================================

text = "Hello World"

print(text.istitle())

# OUTPUT:
# True


# =========================================================
# 24. center()
# String ko given width ke center mein rakhta hai
# =========================================================

text = "Hi"

print(text.center(10, "-"))

# OUTPUT:
# ----Hi----
# (10 characters ki total width)


# =========================================================
# 25. ljust()
# String ko LEFT side par rakhta hai aur right side fill karta hai
# =========================================================

text = "Hi"

print(text.ljust(10, "-"))

# OUTPUT:
# Hi--------


# =========================================================
# 26. rjust()
# String ko RIGHT side par rakhta hai aur left side fill karta hai
# =========================================================

text = "Hi"

print(text.rjust(10, "-"))

# OUTPUT:
# --------Hi


# =========================================================
# 27. zfill()
# Number-like string ke LEFT side par zero lagata hai
# =========================================================

number = "25"

print(number.zfill(5))

# OUTPUT:
# 00025


# =========================================================
# 28. partition()
# String ko 3 parts mein divide karta hai:
# before, separator, after
# =========================================================

text = "I love Python"

print(text.partition("love"))

# OUTPUT:
# ('I ', 'love', ' Python')


# =========================================================
# 29. rpartition()
# partition() jaisa hai, lekin RIGHT side se separator search karta hai
# =========================================================

text = "hello-python-world"

print(text.rpartition("-"))

# OUTPUT:
# ('hello-python', '-', 'world')


# =========================================================
# 30. splitlines()
# Multiple lines ko list mein convert karta hai
# =========================================================

text = "Hello\nWorld\nPython"

print(text.splitlines())

# OUTPUT:
# ['Hello', 'World', 'Python']


# =========================================================
# 31. removeprefix()
# Agar string given prefix se start hoti hai to usko remove karta hai
# =========================================================

text = "Hello Python"

print(text.removeprefix("Hello "))

# OUTPUT:
# Python


# =========================================================
# 32. removesuffix()
# Agar string given suffix par end hoti hai to usko remove karta hai
# =========================================================

text = "Python.py"

print(text.removesuffix(".py"))

# OUTPUT:
# Python


# =========================================================
# 33. expandtabs()
# \t (tab) ko spaces mein expand karta hai
# =========================================================

text = "Hello\tWorld"

print(text.expandtabs(4))

# OUTPUT:
# Hello   World


# =========================================================
# 34. encode()
# String ko bytes mein encode karta hai
# Beginner level par abhi iski zyada zarurat nahi
# =========================================================

text = "Hello"

print(text.encode())

# OUTPUT:
# b'Hello'b 