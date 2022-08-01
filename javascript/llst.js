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


let one = new LinkedList();
one.insertAtTheBegining(60);
one.insertAtTheBegining(50);
one.display();
console.log("---++++++-----");
one.insertAtTheEnd(5);
one.insertAtTheEnd(4);
one.display();
console.log("---++++++-----");
one.insertItemAfter(150, 500)
one.display();
console.log("---++++++-----");
