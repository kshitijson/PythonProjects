import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

x = [0.40, 0.22, 0.35, 0.26, 0.08, 0.45]
y = [0.53, 0.38, 0.32, 0.19, 0.41, 0.30]
point = ['P1', 'P2', 'P3', 'P4', 'P4', 'P6']

data = pd.DataFrame({'Points': point, 'x': x, 'y': y})
data = data.set_index('Points')
print(data)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, c='r', marker='*')
for dt in data.itertuples():
    plt.annotate(dt.Index, (dt.x, dt.y))

plt.figure(figsize=(8, 5))
dend = sch.dendrogram(sch.linkage(data[['x', 'y']], method='single'), labels=data.index)
plt.show()