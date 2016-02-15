import serpent
from ethereum import tester, utils, abi

serpent_code = open('Namecoin.se', 'r').read()

#Create public key
public_k1 = utils.privtoaddr(tester.k1)

#Generate state and add contract to block chain
s = tester.state()
print("Tester state created")
c = s.abi_contract(serpent_code)
print("Code added to block chain")

#Test contract
o = c.get("Bob")
print("The value stored with key \"Bob\" is " + str(o))
o = c.register("Bob", 10)
o = c.get("Bob")
print("The value stored with key \"Bob\" is " + str(o))



