# REVISION LISTS
'''
shoppingcart = ['apple','cherry','banana']
print(shoppingcart[2])
purchase = input("What would you like to purchase? ")
shoppingcart.append(purchase)
print(shoppingcart[3])
remove = input("What would you like to remove? ")
shoppingcart.remove(remove)
print(shoppingcart)
for item in shoppingcart:
    print(item)
'''

# DICTIONARIES      key : value
shoppingcart = { 'apple': 1.5, 'cherry': 2, 'banana': 0.5 }
print(shoppingcart['apple'])
shoppingcart['orange'] = 4.5
print(shoppingcart)
# get a list of the keys in the dictionary
print(shoppingcart.keys())
# get a list of the values in the dictionary
print(shoppingcart.values())
# remove an item from the dictionary
shoppingcart.pop('apple')
print(shoppingcart)
# find the total of the persons shopping cart
total = 0
for item in shoppingcart:
    total += shoppingcart[item]
print(total)

                    #ONE ITEM IN THE LIST                   x, y, width, heigt
detections = [ {'label': 'dog', 'confidence': 0.9, 'box': [10,10,100,100]},
             {'label': 'person', 'confidence': 0.8, 'box': [20,20,80,60]},
             {'label': 'car', 'confidence': 0.7, 'box': [30,30,80,100]}
            ]
import turtle
t = turtle.Turtle()
turtle.bgcolor("black")

# for each detection - draw a box, label and confidence
for detection in detections:
    t.penup()
    t.pencolor("green")
    box = detection['box']
    x = box[0]
    y = box[1]
    t.goto(x,y)
    t.pendown()
    width = box[2]
    height = box[3]
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    #draw box
    label = detection['label']
    t.write(label)
input("PAUSE")