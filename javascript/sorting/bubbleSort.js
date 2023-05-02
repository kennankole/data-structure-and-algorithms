const bubbleSortAsc = (arr) => {
  let n = arr.length;
  for (let i = n - 1; i >= 0; i--){
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