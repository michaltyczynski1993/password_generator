import random, generator as g

new_password = g.Password()
# main
for i in range(new_password.num_characters):
	i = random.randrange(len(new_password.LETTERS)-1)
	new_password.password += new_password.LETTERS[i]

print(new_password.password)