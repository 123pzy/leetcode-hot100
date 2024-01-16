挖了个坑，希望年底可以填上。

# 2024.1.6

![image-20240106205814268](http://panpan.dapanna.cn//image-20240106205814268.png)

# 1.6
第一题，两数之和
这道题首先想到了用回溯，用例过了但是提交超时，之后直接for循环暴力求解

# 1.16

[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj)

这题上次面字节考到了，链表的题目我不太会，这次算是开了一个链表学习的头。

[19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list?envType=featured-list&envId=2cktkvj?envType=featured-list&envId=2cktkvj)

这题主要就是建一个虚拟头节点，然后使用快慢指针，让快指针先走n步，当快指针走到最后一个节点的时候（right.next == None），慢指针此时正好在待删除节点的前一个，通过让此时慢指针指向倒数第n-1个节点的方式，删掉倒数第n个节点。
