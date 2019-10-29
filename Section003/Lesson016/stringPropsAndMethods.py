name = "Sam"
print("name = {0}".format(name))
newname = "P" + name[1:]
print("newname = {0}".format(newname))

letter = "z"
snore = letter * 10
print("snore = {0}".format(snore))

x = "Hello World"
xup = x.upper()
print("x = {0} xup = {1}".format(x, xup))
xlow = x.lower()
print("x = {0} xlow = {1}".format(x, xlow))
xpieces = x.split()
i = 0
for xp in xpieces: 
    print("xpieces {0} = {1}".format(i, xp))
    i = i + 1
