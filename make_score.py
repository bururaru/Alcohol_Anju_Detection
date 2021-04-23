import pandas as pd

def scoring(labels):

    # 트라이
    print('****점수와 결과 출력 시작****')
    num = len(labels)  # 출력값 개수
    result_dict = {}

    if num != 0:
        for i in range(0, num):
            temp = labels[i].split('-')
            result_dict[temp[0]] = temp[1]
        print(result_dict)  # labels에서 확률 오름차순 정렬이기 때문에, 자동으로 label별 가장 높은 값 하나만 가져옴

        anzulist = ['bokkeum', 'bossam', 'canape', 'cheese', 'chicken', 'corncheese', 'dakbal', 'dakgalbi', 'drysnacks',
                    'egg', 'fried', 'fruit', 'grilledclams', 'grilledfish', 'grilledmeat', 'jeon', 'kkochi', 'muchim',
                    'nacho', 'nut', 'pizza', 'popcorn', 'ramen', 'salad', 'sausage', 'soup', 'spicysoup', 'squid',
                    'sushi', 'tofukimchi', 'tteokbokki', 'gambas', 'parboiled_squid', 'taco', 'pasta']
        alcohollist = ['soju', 'fruit_soju', 'can_beer', 'bottle_beer', 'live_beer', 'makgeolli', 'kettle_makgeolli',
                       'bottle_wine', 'glass_red_wine', 'glass_white_wine', 'sake_pack', 'liquor']

        sortlabels = {"anju": None, "alcohol":None}

        key_list = list(result_dict.keys())
        key_list.reverse()

        for i in range(len(result_dict)):
            if sortlabels["anju"] == None and key_list[i] in anzulist:
                sortlabels["anju"] = key_list[i]
            if sortlabels["alcohol"] == None and key_list[i] in alcohollist:
                sortlabels["alcohol"] = key_list[i]
        anju = sortlabels["anju"]
        anju_score = result_dict[anju]
        alcohol = sortlabels["alcohol"]
        alcohol_score = result_dict[alcohol]

        infolist = pd.read_csv('combination.csv')

        if None in list(sortlabels.values()):
            infolist = pd.read_csv('combination.csv')

            uncomplete_result = infolist[(infolist['anju']==sortlabels["anju"]) | (infolist['alcohol']==sortlabels["alcohol"])]
            uncomplete_result = uncomplete_result.sort_values(by=['score'], ascending=False)
            result = uncomplete_result.iloc[0, :]

            score = None
            desc = str(result[0] if sortlabels["anju"] == None else result[1]) + "과 같이 먹어보는건 어떨까요?"


        else:
            result_ex = infolist[(infolist['anju']==sortlabels["anju"]) & (infolist['alcohol']==sortlabels["alcohol"])]
            result = list(result_ex.iloc[0, :])
            supplement = None

            score = result[3]
            desc = result[2]

        print('****점수****', score)
        print('****설명****', desc)
    else:
        anju = None
        alcohol = None
        score = None
        desc = None
    return score, desc, anju, alcohol, anju_score, alcohol_score