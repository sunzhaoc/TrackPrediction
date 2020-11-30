from traffic.data.samples import switzerland
import matplotlib.pyplot as plt
from traffic.core.projection import CH1903
from traffic.drawing import countries

from sklearn.cluster import DBSCAN
from sklearn import svm

from sklearn.preprocessing import StandardScaler
# from traffic.core.projection import CH1903
from sklearn.mixture import GaussianMixture

# from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from traffic.core.projection import CH1903

from itertools import islice, cycle
# from traffic.drawing import countries

from random import sample
from traffic.data import airports, airways, navaids
from traffic.drawing import CH1903, countries, lakes
from traffic.drawing.markers import rotate_marker, atc_tower, aircraft

from sklearn.externals import joblib

## 瑞士地图上的完整轨迹数据
# with plt.style.context("traffic"):
#     ax = plt.axes(projection=CH1903())
#     ax.add_feature(countries())
#     switzerland.plot(ax, alpha=0.1)
#     plt.show()
#
# # 在轨迹上进行聚类时，通常使用轨迹角非常重要
# # t_unwrapped = switzerland.assign_id().unwrap().eval (max_workers=4)
t_unwrapped = switzerland.assign_id().unwrap().eval()     # 已修改

# joblib.dump(t_unwrapped, "t_unwrapped.pkl")
# DBSCAN聚类预测
# t_dbscan = t_unwrapped.clustering(nb_samples=15, projection=CH1903(), features=["x", "y", "track_unwrapped"], clustering=DBSCAN(eps=0.5, min_samples=10), transform=StandardScaler()).fit_predict()

# data = joblib.load("testdata-time.pkl")
t_dbscan = t_unwrapped.clustering(
    nb_samples=15,
    projection=CH1903(),
    features=["x", "y", "track_unwrapped"],
    # features=["latitude", "longitude", "track_unwrapped"],
    # features=["track_unwrapped"],
    # clustering=DBSCAN(eps=0.5, min_samples=10),
    clustering=DBSCAN(eps=0.5, min_samples=10),
    transform=StandardScaler(),
).fit_predict()

joblib.dump(t_dbscan, "./data/03db_scan.pkl")
# data = t_dbscan.data[t_dbscan.data.callsign == "CCM793N"]
# joblib.dump(data, "testdata-time.pkl")
# 高斯混合模型聚类预测
# t_gmm = t_unwrapped.clustering(
#     nb_samples=15,
#     projection=CH1903(),
#     features=["x", "y", "track_unwrapped"],
#     clustering=GaussianMixture(n_components=19),
#     transform=StandardScaler(),
# ).fit_predict()
# joblib.dump(t_dbscan, 'SB-cluster.pkl')


# # 画图
# n_clusters = 1 + t_dbscan.data.cluster.max()
# # -- dealing with colours --
# color_cycle = cycle(
#     "#a6cee3 #1f78b4 #b2df8a #33a02c #fb9a99 #e31a1c "
#     "#fdbf6f #ff7f00 #cab2d6 #6a3d9a #ffff99 #b15928".split()
# )
# colors = list(islice(color_cycle, n_clusters))
# colors.append("#aaaaaa")  # color for outliers, if any
# # -- dealing with the grid --
# nb_cols = 3
# nb_lines = (1 + n_clusters) // nb_cols + (((1 + n_clusters) % nb_cols) > 0)
#
# with plt.style.context("traffic"):
#     fig, ax = plt.subplots(
#         nb_lines, nb_cols, figsize=(10, 15), subplot_kw=dict(projection=CH1903())
#         # nb_lines, nb_cols, figsize=(30, 45), subplot_kw=dict(projection=CH1903())
#     )
#     for cluster in range(-1, n_clusters):
#     # for cluster in range(-1, 0):
#         ax_ = ax[(cluster + 1) // nb_cols][(cluster + 1) % nb_cols]
#         ax_.add_feature(countries())
#
#         t_dbscan.query(f"cluster == {cluster}").plot(
#             ax_, color=colors[cluster], alpha=0.1 if cluster == -1 else 1
#         )
#         ax_.set_global()
#         print(cluster)
# plt.show()
