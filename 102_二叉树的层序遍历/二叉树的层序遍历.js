/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    ans = []
    if (!root) {
        return ans
    } else {
        const deque = [root]
        while (deque.length != 0) {
            level = []
            len = deque.length
            for (var i = 0; i < len; i++) {
                var cur = deque.shift()
                level.push(cur.val)
                if (cur.left) {
                    deque.push(cur.left)
                }
                if (cur.right) {
                    deque.push(cur.right)
                }
            }
            ans.push(level)
        }
        return ans
    }
};