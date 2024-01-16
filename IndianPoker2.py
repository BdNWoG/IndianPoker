import random

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.card = None
        self.bet = 0
        self.folded = False

def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def get_card_value(card):
    rank = card['rank']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[rank]

def take_bet(player):
    while True:
        try:
            action = input(f"{player.name}, you have {player.chips} chips. Do you want to bet (b), fold (f), or call (c)? ").lower()
            if action not in ['b', 'f', 'c']:
                print("Invalid action. Please choose 'b' to bet, 'f' to fold, or 'c' to call.")
                continue

            if action == 'b':
                bet = int(input("Enter your bet: "))
                if bet < 0 or bet > player.chips:
                    print("Invalid bet. Please bet between 0 and your remaining chips.")
                    continue
                player.bet = bet
            elif action == 'f':
                player.folded = True

            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def rotate_blinds(players):
    # Rotate blinds
    players.append(players.pop(0))

def distribute_blinds(players):
    # Small blind
    players[0].bet = 1
    players[1].bet = 2
    players[0].chips -= 1
    players[1].chips -= 2

def distribute_winnings(winner, loser):
    winner.chips += winner.bet + loser.bet + winner.bet + loser.bet
    loser.chips -= winner.bet + loser.bet + winner.bet + loser.bet

def distribute_folded_winnings(folded_player, opponent):
    if 'A' in folded_player.card['rank']:
        half_stake = (folded_player.chips + folded_player.bet) // 2
        opponent.chips += half_stake
        folded_player.chips -= half_stake

def indian_poker():
    player1 = Player("Player 1", 100)
    player2 = Player("Player 2", 100)
    players = [player1, player2]
    deck = initialize_deck()

    while True:
        # Rotate blinds
        rotate_blinds(players)

        # Deal cards
        for player in players:
            player.card = deal_card(deck)

        # Hide own cards and show opponents' cards
        for player in players:
            print(f"{player.name}'s card: {'Hidden' if player.folded else player.card}")

        # Distribute blinds
        distribute_blinds(players)

        # Betting round
        for player in players:
            if not player.folded:
                take_bet(player)

        # Determine the winner
        if not players[0].folded and not players[1].folded:
            player1_value = get_card_value(player1.card)
            player2_value = get_card_value(player2.card)

            if player1_value > player2_value:
                print(f"{player1.name} wins {player2.bet + player1.bet + player2.bet + player1.bet} chips!")
                distribute_winnings(player1, player2)
            elif player1_value < player2_value:
                print(f"{player2.name} wins {player2.bet + player1.bet + player2.bet + player1.bet} chips!")
                distribute_winnings(player2, player1)
            else:
                print("It's a tie!")

        # Handle folded player with A
        for player in players:
            if player.folded and 'A' in player.card['rank']:
                distribute_folded_winnings(player, players[1 - players.index(player)])

        print(f"{player1.name}'s chips: {player1.chips}")
        print(f"{player2.name}'s chips: {player2.chips}")

        # Check if players want to continue
        play_again = input("Do you want to play another round? (y/n): ")
        if play_again.lower() != 'y':
            break

# Game starts here
indian_poker()
