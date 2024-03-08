function solution(nodeinfo) {
  for(var i = 0; i < nodeinfo.length; i++) {
    nodeinfo[i][2] = i + 1 // idx 값을 삽입함.
  }

  function recur(nodes, thisnode) {
    // 노드가 비었으면 종료
    if(nodes.length === 0) return;
    // y 좌표로 높은순으로
    nodes.sort((a,b)=>b[1] -a[1])
    // console.log(nodes)
    var high = nodes.shift()
    // console.log(high);

    // console.log(thisnode)
    // high 에 대해 노드생성
    thisnode.val = high[2] // 3번째 요소가 idx

    var splitter_x = high[0]
    // 가장높은것의 x 기준으로 좌우 분리
    var lefts = nodes.filter(n=> n[0] < splitter_x)
    // console.log(lefts)
    var rights = nodes.filter(n=> n[0] > splitter_x)
    // console.log(rights)

    thisnode.left = recur(lefts, {})
    thisnode.right = recur(rights, {})

    return thisnode
  }

  // dfs 만든 트리 head
  var head = recur(nodeinfo, {})

  // console.log(head)

  // 전위
  var preOrder = []
  var dfsPre = function(n) {
    if(!n) return;
    preOrder.push(n.val)
    dfsPre(n.left)
    dfsPre(n.right)
  }

  // 후위
  var postOrder = []
  var dfsPost = function(n) {
    if(!n) return;
    dfsPost(n.left)
    dfsPost(n.right)
    postOrder.push(n.val)
  }

  dfsPre(head)
  dfsPost(head)

  return [preOrder, postOrder]
}