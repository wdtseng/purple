# coding=utf-8
"""generate a board from a person

@author: Robert Tseng
"""
from model import *
from model_util import *
#----------Population Helper Function-------------#

def __populate_tiangan(board, person):
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

def __populate_palace(board, person):
    ming_dizhi_offset = __calculate_ming_dizhi_offset(person)

    # Fill out the palace starting from Ming grid
    for palace in Palace:
        board.grids[(palace.number + ming_dizhi_offset) % len(DiZhi)].palace = palace

def __populate_element(board, person):
    ming_dizhi_offset = __calculate_ming_dizhi_offset(person)
    board_element_mapping = [Element.JIN, Element.SHUI, Element.HUO, Element.TU, Element.MU]
    board_element_number_mapping = [4, 2, 6, 5, 3]
    element_index = ((((ming_dizhi_offset / 2) % 3)
                    + (board.grids[ming_dizhi_offset].tian_gan.number / 2))
                     % len(board_element_mapping))
    board.element = board_element_mapping[element_index]
    board.element_number = board_element_number_mapping[element_index]

def __populate_tachi_and_classification(board, person):
    ming_dizhi_offset = __calculate_ming_dizhi_offset(person)
    board.person_taichi = Taichi(person.year_tian_gan.number % 2)
    board.board_taichi = Taichi(ming_dizhi_offset % 2)
    board.classification = BoardClassification(ming_dizhi_offset % 3)

def __populate_destiny_star(board, person):
    ming_dizhi_offset = __calculate_ming_dizhi_offset(person)
    destiny_star_mapping = [StarType.TAN_LANG,
                            StarType.JU_MEN,
                            StarType.LU_CUN,
                            StarType.WEN_QU,
                            StarType.LIAN_ZHEN,
                            StarType.WU_QU,
                            StarType.PO_JUN,
                            StarType.LIAN_ZHEN,
                            StarType.WEN_QU,
                            StarType.LU_CUN,
                            StarType.JU_MEN]
    board.destiny_star = Star(type=destiny_star_mapping[ming_dizhi_offset])

def __populate_body_star(board, person):
    body_star_mapping = [StarType.HUO_XING,
                         StarType.TIAN_XIANG,
                         StarType.TIAN_LIANG,
                         StarType.TIAN_TONG,
                         StarType.WEN_CHANG,
                         StarType.TIAN_JI]
    board.body_star = Star(type=body_star_mapping[person.year_di_zhi.number % 6])

def __populate_da_xian(board, person):
    ming_dizhi_offset = __calculate_ming_dizhi_offset(person)
    for dizhi_index in xrange(len(DiZhi)):
        board.grids[(ming_dizhi_offset + dizhi_index) % len(DiZhi)].da_xian_start = board.element_number + dizhi_index * 10
        board.grids[(ming_dizhi_offset + dizhi_index) % len(DiZhi)].da_xian_end = board.element_number + dizhi_index * 10 + 9

def __populate_alpha_stars(board, person):
    # Step 1: Figure out where zi_wei is
    rem = board.element_number - person.lunar_day_of_month % board.element_number
    ziwei_offset_from_chou = (person.lunar_day_of_month + rem) / board.element_number + (1 if rem % 2 == 0 else -1) * rem
    ziwei_dizhi_offset = (DiZhi.CHOU.number + ziwei_offset_from_chou + len(DiZhi)) % len(DiZhi)
    board.grids[ziwei_dizhi_offset].stars.append(Star(type=StarType.ZI_WEI))

    # Step 2: Figure out where the other ziwei related alpha stars are
    ziwei_alpha_star = [StarType.TIAN_JI,
                       StarType.TAI_YANG,
                       StarType.WU_QU,
                       StarType.TIAN_TONG,
                       StarType.LIAN_ZHEN]
    ziwei_alpha_star_offset = [11, 9, 8, 7, 4]
    for index in xrange(len(ziwei_alpha_star)):
        idx = (ziwei_dizhi_offset + ziwei_alpha_star_offset[index]) % len(DiZhi)
        board.grids[idx].stars.append(Star(type=ziwei_alpha_star[index]))

    # Step 3: Figure ou where tianfu is
    tianfu_dizhi_offset = (DiZhi.YIN.number - (ziwei_dizhi_offset - DiZhi.YIN.number) + len(DiZhi)) % len(DiZhi)
    board.grids[tianfu_dizhi_offset].stars.append(Star(type=StarType.TIAN_FU))

    # Step 4: Figure out where other tianfu related alpha stars are
    tianfu_alpha_star = [StarType.TAI_YIN,
                         StarType.TAN_LANG,
                         StarType.JU_MEN,
                         StarType.TIAN_XIANG,
                         StarType.TIAN_LIANG,
                         StarType.QI_SHA,
                         StarType.PO_JUN]
    tianfu_alpha_star_offset = [1, 2, 3, 4, 5, 6, 10]
    for index in xrange(len(tianfu_alpha_star)):
        idx = (tianfu_dizhi_offset + tianfu_alpha_star_offset[index]) % len(DiZhi)
        board.grids[idx].stars.append(Star(type=tianfu_alpha_star[index]))

