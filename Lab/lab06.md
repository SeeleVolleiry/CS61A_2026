# Lab06: OOP

# Q1：Bank Account（银行账户）

扩展 BankAccount 类，新增 transactions 属性——一个记录每次交易的列表。

关键要求：

    每次调用 deposit 或 withdraw，都要新建一个 Transaction 实例并加入列表，即使交易未成功（如余额不足）也要记录：

        第一想法是，监控函数的调用。只要这两个函数被调用了，就根据结果创建一个Transaction的实例加入账户的transactions列表。
        但是，根据教学的知识，似乎没有这样的监控方法。那么办呢？
        之间的想法实在取款或存款结束后再，单独写一个函数来完成该功能。
        为什么不在取款或存款的同时就完成呢？把交易记录的创建就写进存取的函数中。

    新增一个属性：

        属性由__init__方法初始化。

Transaction 属性：
    before：交易前的余额
    after：交易后的余额
    id：该账户此前的交易次数（同一 BankAccount 内的 id 必须唯一，跨账户不必唯一）

Transaction 方法：
    changed() → before != after 返回 True，否则 False
    report() → 返回描述字符串

# Q2：Email（邮件系统）

三个类组成一个邮件系统：Email、Server、Client。

    Client 能用 compose 写邮件，并用 send 发给 Server

    Server 用它内部的字典 clients（键为客户端名字 → 值为 Client 实例）把邮件投递到目标 Client 的 inbox
        前提假设：一个 Client 不会更换它用的 Server，只能通过该 Server 发邮件
    
    Email 类已完整给出，无需改动

补全剩余的代码，关键是在弄清楚三个类之间的关系、每个类的参数的含义和类型。

Important: 
    Before you start, make sure you read the entire code snippet to understand the relationships between the classes, and pay attention to the parameter type of the methods.
    
    Think about what variables you have access to in each method and how can you use them to access the other classes and their methods.

Note:

    The sender parameter from the __init__(self, msg, sender, recipient_name) method in the Email class is a Client instance.
    The client parameter from the register_client(self, client) method in the Server class is a Client instance.
    The email parameter from the send(self, email) method in the Server class is an Email instance.


# Q3：Mint（铸币厂）

实现一个 Mint 类，输出带正确年份和面值的硬币；涉及继承（Nickel、Dime 是 Coin 的子类）。

关键要求：

    每个 Mint 实例有 year 印章；update 方法把实例的 year 设为 Mint 类的 present_year 类属性
    create 方法的参数是 Coin 的子类（不是实例），返回该子类的一个实例，盖上该 Mint 的 year（若没 update，年份可能与 present_year 不同）
    Coin.worth 返回：cents 面值 + 每超过 50 岁的年份加 1 分。年龄 = Mint.present_year - coin.year