class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.data = self.gen(dictionary)
        
    def gen(self, dictionary):
        dic = {}
        for s in dictionary:
            abb = s[0]+str(len(s)-2)+s[-1]
            if abb in dic:
                dic[abb] = dic[abb].append(s)
            else:
                dic[abb] = [s]
        return dic
        

    def isUnique(self, s):
        abb = s[0]+str(len(s)-2)+s[-1]
        return abb not in self.data

dicti= [ "deer", "door", "cake", "card" ]

x = ValidWordAbbr(dicti)

print(x.isUnique("dear"))
print(x.isUnique("cart"))
print(x.isUnique("cane"))
print(x.isUnique("make"))