def __populate_beta_stars(board, person):
    # Step 1: Figure out where zuofu is
    zuofu_dizhi_offset = (DiZhi.CHEN.number + person.lunar_month_of_year - 1) % len(DiZhi)
    board.grids[zuofu_dizhi_offset].stars.append(Star(type=StarType.ZUO_FU))

    # Step 2: Figure out where youbi is
    youbi_dizhi_offset = (DiZhi.XU.number - person.lunar_month_of_year + 1 + len(DiZhi)) % len(DiZhi)
    board.grids[youbi_dizhi_offset].stars.append(Star(type=StarType.YOU_BI))

    # Step 3: Figure out where wenqu is
    wenqu_dizhi_offset = (DiZhi.CHEN.number + person.time_di_zhi.number) % len(DiZhi)
    board.grids[wenqu_dizhi_offset].stars.append(Star(type=StarType.WEN_QU))

    # Step 4: Figure out where wenchang is
    wenchang_dizhi_offset = (DiZhi.XU.number - person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)
    board.grids[wenchang_dizhi_offset].stars.append(Star(type=StarType.WEN_CHANG))

    # Step 5: Figure out where lucun, qingyang, and tuoluo is
    lucun_dizhi = [DiZhi.YIN, DiZhi.MAO, DiZhi.SI, DiZhi.WU, DiZhi.SI, DiZhi.WU, DiZhi.SHEN, DiZhi.YOU, DiZhi.HAI, DiZhi.ZI]
    lucun_dizhi_offset = lucun_dizhi[person.year_tian_gan.number].number
    board.grids[lucun_dizhi_offset].stars.append(Star(type=StarType.LU_CUN))
    board.grids[(lucun_dizhi_offset + 1) % len(DiZhi)].stars.append(Star(type=StarType.QING_YANG))
    board.grids[(lucun_dizhi_offset - 1 + len(DiZhi)) % len(DiZhi)].stars.append(Star(type=StarType.TUO_LUO))

    # Step 6: Figure out where tiankui is
    tiankui_dizhi = [DiZhi.WEI, DiZhi.SHEN, DiZhi.YOU, DiZhi.HAI, DiZhi.CHOU, DiZhi.ZI, DiZhi.CHOU, DiZhi.YIN, DiZhi.MAO, DiZhi.SI]
    tiankui_dizhi_offset = tiankui_dizhi[person.year_tian_gan.number].number
    board.grids[tiankui_dizhi_offset].stars.append(Star(type=StarType.TIAN_KUI))

    # Step 7: Figure out where tianrong is
    tianrong_dizhi = [DiZhi.CHOU, DiZhi.ZI, DiZhi.HAI, DiZhi.YOU, DiZhi.WEI, DiZhi.SHEN, DiZhi.WEI, DiZhi.WU, DiZhi.SI, DiZhi.MAO]
    tianrong_dizhi_offset = tianrong_dizhi[person.year_tian_gan.number].number
    board.grids[tianrong_dizhi_offset].stars.append(Star(type=StarType.TIAN_RONG))

    # Step 8: Figure out where mingma and yuema is (both are calculated the same way, except
    #         one look at year dizhi and another look at month dizhi
    tianma_dizhi = [DiZhi.YIN, DiZhi.HAI, DiZhi.SHEN, DiZhi.SI]
    mingma_dizhi_offset = tianma_dizhi[person.year_di_zhi.number % 4].number
    yuema_dizhi_offset = tianma_dizhi[(person.lunar_month_of_year + DiZhi.YIN.number - 1) % 4].number
    board.grids[mingma_dizhi_offset].stars.append(Star(type=StarType.MING_MA))
    board.grids[yuema_dizhi_offset].stars.append(Star(type=StarType.YUE_MA))

    # Step 9: Figure out where xishen and huagai is
    xishen_dizhi_offset = (mingma_dizhi_offset + 1) % len(DiZhi)
    huagai_dizhi_offset = (mingma_dizhi_offset + 2) % len(DiZhi)
    board.grids[xishen_dizhi_offset].stars.append(Star(type=StarType.XI_SHEN))
    board.grids[huagai_dizhi_offset].stars.append(Star(type=StarType.HUA_GAI))

    # Step 10: Figure out where hongluan and tianxi is
    hongluan_dizhi_offset = (DiZhi.MAO.number - person.year_di_zhi.number + len(DiZhi)) % len(DiZhi)
    tianxi_dizhi_offset = (hongluan_dizhi_offset + 6) % len(DiZhi)
    board.grids[hongluan_dizhi_offset].stars.append(Star(type=StarType.HONG_LUAN))
    board.grids[tianxi_dizhi_offset].stars.append(Star(type=StarType.TIAN_XI))

    # Step 11: Figure out where guchen and guasu is
    guchen_dizhi = [DiZhi.SI, DiZhi.SHEN, DiZhi.HAI, DiZhi.YIN]
    guasu_dizhi = [DiZhi.CHOU, DiZhi.CHEN, DiZhi.WEI, DiZhi.XU]
    index = (person.year_di_zhi.number - DiZhi.YIN.number) / 3
    if person.year_di_zhi == DiZhi.ZI or person.year_di_zhi == DiZhi.CHOU:
        index = 3
    guchen_dizhi_offset = guchen_dizhi[index].number
    guasu_dizhi_offset = guasu_dizhi[index].number
    board.grids[guchen_dizhi_offset].stars.append(Star(type=StarType.GU_CHEN))
    board.grids[guasu_dizhi_offset].stars.append(Star(type=StarType.GUA_SU))

    # Step 12: Figure out where tianku, tianxu, and tiankong is
    tianku_dizhi_offset = (DiZhi.WU.number - person.year_di_zhi.number + len(DiZhi)) % len(DiZhi)
    tianxu_dizhi_offset = (DiZhi.WU.number + person.year_di_zhi.number + len(DiZhi)) % len(DiZhi)
    tiankong_dizhi_offset = (person.year_di_zhi.number + 1) % len(DiZhi)
    board.grids[tianku_dizhi_offset].stars.append(Star(type=StarType.TIAN_KU))
    board.grids[tianxu_dizhi_offset].stars.append(Star(type=StarType.TIAN_XU))
    board.grids[tiankong_dizhi_offset].stars.append(Star(type=StarType.TIAN_KONG))

    # Step 13: Figure out where tianxing, tianyao, and yinsha is
    tianxing_dizhi_offset = (DiZhi.YOU.number + person.lunar_month_of_year - 1 + len(DiZhi)) % len(DiZhi)
    tianyao_dizhi_offset = (DiZhi.CHOU.number + person.lunar_month_of_year - 1 + len(DiZhi)) % len(DiZhi)
    yinsha_dizhi_offset = (DiZhi.YIN.number - (((person.lunar_month_of_year - 1) % 6) * 2) + len(DiZhi)) % len(DiZhi)
    board.grids[tianxing_dizhi_offset].stars.append(Star(type=StarType.TIAN_XING))
    board.grids[tianyao_dizhi_offset].stars.append(Star(type=StarType.TIAN_YAO))
    board.grids[yinsha_dizhi_offset].stars.append(Star(type=StarType.YIN_SHA))

    # Step 14: Figure out where dikong and dijie is
    dikong_dizhi_offset = (DiZhi.HAI.number - person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)
    dijie_dizhi_offset = (DiZhi.HAI.number + person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)
    board.grids[dikong_dizhi_offset].stars.append(Star(type=StarType.DI_KONG))
    board.grids[dijie_dizhi_offset].stars.append(Star(type=StarType.DI_JIE))

    # Step 15: Figure out where huoxing and lingxing is
    huoxing_dizhi_base = [DiZhi.CHOU, DiZhi.YOU, DiZhi.YIN, DiZhi.MAO]
    lingxing_dizhi_base = [DiZhi.MAO, DiZhi.XU, DiZhi.XU, DiZhi.XU]
    index = (person.year_di_zhi.number - DiZhi.YIN.number + len(DiZhi)) % 4
    huoxing_dizhi_offset = (huoxing_dizhi_base[index].number + person.time_di_zhi.number) % len(DiZhi)
    lingxing_dizhi_offset = (lingxing_dizhi_base[index].number + person.time_di_zhi.number) % len(DiZhi)
    board.grids[huoxing_dizhi_offset].stars.append(Star(type=StarType.HUO_XING))
    board.grids[lingxing_dizhi_offset].stars.append(Star(type=StarType.LING_XING))

