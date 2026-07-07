MENU  = {
  "espresso":{
    "ingredients":{
      "water":50,
      "coffee":18
    },
    "cost": 1.5
  },
  "latte": {
      "ingredients":{
      "water":200,
      "milk":150,
      "coffee":24
    },
    "cost": 2.5
  },
  "cappuccino":{
     "ingredients":{
      "water":250,
      "milk":100,
      "coffee":24
  },
  "cost": 3.0
  }
}
money = 0
resources = {
  'water':300,
  "milk":200,
  "coffee":100
}
while True:
  choice = input("what would you like (espresso/latte/cappuccino):")
  if choice == "off":
     is_on = True
  elif choice == "report":
     print(f"water:{resources["water"]}")
     print(f"milk:{resources["milk"]}")
     print(f"coffee:{resources["coffee"]}")
     print(f"money: ${money}")
