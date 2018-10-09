import s1


s1.obj1._registry['k1'] = 123


import s2

print(s1.obj1._registry)

"""
<s1.AdminSite object at 0x0000027C54F88EF0>
<s1.AdminSite object at 0x0000027C54F88EF0>
"""

