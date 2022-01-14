# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:29:38 2022

@author: joeeb
"""

#Circular Doubly Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        
    
    #Insertion method in circular doubly linked list
    def insertionCDLL(self, nodeValue, location):
        if self.head is None:
            print("The CDLL does not exist")
        
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            
            elif location == 1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode
    
    #Traversal metod to traverse the CCLL
    def traversalCDLL(self):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next
    
    #Traversal metod to reverse traverse the CCLL
    def revtraversalCDLL(self):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev
    
    #Search method
    def searchCDLL(self, target):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            node = self.head
            while node:
                if node.value == target:
                    print("The value is found")
                    break
                elif node == self.tail:
                    print("The value does not exist")
                    break
                node = node.next
    
    #Deletion method for deletion from 
    def deleteCDLL(self, location):
        if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail.next = self.head.next
                    self.head = self.head.next
                    self.head.prev = self.tail
        elif location == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            tempNode = self.head
            index = 0
            while index < location -1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
            nextNode.next.prev = tempNode
     
    #Delete entire CDLL
    def Deletion(self):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("Deleted the CDLL")
            




           
circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)

circularDLL.insertionCDLL(0, 0)
circularDLL.insertionCDLL(1, 1)
circularDLL.insertionCDLL(2, 1)

circularDLL.traversalCDLL()
circularDLL.revtraversalCDLL()

circularDLL.searchCDLL(55)


circularDLL.deleteCDLL(0)
circularDLL.deleteCDLL(1)

circularDLL.Deletion()

print([node.value for node in circularDLL])                    
                
    
    
