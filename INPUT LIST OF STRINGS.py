w=["Raju","Ram","Anu"]
vowels="aeiouAEIOU"
result=(map(lambda x: sum(ch in vowels for ch in x), w))
print(list(result))