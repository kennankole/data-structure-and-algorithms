const quickSortAsc = (arr) => {
  if((arr.length) <= 1) return arr;
  let midPoint = Math.floor(arr.length / 2);
  const pivot = arr[midPoint];
  let left = [];
  let right = [];
  for (let x = 0; x < arr.length; x++){
    if(arr[x] < pivot){
      left.push(arr[x])
    }
    else if(arr[x] > pivot){
      right.push(arr[x])
    }
  }
  return [...quickSortAsc(left), pivot, ...quickSortAsc(right)];
}

const quickSortDsc = (arr) => {
  if((arr.length) <= 1) return arr;
  let midPoint = Math.floor(arr.length /2);
  let pivot = arr[midPoint];
  let right = [];
  let left = [];
  for (let x = 0; x < arr.length; x++){
    if(arr[x] < pivot){
      left.push(arr[x])
    }
    else if(arr[x] > pivot){
      right.push(arr[x])
    }
  }
  return [...quickSortDsc(right), pivot, ...quickSortDsc(left)]
}
let arr = [5, 3, 1, 2, 4];
console.log(quickSortAsc(arr));
console.log(quickSortDsc(arr))