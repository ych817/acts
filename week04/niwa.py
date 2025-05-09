from ckanapi import RemoteCKAN
import pandas as pd

# 1. 连接到 DataHub（基于 CKAN）
ckan = RemoteCKAN('https://data.niwa.co.nz')

# 2. 搜索 “Climate station data (daily)” 数据集
result = ckan.action.package_search(q='Climate station data (daily)')
print(f"Found {result['count']} matching datasets.")
if result['count'] > 0:
    dataset = result['results'][0]
    print(f"Dataset title: {dataset['title']}")
    # 3. 列出所有资源
    for r in dataset['resources']:
        print(f"- {r['name']} ({r['format']}) -> {r['url']}")
    # 4. 找到 CSV 资源并下载到 pandas
    csv_res = next(r for r in dataset['resources'] if r['format'].lower() == 'csv')
    df = pd.read_csv(csv_res['url'])
    print(df.head())
else:
    print("No dataset found.")