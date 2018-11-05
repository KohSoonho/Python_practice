# 3-1
years_list = [1988, 1989, 1990, 1991, 1992]
print(years_list)

# 3-2
print(years_list[3])

# 3-3
print(years_list[-1])

# 3-4
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# 3-5
things[1] = things[1].capitalize()
print(things)

# 3-6
things[0] = things[0].upper()
print(things)

# 3-7
things.remove("salmonella")
print(things)

# 3-8
surprise = ["Groucho", "Chico", "Harpo"]

# 3-9
surprise[-1] = surprise[-1][::-1].capitalize()
print(surprise)

# 3-10
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)

# 3-11
print(e2f["walrus"])

# 3-12
f2e = {}
for english, french in e2f.items() :
    f2e[french] = english
print(f2e)

# 3-13
print(f2e["chien"])

# 3-14
print(set(e2f.keys()))

# 3-15
life = {"animal": {
            "cats": ["Henri", "Grumpy", "Lucy"],
            "octopi": {},
            "emus": {}
            },
        "plants": {},
        "other": {}
        }

# 3-16
print(life.keys())

# 3-17
print(life["animal"].keys())

# 3-18
print(life["animal"]["cats"])
