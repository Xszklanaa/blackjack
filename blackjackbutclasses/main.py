from game import GameEngine
from exceptions import *


def main():
    engine = GameEngine(start_balance=1000)
    print("=== Welcome to My BlackJack Game ===")

    # 1. GŁÓWNA PĘTLA GRY (kręci się runda za rundą)
    while True:
        print(f"\nYour game balance: {engine._balance}")

        if engine._balance <= 0:
            print("You lost! Game Over.")
            break

        # 2. WEWNĘTRZNA PĘTLA ZAKŁADU
        while True:
            try:
                bal_input = int(input("Enter your bet: "))
                engine.place_bet(bal_input)
                break  # Zakład poprawny? Wychodzimy TYLKO z pętli obstawiania
            except ValueError:
                print("Invalid input! Enter a number.")
            except InsufficientFunds:  # Upewnij się, że nazwa zgadza się z exceptions.py
                print("Insufficient funds!")

        # 3. FAZA ROZDANIA (Uruchamia się OD RAZU po poprawnym zakładzie)
        engine.start_round()
        print("\n--- Cards Dealt ---")
        print(f"Player hand score: {engine._player_hand.score}")
        print(f"Dealer shows: {engine._dealer_hand.cards[0]}")

        # 4. WEWNĘTRZNA PĘTLA TURY GRACZA (HIT / STAND)
        while True:
            # Jeśli gracz od razu dostał 21, nie ma sensu go pytać o ruch
            if engine._player_hand.score == 21:
                print("Blackjack!")
                break

            choose = input("Do you want to [H]it or [S]tand?: ").strip().lower()

            if choose == 'h':
                try:
                    engine.hit()
                    print(f"Your score: {engine._player_hand.score}")

                    if engine._player_hand.is_bust():
                        print("You bust!")
                        break  # Koniec tury gracza, bo przegrał
                except InvalidMove as e:
                    print(e)
                    break
            elif choose == 's':
                engine.stand()  # Krupier dobiera swoje karty w tej metodzie
                break  # Gracz pasuje, koniec tura gracza
            else:
                print("Invalid input! Enter [H]it or [S]tand.")

        # 5. FAZA ROZSTRZYGNIĘCIA (Na samym końcu rundy, po zakończeniu Hit/Stand)
        print("\n--- Round Settlement ---")
        print(f"Dealer's final score: {engine._dealer_hand.score}")
        engine.settle_round()


if __name__ == "__main__":
    main()