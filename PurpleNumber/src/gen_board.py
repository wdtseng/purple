# coding=utf-8
"""generate a board from a person

@author: Robert Tseng
"""
from model import *


#----------Population Helper Function-------------#

def populate_tiangan(board, person):
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

def populate_palace(board, person):
    ming_dizhi_offset = calculate_ming_dizhi_offset(person)

    # Fill out the palace starting from Ming grid
    for palace in Palace:
        board.grids[(palace.number + ming_dizhi_offset) % len(DiZhi)].palace = palace

def populate_element(board, person):
    ming_dizhi_offset = calculate_ming_dizhi_offset(person)
    board_element_mapping = [Element.JIN, Element.SHUI, Element.HUO, Element.TU, Element.MU]
    board_element_number_mapping = [4, 2, 6, 5, 3]
    element_index = ((((ming_dizhi_offset / 2) % 3)
                    + (board.grids[ming_dizhi_offset].tian_gan.number / 2))
                     % len(board_element_mapping))
    board.element = board_element_mapping[element_index]
    board.element_number = board_element_number_mapping[element_index]

def populate_tachi_and_classification(board, person):
    ming_dizhi_offset = calculate_ming_dizhi_offset(person)
    board.person_taichi = Taichi(person.year_tian_gan.number % 2)
    board.board_taichi = Taichi(ming_dizhi_offset % 2)
    board.classification = BoardClassification(ming_dizhi_offset % 3)

def populate_destiny_star(board, person):
    ming_dizhi_offset = calculate_ming_dizhi_offset(person)
    destiny_star_mapping = [AlphaStar.TAN_LANG,
                            AlphaStar.JU_MEN,
                            AlphaStar.LU_CUN,
                            AlphaStar.WEN_QU,
                            AlphaStar.LIAN_ZHEN,
                            AlphaStar.WU_QU,
                            AlphaStar.PO_JUN,
                            AlphaStar.LIAN_ZHEN,
                            AlphaStar.WEN_QU,
                            AlphaStar.LU_CUN,
                            AlphaStar.JU_MEN]
    board.destiny_star = destiny_star_mapping[ming_dizhi_offset]

def populate_body_star(board, person):
    body_star_mapping = [AlphaStar.HUO_XING,
                         AlphaStar.TIAN_XIANG,
                         AlphaStar.TIAN_LIANG,
                         AlphaStar.TIAN_TONG,
                         AlphaStar.WEN_CHANG,
                         AlphaStar.TIAN_JI]
    board.body_star = body_star_mapping[person.year_di_zhi.number % 6]

def populate_da_xian(board, person):
    ming_dizhi_offset = calculate_ming_dizhi_offset(person)
    for dizhi_index in xrange(len(DiZhi)):
        board.grids[(ming_dizhi_offset + dizhi_index) % len(DiZhi)].da_xian_start = board.element_number + dizhi_index * 10
        board.grids[(ming_dizhi_offset + dizhi_index) % len(DiZhi)].da_xian_end = board.element_number + dizhi_index * 10 + 9

def populate_alpha_star(board, person):
    # Step 1: Figure out where zi_wei is
    rem = board.element_number - person.lunar_day_of_month % board.element_number
    ziwei_offset_from_chou = (person.lunar_day_of_month + rem) / board.element_number + (1 if rem % 2 == 0 else -1) * rem
    ziwei_dizhi_offset = (DiZhi.CHOU.number + ziwei_offset_from_chou + len(DiZhi)) % len(DiZhi)
    board.grids[ziwei_dizhi_offset].alpha_stars.append(AlphaStar.ZI_WEI)

    # Step 2: Figure out where the other ziwei related alpha stars are
    ziwei_alpha_star = [AlphaStar.TIAN_JI,
                       AlphaStar.TAI_YANG,
                       AlphaStar.WU_QU,
                       AlphaStar.TIAN_TONG,
                       AlphaStar.LIAN_ZHEN]
    ziwei_alpha_star_offset = [11, 9, 8, 7, 4]
    for index in xrange(len(ziwei_alpha_star)):
        board.grids[(ziwei_dizhi_offset + ziwei_alpha_star_offset[index]) % len(DiZhi)].alpha_stars.append(ziwei_alpha_star[index])

    # Step 3: Figure ou where tianfu is
    tianfu_dizhi_offset = (DiZhi.YIN.number - (ziwei_dizhi_offset - DiZhi.YIN.number) + len(DiZhi)) % len(DiZhi)
    board.grids[tianfu_dizhi_offset].alpha_stars.append(AlphaStar.TIAN_FU)

    # Step 4: Figure out where other tianfu related alpha stars are
    tianfu_alpha_star = [AlphaStar.TAI_YIN,
                         AlphaStar.TAN_LANG,
                         AlphaStar.JU_MEN,
                         AlphaStar.TIAN_XIANG,
                         AlphaStar.TIAN_LIANG,
                         AlphaStar.QI_SHA,
                         AlphaStar.PO_JUN]
    tianfu_alpha_star_offset = [1, 2, 3, 4, 5, 6, 10]
    for index in xrange(len(tianfu_alpha_star)):
        board.grids[(tianfu_dizhi_offset + tianfu_alpha_star_offset[index]) % len(DiZhi)].alpha_stars.append(tianfu_alpha_star[index])

#----------DiZhi Calculation Helper Function-------------#

def calculate_ming_dizhi_offset(person):
    # Figure out which DiZhi matches the Ming palace by adding the month to DiZhi.YIN
    # and subtracting the time_di_zhi from that.
    return ((DiZhi.YIN.number + person.lunar_month_of_year - 1) - person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)

def calculate_body_dizhi_offset(person):
    return ((DiZhi.YIN.number + person.lunar_month_of_year - 1) + person.time_di_zhi.number) % len(DiZhi)

def generate_board(person):
    board = Board()
    board.person = person

    # Populate the 12 Grids with DiZhi
    board.grids = [Grid() for _ in xrange(len(DiZhi))]
    for dizhi in DiZhi:
        grid = board.grids[dizhi.number]
        grid.di_zhi = dizhi

    # Populate the 12 Grids with TianGan
    populate_tiangan(board, person)

    # Populate the 12 Grids with palace
    populate_palace(board, person)

    # Determine where the body palace is
    body_dizhi_offset = calculate_body_dizhi_offset(person)
    board.grids[body_dizhi_offset].is_body_palace = True;

    # Determine the element and element_number of the board
    populate_element(board, person)

    # Determine the TaiChi of the person and the board
    populate_tachi_and_classification(board, person)

    # Determine destiny_star
    populate_destiny_star(board, person)

    # Determine body_star
    populate_body_star(board, person)

    # Calculate da_xian for all grids
    populate_da_xian(board, person)

    # Calculate where the alpha_stars
    populate_alpha_star(board, person)

    # For debugging: print the board. This breaks when running on app engine due
    # to utf-8 logging bug.
    # print_board(board)
    return board





