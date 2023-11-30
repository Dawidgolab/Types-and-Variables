print("Hello in favorite-dish program!!!")

'''
firstFavoriteDish = input("Enter the names of the first favorite delicacy: ")
secoundFavoriteDish = input("Enter the names of the secound favorite delicacy: ")

print(f"Combine two goodies gives us {firstFavoriteDish+secoundFavoriteDish}")
'''
# secound way

'''
FavoriteDishs = input("Enter the names of the two favorite delicacy but secound write after space: ")

splitTheDishes = FavoriteDishs.split(" ")
print(splitTheDishes)
combineDishes = splitTheDishes[0] + splitTheDishes[1]
print(f"Combine two goodies gives us: {combineDishes}")

'''