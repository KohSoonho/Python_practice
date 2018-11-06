# 4-1
guess_me = 7

if guess_me < 7 :
    print("too low")
elif guess_me > 7 :
    print("too high")
else :
    print("just right")

# 4-2
start = 1

while True :
    if start < guess_me :
        print("too low")
    elif start == guess_me :
        print("found it!")
    else :
        print("oops")
        break
    start += 1

# 4-3
lst = [3, 2, 1, 0]

for i in lst :
    print(i)

# 4-4
print([num for num in range(10) if num % 2 == 0])

# 4-5
squares = {num : num ** 2 for num in range(10)}
print(squares)

# 4-6
odd = {num for num in range(10) if num % 2 == 1}
print(odd)

# 4-7
for value in ("Got %s" % num for num in range(10)) :
    print(value)

# 4-8
def good() :
    return ["Harry", "Ron", "Hermione"]

print(good())

# 4-9
def get_odds(nums) :
    for num in nums :
        if num % 2 == 1 :
            yield num

gen2 = get_odds(range(10))

for count, value in enumerate(gen2) :
    if count == 2 :
        print(value)

def test(func) :
    def new_func(*args, **kwargs) :
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_func

@test
def greeting() :
    print("hello!")

print(greeting())

# 4-10
class OopsException(Exception) :
    pass

# raise OopsException() -> raise exception

try :
    raise OopsException
except OopsException :
    print("Caught an oops")

# 4-11
titles = ["Creature of Habit", "Crewel Fate"]
plots = ["A nun turns into a monster", "A haunted yarn shop"]
movies = dict(zip(titles, plots))
print(movies)
