flavors =["chocolate","vanilla","lemon","strawberry"]
user_resp = input("what is the ice cream flavor you like best, guess our available flavors: ")

while user_resp.lower() not in flavors:
    print("Flavor not avaiable ... try again")
    user_resp = input("what is the ice cream flavor you like best, guess our available flavors: ")

print(f"OK!!.. {user_resp} ice cream coming right up !!!")    