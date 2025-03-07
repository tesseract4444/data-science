from typing import List, Any


class Card:
    def __init__(self, suit: int, rank: int):
        self.suit: int = suit
        self.rank: int = rank

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Card) and other.suit == self.suit and other.rank == self.rank  # pragma: no cover

    def __repr__(self) -> str:
        return "Card({}, {})".format(self.suit, self.rank)  # pragma: no cover


def can_be_played_on(first_card: Card, second_card: Card) -> bool:
    return first_card.suit == second_card.suit or first_card.rank == second_card.rank


def playable_cards(card: Card, hand: List[Card]) -> List[Card]:
    '''liste = []
    for hand_card in hand:
        if can_be_played_on(hand_card, card):
            liste.append(hand_card)
    return liste'''

    return [hand_card for hand_card in hand if can_be_played_on(hand_card, card)]

print(can_be_played_on(Card(1, 2), Card(1, 3)))
print(playable_cards(Card(3, 13), [Card(3, 12), Card(1, 13), Card(5, 18), Card(3, 18)]))