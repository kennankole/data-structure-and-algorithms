const bubbleSortAsc = (arr) => {
  let n = arr.length;
  for (let i = n - 1; i >= 0; i--){
    // The outer loop iterates in reverse, 
    // starting from the last element (n-1) 
    // and going down to the first element (0). 
    // This is optimization helps improve the algorithm's efficiency. 
    // In the worst case, if the array is already sorted, 
    // this modification can prevent unnecessary iterations.
    let swapped = false;
    for (let j = 0; j < i; j++){
      if (arr[j] > arr[j + 1]){
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) return arr;
  }
  return arr;
}


const bubbleSortDsc = (arr) => {
  let n = arr.length;
  for (let i = n - 1; i >= 0; i--){
    // The outer loop iterates in reverse, 
    // starting from the last element (n-1) 
    // and going down to the first element (0). 
    // This is optimization helps improve the algorithm's efficiency. 
    // In the worst case, if the array is already sorted, 
    // this modification can prevent unnecessary iterations.
    swapped = false;
    for (let j = 0; j < i; j++){
      if(arr[j] < arr[j+1]){
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true
      }
    }
    if(!swapped) return arr;
  }
  return arr;
}
console.log(bubbleSortAsc([5, 3, 1, 2, 4]));
console.log(bubbleSortDsc([5, 3, 1, 2, 4]));
