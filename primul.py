# orase = ["Barcelona", "Bucuresti", "Madrid", "Cluj", "Londra"]

# # def filtreaza_orase(oras:str):
# #     return oras.startswith("B")

# print(list(filter(lambda x: x.startswith("B") , orase)))


from functools import reduce

# lista =[2,3,4,5,6,7]

# print(reduce(lambda x,y: x+y, lista))
lista = [10,2,30,50,300,10]

print(list(filter(lambda x: x>5, lista)))
print(reduce(lambda x,y: x+y, lista))


# def siruri_mai_lungi_de_5(lista):
#     o_noua_lista = []
#     for i in lista:
#         if len(str(i)) > 5:
#             o_noua_lista.append(i)
#     return o_noua_lista

# print(siruri_mai_lungi_de_5([10, 2, 30, 50, 300_000, 10]))
