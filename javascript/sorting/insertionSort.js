const insertionSortAsc = (arr) => {
  for (let i = 0; i < arr.length; i++){
    currentIndex = i;
    while(currentIndex > 0 && arr[currentIndex] < arr[currentIndex - 1]){
      temp = arr[currentIndex];
      arr[currentIndex] = arr[currentIndex - 1];
      arr[currentIndex - 1] = temp;
      currentIndex -= 1
    }
  }
  return arr
}
const arr = [5, 3, 1, 2, 4]
console.log(insertionSortAsc(arr))