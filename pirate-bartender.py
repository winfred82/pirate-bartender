import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def ask_questions():
    responses={}

    for key,value in questions.items():
        drink_type=key
        print drink_type
        drink_question=value
        print drink_question + "(y or yes)"
        responses[drink_type]=raw_input().lower() in ["y","yes"]
        print responses
        print '\n'

    return responses

def make_drink(responses):
    customer_drink=[]
    for key,value in responses.items():
        if value:
            customer_drink.append(random.choice(ingredients[key]))

    return customer_drink

if __name__ == '__main__':
    responses=ask_questions()
    customer_drink=make_drink(responses)
    print 'Here we go'
    for ingredient in customer_drink:
        print("Drink has {}".format(ingredient))
