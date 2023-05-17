const binarySearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1
  while(left <= right){
    let mid = left + Math.floor((right - left) / 2)
    if (arr[mid] === target) return arr[mid];
    if (arr[mid] < target){
      left = mid + 1
    }else{
      right = mid - 1
    }
  }
  return - 1
}

// let arr = [1, 3, 5, 7, 8]
// console.log(binarySearch(arr, 15))

const arraySum = (arr, target) => {
  let low = 0;
  let high = arr.length - 1;
  while (low < high){
    const two_sum = arr[low] + arr[high];
    if (two_sum === target){
      return [low, high]
    }else if(two_sum < target){
      low++;
    }else {
      high--;
    }
  }
}

// let arr1 = [2, 3, 4, 5, 8, 11, 18];
// console.log(arraySum(arr1, 8))

const subArray = (nums, k) => {
  let windowSum = 0;
  for(let i = 0; i < k; i++){
    windowSum = windowSum + nums[i]
    console.log(windowSum);
  }
  let largest = windowSum;
  for(let right = k; right < nums.length; right++){
    const left = right - k;
    windowSum = windowSum - nums[left];
    windowSum = windowSum + nums[right];
    largest = Math.max(largest, windowSum)
  }
  return largest;
}

console.log(subArray([1, 2, 3, 7, 4, 1], 3));