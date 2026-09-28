in_scope_sites = ["example.copm","target.com"]
user_site = input("Enter website domain:")
if user_site in in_scope_sites:
    print("This site is already in scope for testing!")
else:
    print("New site added to scope!")

in_scope_sites.append(user_site)

print(in_scope_sites)

