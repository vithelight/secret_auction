from replit import clear
from art import logo

print(logo)
print('Welcome to the secret auction program.')

bidders = {}
while True:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))
  bidders[name] = bid
  end = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if end == 'no':
    break
  elif end == 'yes':
    clear()

def find_winner(bidding_record):
  max_bid = 0
  winner = ''
  for name, bid in bidders.items():
    if max_bid < bid:
      max_bid = bid
      winner = name
  print(f'The winner is {winner} with a bid of ${max_bid}.')

find_winner(bidders)
