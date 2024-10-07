nap = str(input("Jó napod van?"))
nap_lowercase = nap.lower()
if nap_lowercase == "igen":
    print("Az jó!")
elif nap_lowercase == "nem":
    print("Az nem jó.")
else:
    print("Sajnos nem értem a válaszodat!")
print("A program vége.")