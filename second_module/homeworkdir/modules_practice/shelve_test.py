import shelve
# 写文件
f = shelve.open("shelve_file")
names = {"k1":"v1","k2":"v2"}
list01 = ['a','b','c','d']

f["names"] = names
f["list01"] = list01
f.close()

#读取文件
f = shelve.open("shelve_file")

print(list(f.keys()),'up key back value',list(f.values()))
print(f['names'])
#删除
del f['names']
#修改，假如key对应的values是 列表或者字典，那么列表或者字典里面的值是不可以单独修改的。只有一起修改才可以。
f['names'] = ['x','y','z']

print(f['names'])
f.close()