def __populate_sihua(board, person):
    sihua_matrix = [
        [StarType.LIAN_ZHEN  , StarType.PO_JUN     , StarType.WU_QU      , StarType.TAI_YANG ],
        [StarType.TIAN_JI    , StarType.TIAN_LIANG , StarType.ZI_WEI     , StarType.TAI_YIN  ],
        [StarType.TIAN_TONG  , StarType.TIAN_JI    , StarType.WEN_CHANG  , StarType.LIAN_ZHEN],
        [StarType.TAI_YIN    , StarType.TIAN_TONG  , StarType.TIAN_JI    , StarType.JU_MEN   ],
        [StarType.TAN_LANG   , StarType.TAI_YIN    , StarType.YOU_BI     , StarType.TIAN_JI  ],
        [StarType.WU_QU      , StarType.TAN_LANG   , StarType.TIAN_LIANG , StarType.WEN_QU   ],
        [StarType.TAI_YANG   , StarType.WU_QU      , StarType.TAI_YIN    , StarType.TIAN_TONG],
        [StarType.JU_MEN     , StarType.TAI_YIN    , StarType.WEN_QU     , StarType.WEN_CHANG],
        [StarType.TIAN_LIANG , StarType.ZI_WEI     , StarType.ZUO_FU     , StarType.WU_QU    ],
        [StarType.PO_JUN     , StarType.JU_MEN     , StarType.TAI_YIN    , StarType.TAN_LANG ]]

    sihua_stars = sihua_matrix[person.year_tian_gan.number]
    for sihua in SiHua:
        sihua_star = sihua_stars[sihua.number]
        for grid in board.grids:
            star_found = find_star_in_grid(grid, sihua_star)
            if star_found is not None:
                star_found.si_hua = sihua

