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
    insert(data){
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
        return false;
    }
}


let one = new LinkedList()
one.insert(50)
one.insert(90)
one.insert(40)

one.display()
console.log("break")
console.log(one.search(900));
