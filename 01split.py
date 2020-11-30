from sklearn.externals import joblib

# -------------------------------------------------------------------------------------------
# data = joblib.load("SB_data.pkl")
#
# names = locals()
# for i in range(20):
#     names['all_data_cluster' + str(i)] = data[data.cluster == i]
#     joblib.dump(names['all_data_cluster' + str(i)], 'all_data_cluster' + str(i) + '.pkl')

# -------------------------------------------------------------------------------------------
# names = locals()
# for i in range(20):
#     exec('data = joblib.load(\'./all_data/all_data_cluster' + str(i) + '.pkl\')')
#
#     len_data = len(data)//15
#     test_index = (len_data*2//10)*15
#
#     test = data[: test_index]
#     train = data[test_index:]
#
#     # joblib.dump(train, 'train_data_cluster' + str(i) + '.pkl')
#     # joblib.dump(test, 'test_data_cluster' + str(i) + '.pkl')
#     V = 1
# -------------------------------------------------------------------------------------------

# for k in range(20):
#     temp_train = joblib.load("./test/test_data_cluster" + str(k) + ".pkl")
#     # temp_train = joblib.load("./train/train_data_cluster" + str(k) + ".pkl")
#
#     all_feature = []
#     for i in range(len(temp_train)//15):
#         data = temp_train[i*15: i * 15 + 15]
#         X = data.x.tolist()
#         Y = data.y.tolist()
#         angle = data.track_unwrapped.tolist()
#
#         feature = []
#         for j in range(15):
#             feature.append(X[j])
#             feature.append(Y[j])
#             feature.append(angle[j])
#         all_feature.append(feature)
#     V = 1
#     # joblib.dump(all_feature, './testlist/test_data_cluster' + str(k) + '.pkl')
#     # joblib.dump(all_feature, './trainlist/train_data_cluster' + str(k) + '.pkl')
# -------------------------------------------------------------------------------------------
# train_dic = {}
# for i in range(20):
#     # data = joblib.load("./trainlist/train_data_cluster" + str(i) + ".pkl")
#     data = joblib.load("./testlist/test_data_cluster" + str(i) + ".pkl")
#     train_dic[str(i)] = data
# joblib.dump(train_dic, 'test.pkl')
# -------------------------------------------------------------------------------------------
# data = joblib.load("t_unwrapped.pkl")
#
# new_data = data.data[data.data.callsign == "CCM793N"]
# joblib.dump(new_data, "testdata-time.pkl")
# A = 1
# -------------------------------------------------------------------------------------------

# data = joblib.load("testdata-time.pkl")
#
# new_data = data[:90]
# joblib.dump(new_data, "testdata-time90.pkl")
# A = 1
# # # -------------------------------------------------------------------------------------------
# from traffic.drawing import CH1903
# projection = CH1903()
#
# data = joblib.load("t_unwrapped.pkl")
# data2 = joblib.load("testdata-time90.pkl")
# data.data = data2
# A = data.resample(15).eval(max_workers=1)
# resampled = A.compute_xy(projection)
#
# all_feature = []
#
# X = resampled.data.x.tolist()
# Y = resampled.data.y.tolist()
# angle = resampled.data.track_unwrapped.tolist()
#
# for i in range(15):
#     all_feature.append(X[i])
#     all_feature.append(Y[i])
#     all_feature.append(angle[i])
#
# data_dict ={}
# for i in range(20):
#     if i != 8:
#         data_dict[str(i)] = []
#     else:
#         data_dict[str(i)] = [all_feature]
#
# joblib.dump(data_dict, "demo90.pkl")
# # V = 1
# # # -------------------------------------------------------------------------------------------
data = joblib.load("demo100.pkl")
data["8"][0] = data["8"][0][0:30] + [0] * 15


V = 1
