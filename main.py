
from shuffle import crypto_shuffle
values=["2", "3", "4", "5", "6", "7", "8", "9", "10","J","Q","K","A"]
suits = ["H", "D", "C", "S"]

num_of_decks = 4

decs = [(value, suit) for i in range(num_of_decks) for value in values for suit in suits]




crypto_shuffle(decs)
hand = []
dealer_hand = []



def sum_cards(dec):
   total = 0
   aces_count = 0
   for card in dec:
       val = card[0]
       if val == "A":
           total += 11
           aces_count += 1
       elif val in ["J", "Q", "K"]:
           total += 10
       elif val in ["2", "3", "4", "5", "6", "7", "8", "9","10"]:
           total += int(val)
   while total > 21 and aces_count > 0:
       total -= 10
       aces_count -= 1
   return total

while True:
    print(len(decs))
    for i in range(2):
        cards_p = decs.pop()
        hand.append(cards_p)
        cards_d = decs.pop()
        dealer_hand.append(cards_d)
    cards_p = 0
    cards_d = 0

    print("Twoja ręka")
    print(hand)
    sum = sum_cards(hand)
    sum_d = sum_cards(dealer_hand)
    print("Twoja suma: ", sum)
    if sum == 21:
        print("BlackJack!")
        current_round_active=False
    elif sum_d == 21:
        print("Dealer BlackJack!")
        print("Bust!")
        current_round_active=False
    elif sum_d and sum_d == 21:
        print("remis")
        current_round_active=False
    else:
        current_round_active=True
    sum = 0
    sum_d = 0
    print("Karta dealera")
    print(dealer_hand[0])
    played_bust = False
    while current_round_active:
        print("1-Hit")
        print("2-Stand")
        p_choise = int(input("Wybierz: "))
        match p_choise:
            #gracz hituje
            case 1:
                cards_p = decs.pop()
                hand.append(cards_p)
                sum = sum_cards(hand)
                print("Twoje aktualne karty to: ", hand)
                print("Twoja suma to: ", sum)
                if sum > 21:
                    print("Bust!")
                    played_bust = True

                    break
            case 2:
                print("Czekasz")
                played_bust = False
                break
    if not played_bust and current_round_active:
        dealer_sum = sum_cards(dealer_hand)
        print("Pełna ręka krupiera to ",dealer_hand )
        print("suma kart krupiera to ", dealer_sum)
        while dealer_sum < 17:
            cards_d = decs.pop()
            dealer_hand.append(cards_d)
            dealer_sum = sum_cards(dealer_hand)
            print("Karta dealera")
            print(dealer_hand[0])

        player_sum = sum_cards(hand)
        dealer_sum = sum_cards(dealer_hand)
        print("\n--- WYNIK KOŃCOWY RUNDY ---")
        if dealer_sum > 21:
            print("Dealer przekroczył 21! Wygrywasz!")
        elif player_sum > dealer_sum:
            print(f"Wygrywasz! Twój wynik: {player_sum}, Krupier: {dealer_sum}")
        elif player_sum < dealer_sum:
            print(f"Przegrywasz! Twój wynik: {player_sum}, Krupier: {dealer_sum}")
        else:
            print(f"Remis! Obaj macie po {player_sum}")

    decs.extend(hand)
    decs.extend(dealer_hand)
    hand.clear()
    dealer_hand.clear()
    crypto_shuffle(decs)

        # 8. Pytanie o kolejną rundę
    again = input("\nCzy chcesz zagrać kolejną rundę? (t/n): ").strip().lower()
    if again != 't':
        print("Dzięki za grę!")
        break






