#######the if statement
cars = ['audi','bmw','corvet','acura','lecus'] ### making a set 
for car in cars: ### creating a for loop
    if cars == 'bmw': ### this declaration making that an === is to be equal to each other
        print(car.upper())
    else: ### declearing an else would be whatever it is the remainnig 
        print(car.title())
    ### demo for a simple understanding with an if statement 
### conditional tests an if statement can be TRUE or FALse for a conditional test
#### TRUEcar = 'btw'
#### TRUEcar == 'btw'
# we will begin FALSE
#### car = 'audi' FALSE
#### car == 'btw' FALSE
### ignoring case when checking for the equality
#### car = 'AUDI' FALSE
#### car = 'audi' FALSE
### test a variable of the value lowercase
###car = 'Audi' TRUE
###car.lower() == 'audi' TRUE
#car = 'Audi' True 
#car.lower() == 'audi' true
### checking the inequality / toppiings
request_topping = 'mushrooms'
if request_topping != 'anchovies':## python returns true
    print("hold the anchives")
### numerical comparisons numerical compariosons
## true age = 18
## true age == 18
answer = 17
input("What number is going to be the right answer")
if answer != 42: ### passes because the value of answer(17) is not equal 42
    print("that is the worong number please answer again") 
# checking the multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21
### FALSE
age_2 = 23
age_0 >= 21 and age_2 >=21
###TRUE

###Checking Whether a value is not in a list
banner_users = ['andrew', 'carolina', 'david']
user = 'maria'

if user not in banner_users:
    print(f"{user.title()}, you can post a response if you wish.")

####Boolean Expression a boolean value can be True or False
#game_active = True
#lose = False

### 5-1 Condtional test
kk = 'subaru'
print("is kk == 'subaru' I predict True.")
print(kk == 'subaru')##### this indication was TRUe

print("\nIs jj == 'audi'? I predict False")
print( kk == 'audi')### indication was False

ll = 'lebron'
print("is ll == 'lebron' I predict is TRUE" )
print(ll == 'lebron')

print("\nIs ll == 'kobe'? I predict False")
print(ll == 'kobe')

marriage = 'serious'
print(" this will mean the world to me == 'serious' I predict True. ")
print(marriage == 'serious')

loser = 'dontwin'
print("dont ever bring that shit 'dontwin' False")
print(loser == 'dontwin')

###5-2 More Conditional Test
gg = ['asdfa','asdf','asdfe','trtry','uiyuiog','mvnnh','qertyrt','yuyih']
for gg in gg:
    if gg == 'lebron':
        print(gg.upper())
    else:
        print(gg.lower())
### if statements
#if conditional_test:
    #do something
what_if = 19
if what_if >= 18:
    print("You are old to enough to vote!")
    print("Have you registered to vote yet")
else:
    print("SOrry, you are too youung to vote.")
    print("please register to vote as soon as you turn 18!")
    

