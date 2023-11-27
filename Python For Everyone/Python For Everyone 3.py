tilecolor = ('red':100,'gold':200,'white':90)

print('--------- Tile Calculation Program By POONPHUBEJ ---------')
try:
    tiles = int(input('How Many Tiles Do You Want To Lay: '))
    row = int(input('How Maney Tiles Muat Ba Laid In 1 Row: ')) # 3 pieces per row
    color = input('What Color Are The Tiles? [red / gold / white]: ')
except:
    print('Please fill in numbers only!')
    tiles = int(input('How Many Tiles Do You Want To Lay: '))
    row = int(input('How Maney Tiles Muat Ba Laid In 1 Row: '))
    color = input('What Color Are The Tiles? [red / gold / white]: ')

print('------Calculate-------')
total_row = tiles // row
remain_tiles = tiles % row
 
#print(total_row,remain_tiles)

buy_more = row - remain_tiles

print(f'There are all: {tiles} tiles')
print(f'1 row can laid {row} tiles')
print('------calculate-------')
print('A total of {} rows of tiles must be laid'.format(total_row))
print('There are {} tiles left that have not yet been laid in a full row'.format(remain_tiles))
print('Customers must purchase {} additional tiles.'.formst(buy_more))
print('Total amount required to purchase additonal tiles'.format(buy_more) * )


