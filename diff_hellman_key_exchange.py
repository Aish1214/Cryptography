# Enter the approved prime number and the primitive root g.
prime = int(input("Enter Prime No. p : "))
g = int(input("Enter Primitive root (g<p) : "))

# need to enter the chosen private key
Wa = int(input("Enter the private key of Alice (a<p): "))
Wb = int(input("Enter the private key of Bob (b<p) : "))

#calculating public key of both 
pa = g**Wa % prime 
pb = g**Wb % prime 

#Calculating shared key 
sa = pb**Wa % prime 
sb = pa**Wb % prime 
print("\n After using formula we got the public keys as follows :")
print("Public key of Alice", pa)
print("Public key of Bob", pb)

#after calculating shared key 
print("Shared Secret Key is: ", sa)
print("Shared Secret Key is: ", sb)