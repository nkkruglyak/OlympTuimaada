def auction(creatives, num_of_winners, country=""):
    pass

def simple_auction_0(creatives, num_of_winners):
    # элементы каждой группы имеют один id_of_advertiser
    # эти элементы имеют максимальную цену в списке элементов с одинаковым id_of_advertiser
    winners = []

    max_of_groups = get_max_in_list_id_of_advertiser(creatives, num_of_winners)

    # равно числу разных id_of_advertiser
    if len(max_of_groups) < num_of_winners:
        return False

    max_of_groups.sort(key=lambda x: -x[0].price)

    while len(winners) < max_of_groups:
        lost_winners = num_of_winners - len(winners)
        bigger_groups = []
        bigger_price = max_of_groups[0][0].price
        ind_group = 0
        while max_of_groups[ind_group][0].price == bigger_price:
            bigger_groups.append(max_of_groups[ind_group])
            ind_group += 1
        if len(bigger_groups) > lost_winners:
            # случайно дергаем ind 0  до ind_group
            # из этой группы  дергаем элемент
            # удалим из max_of_groups по ind
            # элемент добавляем в winner

            pass
        else:
            # из каждой группы случайно дернем элемент
            pass
