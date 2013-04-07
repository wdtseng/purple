# coding=utf-8
"""generate a board from a person

@author: Robert Tseng
"""

from model import *

def generate_board(person):
    board = Board()
    board.person = person

    # Populate the 12 Grids with DiZhi first
    board.grids = [Grid() for _ in xrange(len(DiZhi))]
    for dizhi in DiZhi:
        grid = board.grids[dizhi.number]
        grid.di_zhi = dizhi

    # Populate the 12 Grids with TianGan
    # Step 1: Calculate which DiZhi matches with person's year_tian_gan
    year_tian_gan_dizhi_offset = DiZhi.XU.number - person.year_tian_gan.number
    if year_tian_gan_dizhi_offset == DiZhi.CHOU.number:
        # Special case: if the year_tian_gan is supposed to match with CHOU, it
        # really mean that it should match with HAI (go figure...)
        year_tian_gan_dizhi_offset = DiZhi.HAI.number

    # Step 2: Figure out the TianGan matches the ZI grid
    zi_tiangan_offset = (len(DiZhi) - year_tian_gan_dizhi_offset + person.year_tian_gan.number) % len(TianGan)

    # Step 3: Fill out the TianGan of the grid starting from the ZI grid.
    cur_tiangan_offset = zi_tiangan_offset
    for dizhi in DiZhi:
        cur_tiangan = TianGan(cur_tiangan_offset % len(TianGan))
        if dizhi == DiZhi.YIN:
            # Special case: YIN's tiangan is alway the same as ZI's
            cur_tiangan = board.grids[DiZhi.ZI.number].tian_gan
        elif dizhi == DiZhi.MAO:
            # Special case: MAO's tiangan is always the same as CHOU's
            cur_tiangan = board.grids[DiZhi.CHOU.number].tian_gan
        else:
            # Otherwise, increment the TianGan
            cur_tiangan_offset = cur_tiangan_offset + 1
        board.grids[dizhi.number].tian_gan = cur_tiangan


    # Populate the 12 Grids with palace
    # Step 1: Figure out which DiZhi matches the Ming palace by adding the month to DiZhi.YIN
    # and subtracting the time_di_zhi from that.
    ming_dizhi_offset = ((DiZhi.YIN.number + person.lunar_month_of_year - 1) - person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)

    # Step 2: Fill out the palace starting from Ming grid
    for palace in Palace:
        board.grids[(palace.number + ming_dizhi_offset) % len(DiZhi)].palace = palace


    # For debugging: print the board
    print_board(board)
    return board