def __populate_brightness(board, person):
    assert isinstance(board, Board)
    for grid in board.grids:
        for star in grid.stars:
            star.brightness = star_brightness(star.type, grid.di_zhi)

#----------DiZhi Calculation Helper Function-------------#

def __calculate_ming_dizhi_offset(person):
    # Figure out which DiZhi matches the Ming palace by adding the month to DiZhi.YIN
    # and subtracting the time_di_zhi from that.
    return ((DiZhi.YIN.number + person.lunar_month_of_year - 1) - person.time_di_zhi.number + len(DiZhi)) % len(DiZhi)

def __calculate_body_dizhi_offset(person):
    return ((DiZhi.YIN.number + person.lunar_month_of_year - 1) + person.time_di_zhi.number) % len(DiZhi)

#----------Public Function-------------#

def generate_board(person):
    board = Board()
    board.person = person

    # Populate the 12 Grids with DiZhi
    board.grids = [Grid() for _ in xrange(len(DiZhi))]
    for dizhi in DiZhi:
        grid = board.grids[dizhi.number]
        grid.di_zhi = dizhi

    # Populate the 12 Grids with TianGan
    __populate_tiangan(board, person)

    # Populate the 12 Grids with palace
    __populate_palace(board, person)

    # Determine where the body palace is
    body_dizhi_offset = __calculate_body_dizhi_offset(person)
    board.grids[body_dizhi_offset].is_body_palace = True;

    # Determine the element and element_number of the board
    __populate_element(board, person)

    # Determine the TaiChi of the person and the board
    __populate_tachi_and_classification(board, person)

    # Determine destiny_star
    __populate_destiny_star(board, person)

    # Determine body_star
    __populate_body_star(board, person)

    # Calculate da_xian for all grids
    __populate_da_xian(board, person)

    # Calculate where the alpha_stars
    __populate_alpha_stars(board, person)

    # Calculate where the beta_stars
    __populate_beta_stars(board, person)

    # Calculate the sihua
    __populate_sihua(board, person)

    # Calculate brightness
    __populate_brightness(board, person)

    # For debugging: print the board. This breaks when running on app engine due
    # to utf-8 logging bug.
    # print_board(board)
    return board





