const selectionSortAsc = (arr) => {
  for(let i = 0; i < arr.length - 1; i++){
    let minIndex = i;
    for(let j = i; j < arr.length; j++){
      if (arr[j] < arr[minIndex]){
        minIndex = j;
      }
    }
    [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
  }
  return arr;
}


const selectionSortDesc = (arr) => {
  for(let i = 0; i < arr.length; i++){
    let minIndex = i;
    for (let j = i; j < arr.length; j++){
      if(arr[j] > arr[minIndex]){
        minIndex = j;
      }
    }
    [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
  }
  return arr
}
console.log(selectionSortAsc([5, 3, 1, 2, 4]));
console.log(selectionSortDesc([5, 3, 1, 2, 4]));