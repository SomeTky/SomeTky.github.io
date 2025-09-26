# unordered_map

| 成员方法           | 功能描述                                                     | 用法示例                                                     |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **迭代器相关**     |                                                              |                                                              |
| begin()            | 返回指向容器中第一个键值对的正向迭代器。                     | `auto it = mymap.begin();`                                   |
| end()              | 返回指向容器中最后一个键值对之后位置的正向迭代器。           | `it != mymap.end();`                                         |
| cbegin()           | 与 begin () 相同，但返回的迭代器不能修改容器内容。           | `auto it = mymap.cbegin();`                                  |
| cend()             | 与 end () 相同，但返回的迭代器不能修改容器内容。             | `it != mymap.cend();`                                        |
| **容量相关**       |                                                              |                                                              |
| empty()            | 检查容器是否为空，为空返回 true，否则返回 false。            | `mymap.empty();`                                             |
| size()             | 返回当前容器中键值对的数量。                                 | `mymap.size();`                                              |
| max_size()         | 返回容器所能容纳键值对的最大数量，取决于系统实现。           | `mymap.max_size();`                                          |
| **元素访问**       |                                                              |                                                              |
| operator[key]      | 访问或插入指定键的值。若键不存在，会自动插入默认值。         | `string name = mymap[key];` `mymap[key2] = name;`            |
| at(key)            | 返回指定键对应的值，若键不存在则抛出 `out_of_range` 异常。   | `mymap.at(key) = value;`                                     |
| **查找操作**       |                                                              |                                                              |
| find(key)          | 查找键为 key 的键值对，存在则返回迭代器，否则返回 end ()。   | `mymap.find(key);`                                           |
| count(key)         | 返回键为 key 的键值对的数量（0 或 1，因为 unordered_map 不允许重复键）。 | `mymap.count(key);`                                          |
| equal_range(key)   | 返回包含两个迭代器的 pair，表示键为 key 的元素范围（适用于允许重复键的容器）。 | `mymap.equal_range(key);`                                    |
| **修改操作**       |                                                              |                                                              |
| emplace()          | 高效地插入键值对（如果键不存在）。                           | `mymap.emplace(key, value);`                                 |
| emplace_hint()     | 带位置提示的高效插入操作。                                   | `mymap.emplace_hint(pos, key, value);`                       |
| insert()           | 插入键值对或范围。                                           | `mymap.insert(pair<string,double>(key,value));` `mymap.insert({{key,value},{key2,value2}});` |
| erase()            | 删除指定键或迭代器位置的键值对。                             | `mymap.erase(key);`                                          |
| clear()            | 清空容器中的所有键值对。                                     | `mymap.clear();`                                             |
| swap()             | 交换两个同类型容器的内容。                                   | `mymap1.swap(mymap2);`                                       |
| **桶操作**         |                                                              |                                                              |
| bucket_count()     | 返回当前容器使用的桶的数量。                                 | `unsigned n = mymap.bucket_count();`                         |
| max_bucket_count() | 返回系统允许的最大桶数量。                                   | `mymap.max_bucket_count();`                                  |
| bucket_size(n)     | 返回第 n 个桶中存储的键值对数量。                            | `unsigned size = mymap.bucket_size(n);`                      |
| bucket(key)        | 返回键为 key 的元素所在的桶编号。                            | `unsigned bucket_num = mymap.bucket(key);`                   |
| **哈希策略**       |                                                              |                                                              |
| load_factor()      | 返回当前负载因子（键值对数 / 桶数）。                        | `float factor = mymap.load_factor();`                        |
| max_load_factor()  | 获取或设置最大负载因子。                                     | `mymap.max_load_factor(2.0);`                                |
| rehash(n)          | 设置桶的数量为 n，并重新哈希所有元素。                       | `mymap.rehash(20);`                                          |
| reserve(n)         | 预留至少能容纳 n 个元素的空间（调整桶数量）。                | `mymap.reserve(6);`                                          |
| **哈希函数**       |                                                              |                                                              |
| hash_function()    | 返回当前使用的哈希函数对象。                                 | `auto hash_fn = mymap.hash_function();`                      |

## 默认值

unordered_map使用[]访问时，如果键值不存在，会用类型的构造函数生成默认值。



# vector

## 访问最后一个元素

1. vector.back()直接返回最后一个元素的引用
2. 使用end迭代器-1：vector.end() - 1
3. 使用负偏移： vector.end()[-1]

# size()方法返回的是一个无符号整数

如果直接用vector.size() - 10，当vector.size()小于10时，会得到一个非常大的无符号整数。因此如果想用vector.size()来直接作减法时，建议先转换成int。

