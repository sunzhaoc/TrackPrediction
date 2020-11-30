from sklearn.externals import joblib
import copy
# data = joblib.load("./data/01origin_data.pkl")
# temp = data.data.values.tolist()
#
# joblib.dump(temp, "./data/02origin_data_list.pkl")
# V = 1

# ----------------------------------------------------------------
# data = joblib.load("./data/03db_scan.pkl")
# temp = data.data.values.tolist()
# joblib.dump(temp, "./data/04db_scan_list.pkl")
# V = 1
# ----------------------------------------------------------------
# data = joblib.load("./data/04db_scan_list.pkl")
# dict = {}
# for i in range(len(data)):
#     try:
#         if data[i][2] not in dict[str(data[i][11])]:
#             dict[str(data[i][11])].append(data[i][2])
#     except KeyError:
#         dict[str(data[i][11])] = [data[i][2]]
#
# joblib.dump(dict, "./data/05classify_dict.pkl")
# V = 1
# ----------------------------------------------------------------
# data = joblib.load("./data/02origin_data_list.pkl")
# dict = joblib.load("./data/05classify_dict02.pkl")
#
# for i in range(len(data)):
#     data[i].append(dict[data[i][2]][0])
#
# joblib.dump(data, "./data/06data.pkl")
# V = 1
# ----------------------------------------------------------------
# data = joblib.load("./data/06data.pkl")
# temp = []
# for i in range(len(data)):
#     if data[i][13] != -1:
#         temp.append(data[i])
# joblib.dump(temp, "./data/07data_no-1.pkl")
# V = 1
# ----------------------------------------------------------------
# data = joblib.load("./data/07data_no-1.pkl")
#
# dict = {}
# for i in range(len(data)):
#     try:
#         dict[data[i][2]].append(data[i])
#     except KeyError:
#         dict[data[i][2]] = [data[i]]
#
# joblib.dump(dict, "./data/08data-dict.pkl")

# ----------------------------------------------------------------

# data = joblib.load("./data/08data-dict.pkl")
# clssify_dict = joblib.load("./data/05classify_dict.pkl")
# train_dict = {}
# test_dict = {}
# for i in clssify_dict:
#     if i == "-1":
#         continue
#     test = clssify_dict[i][:len(clssify_dict[i])*2//10]
#     train = clssify_dict[i][len(clssify_dict[i])*2//10:]
#     for j in train:
#         train_dict[j] = data[j]
#     for j in test:
#         test_dict[j] = data[j]
# # joblib.dump(train_dict, "./data/10train_data.pkl")
# # joblib.dump(test_dict, "./data/10test_data.pkl")
# V = 1
# # ----------------------------------------------------------------
# # data2 = joblib.load("./data/10train_data.pkl")
# data2 = joblib.load("./data/10test_data.pkl")
# for xx in (30, 40, 50, 60, 70, 80, 90, 100):
#     data = copy.deepcopy(data2)
#     n_sample = 15
#
#     def Percent(dat_list, per):
#         for i in dat_list:
#             length = len(dat_list[i])
#             dat_list[i] = dat_list[i][:int(length*per)]
#         return dat_list
#
#
#     def DownSample(data_list, n_sample):
#         temp = []
#         length = len(data_list)
#         for i in range(n_sample):
#             temp.append(data_list[(length * i) // n_sample])
#         return temp
#
#
#     def GuiOne(data_dict):
#         for i in data_dict:
#             max_x = max(data_dict[i])[11]
#             max_y = max(data_dict[i])[12]
#             max_angle = max(data_dict[i])[10]
#             min_x = min(data_dict[i])[11]
#             min_y = min(data_dict[i])[12]
#             min_angle = min(data_dict[i])[10]
#             for j in range(len(data_dict[i])):
#                 data_dict[i][j][11] = (data_dict[i][j][11] - min_x) / (max_x - min_x)
#                 data_dict[i][j][12] = (data_dict[i][j][12] - min_y) / (max_y - min_y)
#                 try:
#                     data_dict[i][j][10] = (data_dict[i][j][10] - min_angle) / (max_angle - min_angle)
#                 except ZeroDivisionError:
#                     A = data_dict[i]
#                     B = max(A)
#                     C = min(A)
#                     V = 1
#         return data_dict
#
#
#     data = Percent(data, xx/100)
#
#     # data = GuiOne(data)
#
#     dict = {}
#     for i in data:
#          dict[i]= DownSample(data[i], n_sample)
#
#     joblib.dump(dict, "./data/11test_downsample" + str(xx) + ".pkl")
#     # joblib.dump(dict, "./data/11train_downsample" + str(xx) + ".pkl")
#     # joblib.dump(dict, "./data/11train_downsample_toone" + str(xx) + ".pkl")
# ----------------------------------------------------------------
for xx in (30, 40, 50, 60, 70, 80, 90, 100):

    # dict = joblib.load("./data/11test_downsample" + str(xx) + ".pkl")
    dict = joblib.load("./data/11train_downsample" + str(xx) + ".pkl")
    svm_dict = {}
    for i in range(20):
        svm_dict[str(i)] = []

    for i in dict:
        id = dict[i][0][13]
        svm_dict[str(id)].append([])
        for j in range(len(dict[i])): # 15
            svm_dict[str(id)][-1].append(dict[i][j][11])
            svm_dict[str(id)][-1].append(dict[i][j][12])
            svm_dict[str(id)][-1].append(dict[i][j][10])

    # joblib.dump(svm_dict, "./data/12test"+ str(xx) +".pkl")
    joblib.dump(svm_dict, "./data/12train"+ str(xx) +".pkl")
    V = 1
