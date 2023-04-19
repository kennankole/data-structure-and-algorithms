
class BasicHashTable {
	constructor(){
		this.dataList = new Array(1024);
	}
	hash(key){
		let hash = 0;
		for (let y = 0; y < key.length; y++){
			hash = (hash + key.charCodeAt(y) * y) % this.dataList.length;
		}
		return hash;
	}

	set(key, value){
		const index = this.hash(key);
		if(!this.dataList[index]){
			this.dataList[index] = [];
		}
		this.dataList[index].push([key, value])
	}

	get(key){
		const index = this.hash(key)
		if (this.dataList[index]){
			for(let x = 0; x < this.dataList[index].length; x++){
				if(this.dataList[index][x][0] === key){
					return this.dataList[index][x][1]
				}
			}
		}
		return;
	}
}

const hashTable = new BasicHashTable()
hashTable.set("name", "John Doe");
console.log(hashTable.get("name"));
