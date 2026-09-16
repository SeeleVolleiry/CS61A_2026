# Lab07: MUtable Trees

树是递归结构

# Q1：Maximum Path Sum（最大路径和）

跟以前的某道题很相似

任务：写函数，输入一棵树，返回从根到某个叶子的任意路径上值的最大总和。

示例：t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
max_path_sum(t) → 11（路径 1→10）
测试：python3 ok -q max_path_sum

# Q2：Add Leaves（按深度加叶子）

任务：
    实现 add_d_leaves(t, v)。定义节点深度 = 从根到该节点的边数（根深度为 0）。
    该函数对深度为d的节点添加d个子节点，每个子节点的值为v。

对每个节点：
    加 d 片叶子，d = 该节点的深度；每片叶子 label 都是 v
    若该深度节点已有 branches，把新叶子加到该列表末尾
    例：深度 1 的节点各加 1 片叶子、深度 2 加 2 片…

两条 Hint（重要）：

    用一个辅助函数追踪 depth
    小心添加时机：新叶子只加给"原始节点"，不要加给那些刚被加进来的节点。也就是说先给子树添加节点。

# Q3：Has Path（路径拼词）

任务：输入 Tree t 和字符串 target，若存在一条从根出发、沿途 label 正好拼出 target 的路径则返回 True，否则 False。可假定每个节点 label 恰好是一个字符。

说明：这种结构叫 trie（前缀树），常见应用如自动补全

示例树 greetings（h→i 和 h→e→y / h→e→l→l→o）：
'h' → True、'i' → False（不从根出发）
'hi' → True、'hello' → True、'hey' → True
'bye' → False、'hint' → False
测试：python3 ok -q has_path

# Q4：Preorder（前序遍历）

任务：返回一个列表，包含树里所有 label，顺序与打印树时出现的顺序一致。

这种顺序叫 preorder traversal（前序遍历）

示例：树 8→[2, 9→[4,5], 6→[7]]，输出 [8, 2, 9, 4, 5, 6, 7]

# Q5：Level Mutation Link（按层用链表函数改标签）填空题

任务：给定树 t 和一个单参函数链表 funcs，用 funcs 里对应深度的函数去就地修改（mutate） t 的每个 label。

    根节点（深度 0）用 funcs.first 改；第一层用 funcs.rest.first；依此类推
    特殊情况：某个节点是叶子、而 funcs 里还有剩余函数 → 把剩余函数按顺序依次作用到该叶子节点 label 上
    funcs 为空 → 树保持原样