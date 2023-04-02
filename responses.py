import random


def handle_response(message) -> str:
    p_message = message.lower()
    p_message_string = p_message.split(' ')

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`no chance`"

    if p_message == 'roll adv':
        r1 = random.randint(1, 20)
        r2 = random.randint(1, 20)
        if r1 > r2:
            return f"{r1} ~~{r2}~~"
        else:
            return f"~~{r1}~~ {r2}"
    elif p_message == 'roll disadv':
        r1 = random.randint(1, 20)
        r2 = random.randint(1, 20)
        if r1 > r2:
            return f"~~{r1}~~ {r2}"
        else:
            return f"{r1} ~~{r2}~~"
    elif p_message[0:4] == 'roll' and 'd' in p_message:
        dice_list = p_message.split(' ')
        dice_list = dice_list[1:]
        results = []
        for roll in dice_list:
            parts = roll.split('d')
            no_of_dice = int(parts[0])
            sided_dice = int(parts[1])
            result = []
            for i in range(no_of_dice):
                result.append(random.randint(1, sided_dice))
            results.append(result)
        return_string = ''
        for result in results:
            for roll in result:
                return_string += str(roll) + ' '
            return_string += '\n'
        return return_string





