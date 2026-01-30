import random

class cards():
    color_dic = {1:'green', 2:'purple', 3:'red'}
    shape_dic = {1:'diamond', 2:'oval', 3:'squiggle'}
    inside_dic = {1:'empty', 2:'shaded', 3:'filled'}

    def __init__(self, code=None):
        if code is None:
            self.code = [random.randrange(1, 4) for _ in range(4)]
        else:
            self.code = code

    @staticmethod
    def generatecard():
        return cards([random.randrange(1, 4) for _ in range(4)])
    
    def get_code(self): #Magic methode???
        if isinstance(self.code, list):
            return self.code.copy()
        else:
            return self.code.code.copy()
        
    @staticmethod
    def randomizecurrentcards(currentcards):
        currentcards.clear()
        for _ in range(12):
            currentcards.append(cards.generatecard())


    def find_all_sets(currentcards):
        currentcards2 = [x.get_code() for x in currentcards]

        n = len(currentcards2)
        sets_found = []
        
        card_to_index = {tuple(card): i for i, card in enumerate(currentcards2)}
        
        for i in range(n): #O(n)
            for j in range(i + 1, n):
                # Calculate what the third card must for a SET
                third_card = []
                for k in range(len(currentcards2[i])):
                    attr_i = currentcards2[i][k]
                    attr_j = currentcards2[j][k]
                    
                    if attr_i == attr_j:
                        # If two cards have the same attribute, third must match
                        third_card.append(attr_i)
                    else:
                        # If two cards differ, third must be the remaining value
                        third_card.append(6 - attr_i - attr_j)
                third_card_tuple = tuple(third_card)

                if third_card_tuple in card_to_index:
                    k = card_to_index[third_card_tuple]
                    if k > j:
                        sets_found.append([i, j, k])
        return sets_found


    @staticmethod
    def is_a_SET(card1, card2, card3):
        for i in range(4):
            if len({card1[i], card2[i], card3[i]}) == 2:
                return False
        return True

    def __str__(self):
        return(f"{cards.color_dic[self.code[0]]}{cards.shape_dic[self.code[1]]}{cards.inside_dic[self.code[2]]}{self.code[3]}")
    
    @staticmethod
    def third_card(a, b):
        return [a[i] if a[i] == b[i] else 6 - a[i] - b[i] for i in range(4)]
    
    def find_one_set(currentcards):
        currentcards2 = [x.get_code() for x in currentcards]
        n = len(currentcards2)
        card_to_index = {tuple(card): i for i, card in enumerate(currentcards2)}
        for i in range(n):
            for j in range(i + 1, n):
                third_card = []
                for k in range(len(currentcards2[i])):
                    attr_i = currentcards2[i][k]
                    attr_j = currentcards2[j][k]

                    if attr_i == attr_j:
                        third_card.append(attr_i)
                    else:
                        third_card.append(6 - attr_i - attr_j)
                
                third_card_tuple = tuple(third_card)
                if third_card_tuple in card_to_index:
                    k = card_to_index[third_card_tuple]
                    if k > j:
                        return [i, j, k]
        return None