

## Rules

## Deck

- There is a deck with 52 cards
- Four Suits:
    1. Hearts
    2. Diamonds
    3. Clubs
    4. Spades

    **Values**
    ```markdown
    [] Cards 2-10 are worth their face value
    [] Jack, Queen, King worth 10
    [] Ace----+-> Worth 11 if the sum of the hand including it wont bust
              |
              |
              +-> Worth 1 if the sum of the hand including it would bust
    ```
### Goal
> The goal is to get as close to `21` as possible wthout going over it. Going over 21 results in a loss.

### Turns

Borth `Dealer` and `Player` start with 2 cards. The player can see both of their card, but can only see _one_ of the cards the `Dealer` has,

When both `Player` and `Dealer` bust, compare the total of their `hand` and whoever has the highest wins.

|                  Player                  |                   Dealer                      |
| :--------------------------------------: |:---------------------------------------------:|
| Turns is over if Player stays or busts   | Always `hit` if hand total is less than 17    |
| If the Player busts, the Dealer wins     | If dealer busts, player wins                  |

### Basic Construction
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.
