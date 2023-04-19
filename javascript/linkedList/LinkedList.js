class Node{
	constructor(data, next=null){
		this.data = data;
		this.next = next;
	}
}

class LinkedList{
	constructor(){
		this.head = null;
	}

	insertAtTheBegining(data){
		let newNode = new Node(data)
		newNode.next = this.head;
		this.head = newNode;
	}

	insertAtTheEnd(data){
		let newNode = new Node(data)
		if(this.head){
			let currentNode = this.head
			while(currentNode.next){
				currentNode = currentNode.next
			}
			currentNode.next = newNode;
		}else{
			this.head = newNode;
		}
	}

    insertItemAfter(item, data){
			let newNode = new Node(data);
			let currentNode = this.head;
			while(currentNode){
				if(currentNode.data === item){
					break
				}
			currentNode = currentNode.next;
			}
			if(currentNode == null){
				console.log("No item in the list")
			}else{
				newNode.next = currentNode.next;
				currentNode.next = newNode;
			}
    }

    insertItemBefore(item, data){
			if(this.head == null){
				console.log("The list is empty")
			}
			if(this.head.data == item){
				let newNode = new Node(data)
				newNode.next = this.head;
				this.head = newNode;
			}
			let currentNode = this.head;
			while(currentNode.next){
				if(currentNode.next.data == item){
					break
				}
			currentNode = currentNode.next
			}
			if(currentNode.next == null){
				console.log("Item not in the list")
			}else{
				let newNode = new Node(data)
				newNode.next = currentNode.next;
				currentNode.next = newNode;
			}
    }

    insertAtIndex(index, data){
			if(index > 0){
				if(index == 1){
					let newNode = new Node(data);
					newNode.next = this.head;
					this.head = newNode;
				}else{
					let currentNode = this.head;
					let i = 1;
					while(i < index - 1 && currentNode != null){
						i+=1;
						currentNode = currentNode.next;
					}
					if(currentNode == null){
						console.log("Index out of range");
					}else{
						let newNode = new Node(data);
						newNode.next = currentNode.next;
						currentNode.next = newNode;
					}
				}
		}else{
			console.log(`${index} is invalid: index must be greator than zero`)
		}
	}
    
    getSize(){
			let count = 0;
			let currentNode = this.head;
			while(currentNode){
				count+= 1;
				currentNode = currentNode.next;
			}
			return count;
    }

    deleteItemAtStart(){
			if(this.head == null){
				console.log("The list is empty");
			}
			this.head = this.head.next;
    }

    deleteItemAtTheEnd(){
			if(this.head == null){
				console.log("The list is empty");
			}
			let currentNode = this.head;
			while(currentNode.next.next){
				currentNode = currentNode.next;
			}
			currentNode.next = null;
    }

    deleteItemByValue(item){
			// check if list is empty
			if(this.head == null){
				console.log("List is empty")
			}
			// check if the item is in the first Node 
			if(this.head.data === item){
				this.head = this.head.next;
			}
			// Check if item exists in susbsequent Nodes 
			let currentNode = this.head;
			while(currentNode.next){
				if(currentNode.next.data == item){
					break
				}
				currentNode = currentNode.next;
			}
			if(currentNode.next == null){
				console.log("Item does not exist")
			}else{
				currentNode.next = currentNode.next.next;
			}
    }
    display(){
			let currentHead = this.head
			while(currentHead){
				console.log(currentHead.data)
				currentHead = currentHead.next
			}
    }

    search(data){
			let currentNode = this.head; 
			while(currentNode){
				if(data === currentNode.data){
					return currentNode.data;
				}
				currentNode = currentNode.next;
			}
			return "Node not found";
    }

    reverseLinkedList(){
			let currentNode = this.head;
			let previousNode = null;

			while(currentNode != null){
				let nextNode = currentNode.next;
				currentNode.next = previousNode;
				previousNode = currentNode;
				currentNode = nextNode;
			}
			this.head = previousNode;
	}

    bubleSortDataExchange(){
			let end = null;
			while(end != this.head){
				let current_node = this.head;
				while(current_node.next != end){
					let q_node = current_node.next;
					if(current_node.data > q_node.data){
						[current_node.data, q_node.data] = [q_node.data, current_node.data];
					}
					current_node = current_node.next
				} 
				end = current_node;
			} 
	}
}


let one = new LinkedList();
one.insertAtTheBegining(60);
one.insertAtTheBegining(50);
one.insertAtTheEnd(5);
one.insertAtTheEnd(4);
one.insertItemAfter(60, 500)
one.insertItemBefore(5, 888);
one.bubleSortDataExchange();
one.display()





