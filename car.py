#%% 
# camelcase for names of classes
class Car:
    pass

# creating instances/objects of class
car1 = Car()
car2 = Car()
car1 = car2

#print(type(car1))
print(car1 == car2)

# %%

lst = [1,2,3]

print(type(lst))
# %%


# list can change size and have ordering
[1,3,34]

# tuples cannot grow or shrink in size
(1,2,3,4)

# sets: no repetition, fast check of existence in the set
{1,2,3,4}

#%%

print({"clara", "clara"})
print(["clara", "clara"])


#%%
{}
{'asdf': 3}
{'asdf'}
#%%

class Car:

    def __init__(self, brand, model, color="Champagne"):

        if type(brand) != str:
            raise Exception("brand must be a string")

        allowed_brands = ["Ford", "BMW"]
        if brand not in allowed_brands:
            raise Exception()

        self.brand = brand
        self.model = model
        self.color = color

bmw_m3 = Car("BMW", "M3", "Blue")
ford_mustang = Car("Ford", "Mustang")

potato = Car(2, False, 2.3)


print(bmw_m3.brand)
print(ford_mustang.color)
# %%

