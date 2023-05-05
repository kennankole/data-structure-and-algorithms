const binarySearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1
  while(left <= right){
    let mid = Math.floor((left + right) / 2)
    if (arr[mid] === target) return arr[mid];
    if (arr[mid] < target){
      left = mid + 1
    }else{
      right = mid - 1
    }
  }
  return - 1
}

let arr = [1, 3, 5, 7, 8]
console.log(binarySearch(arr, 15))