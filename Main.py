import pygame, random, os, time
from Cards import cards
from SaveLoadScript import SaveLoad

pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("SET")
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "Images")
CARD_DIR = os.path.join(BASE_DIR, "Images", "kaarten")
SAVE_DIR = os.path.join(BASE_DIR, "Saves")
os.makedirs(SAVE_DIR, exist_ok=True)

logo = pygame.image.load(os.path.join(IMG_DIR, "LogoPic.png"))
logo = pygame.transform.scale(logo, (120, 60))

font = pygame.font.SysFont(None, 32)
bigfont = pygame.font.SysFont(None, 42)

#Define
currentcards = []
cards.randomizecurrentcards(currentcards)
selected = []
total_sets = 0
computer_sets = 0
set_this_round = 0
Hint_SET = "None"
early_reset = 0
start_time = pygame.time.get_ticks()
tried_no_sets = 0
hint_used_this_round = 0
ROUND_TIME = 60

def draw_button(rect, text):
    pygame.draw.rect(screen, (200, 200, 200), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    txt = font.render(text, True, (0, 0, 0))
    screen.blit(txt, txt.get_rect(center=rect.center))

def draw_cards():
    card_rects = []
    start_x, start_y = 100, 150

    for i in range(12):
        x = start_x + (i % 4) * 250 #a new row every 4 cards
        y = start_y + (i // 4) * 180 #New collom, mod 4
        rect = pygame.Rect(x, y, 200, 140)

        #Images
        card = currentcards[i]
        filename = str(card) + ".gif"
        img_path = os.path.join(CARD_DIR, filename)

        image = pygame.image.load(img_path).convert_alpha()
        image = pygame.transform.scale(image, (200, 140))
        screen.blit(image, rect)

        #Place
        if i in selected:
            pygame.draw.rect(screen, (255, 200, 0), rect, 4)

        card_rects.append(rect)

    return card_rects

save_btn = pygame.Rect(700, 20, 100, 40)
load_btn = pygame.Rect(820, 20, 100, 40)
noset_btn = pygame.Rect(940, 20, 100, 40)
hint_btn = pygame.Rect(820, 80, 100, 40)

#Game Loop
running = True
if __name__ == "__main__":
    while running: #Mainloop
        screen.fill((240, 240, 240))

        #Timer, independent of loop
        elapsed = (pygame.time.get_ticks() - start_time) // 1000
        remaining = max(0, ROUND_TIME - elapsed)

        #Reset timer and checks if it should award the computer a point
        if remaining == 0 or early_reset == 1:
            cards.randomizecurrentcards(currentcards)
            selected.clear()
            start_time = pygame.time.get_ticks()
            if set_this_round == 0:
                computer_sets += 1
            set_this_round = 0
            early_reset = 0
            tried_no_sets = 0
            hint_used_this_round = 0
            Hint_SET = "None"

        #Computes your inputs basically
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if save_btn.collidepoint(pos):
                    SaveLoad.save_game(currentcards, total_sets, computer_sets, set_this_round, SAVE_DIR)
                elif load_btn.collidepoint(pos): 
                    data = SaveLoad.load_game(SAVE_DIR)
                    if data:
                        currentcards[:] = data["currentcards"]
                        total_sets = data["total_sets"]
                        computer_sets = data["computer_sets"]
                        set_this_round = data["set_this_round"]
                        selected.clear()
                elif noset_btn.collidepoint(pos):
                    if cards.find_all_sets(currentcards) == []:
                        total_sets += 10
                        set_this_round = 1
                        early_reset = 1
                    elif tried_no_sets == 0:
                        computer_sets += 1
                        tried_no_sets = 1
                elif hint_btn.collidepoint(pos):
                    if hint_used_this_round == 0:
                        computer_sets += 1
                        hint_used_this_round = 1
                        Hint_SET = str(cards.find_one_set(currentcards))

                for i, rect in enumerate(card_rects):
                    if rect.collidepoint(pos):
                        if i not in selected and len(selected) < 3:
                            selected.append(i)
                        if len(selected) == 3:
                            c1, c2, c3 = [currentcards[i].get_code() for i in selected]
                            if cards.is_a_SET(c1, c2, c3):
                                total_sets += 1
                                set_this_round = 1
                                for i in selected:
                                    currentcards[i] = cards.generatecard()
                            selected.clear()

        #Text
        screen.blit(logo, (20, 20))
        screen.blit(bigfont.render("Set, the game!", True, (0, 0, 0)), (160, 30))
        screen.blit(font.render(f"Time left: {remaining}s", True, (0, 0, 0)), (500, 30))
        screen.blit(font.render(f"Total points: {total_sets}", True, (0, 0, 0)), (500, 60))
        screen.blit(font.render(f"Computer points: {computer_sets}", True, (0, 0, 0)), (500, 90))
        screen.blit(font.render(f"Hint: {Hint_SET}", True, (0, 0, 0)), (950, 90))

        #Maak de knoppen aan
        draw_button(save_btn, "Save")
        draw_button(load_btn, "Load")
        draw_button(noset_btn, "No Sets")
        draw_button(hint_btn, "Reveal")

        card_rects = draw_cards()

        pygame.display.flip()
        pygame.display.set_icon(logo)
        clock.tick(60)

#Terminates and closes window
pygame.quit()