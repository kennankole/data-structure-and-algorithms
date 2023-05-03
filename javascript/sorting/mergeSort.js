const mergeSortAsc = (arr) => {
  if(arr.length > 1){
    let midPoint = Math.floor(arr.length / 2)
    let leftPart = arr.slice(0, midPoint);
    let rightPart = arr.slice(midPoint);
    mergeSortAsc(leftPart)
    mergeSortAsc(rightPart)
    let i = j = k = 0;
    while(i < leftPart.length && j < rightPart.length){
      if (leftPart[i] < rightPart[j]){
        arr[k] = leftPart[i];
        i += 1;
      }else{
        arr[k] = rightPart[j];
        j += 1;
      }
      k += 1;
    }
    while(i < leftPart.length){
      arr[k] = leftPart[i];
      i += 1;
      k += 1;
    }
    while(j < rightPart.length){
      arr[k] = rightPart[j];
      j += 1;
      k += 1;
    }
  }
  return arr
}

const mergeSortDesc = (arr) => {
  if (arr.length > 1){
    let midPoint = Math.floor(arr.length / 2);
    let leftPart = arr.slice(0, midPoint);
    let rightPart = arr.slice(midPoint);

    mergeSortDesc(leftPart);
    mergeSortDesc(rightPart);

    let i = j = k = 0;

    while(i < leftPart.length && j < rightPart.length){
      if(leftPart[i] > rightPart[j]){
        arr[k] = leftPart[i];
        i += 1;
      }else{
        arr[k] = rightPart[j];
        j += 1;
      }
      k += 1;
    }

    while(i < leftPart.length){
      arr[k] = leftPart[i];
      i += 1;
      k += 1;
    }

    while (j < rightPart.length){
      arr[k] = rightPart[j];
      j += 1;
      k += 1;
    }
  }
  return arr
}


let arr = [5, 3, 1, 2, 4]
console.log(mergeSortAsc(arr))
console.log(mergeSortDesc(arr))