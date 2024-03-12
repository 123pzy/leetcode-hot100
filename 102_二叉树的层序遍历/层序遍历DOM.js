/**
 * 补充一道好玩的题
 * 3. 按层遍历DOM树
 * <div id="root">
 *     <p>p1</p>
 *     <span>span1
 *         <span>span2</span>
 *     </span>
 *     <p>p2</p>
 *     <span>span3
 *         <span>span4</span>
 *     </span>
 * </div>
 *
 * traverse(document.querySelector('#root'))
 * // 结果用console.log()进行输出
 * // 上述表达式的输出结果为
 * // ['DIV']
 * // ['P', 'SPAN', 'P', 'SPAN']
 * // ['SPAN', 'SPAN']
 * function traverse (elRoot) {
 *   // 补充实现
 * }
 */
function traverse(e) {
    const ans = []
    if (!(e instanceof Element)) {
        console.log(ans);
        return
    }
    const dp = [e]
    while (dp.length > 0) {
        const len = dp.length
        const level = []
        for (var i = 0; i < len; i++) {
            const cur = dp.shift()
            level.push(cur.tagName)
            if (cur.children.length > 0) {
                for (var j of cur.children) {
                    dp.push(j)
                }
            }
        }
        console.log(level);
    }
}