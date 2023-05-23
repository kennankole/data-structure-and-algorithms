class Node {
  constructor(val, left=null, right=null){
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

const insert = (tree, value) => {
  if (tree === null) return new Node(value);
  else if (tree.val < value){
    tree.right = insert(tree.right, value);
  } else {
    tree.left = insert(tree.left, value);
  }
  return tree;
}

const find = (tree, target) => {
  if (tree.val === target) return true;
  else if (tree.val > value) return find(tree.right, target);
  else return find(tree.left, target);
}