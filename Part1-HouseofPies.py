# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:22:51 2019

@author: Andre
"""

pie_nos_list= [1,2,3,4,5,6,7,8,9,10]
pienames_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
#Defining the order user interface

print('Welcome to the House of Pies !  Here are our pies: \n \n')
print('---------------------------------------------------------')
print('(1) Pecan, (2) Apple Crisp, (3) Bean), (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak')

pie_Orders=[]
pie_OrderNumber = int(input('Select the pie you would like by way of the pie number  '))
pie_Orders.append(pie_OrderNumber)
pie_name=pienames_list[pie_OrderNumber - 1]
print(f'Great! We will have that {pie_name} right out for you')

more_Orders = input('Would you like to make another pie purchase? Yes or No   ')
while more_Orders =='Yes':
    pie_OrderNumber = input('Select the pie you would like by way of the pie number  ')
    pie_Orders.append(int(pie_OrderNumber))
    pie_name=pienames_list[int(pie_OrderNumber)-1]
    print(f'Great! We will have that {pie_name} right out for you')
    more_Orders = input('Would you like to make another pie purchase? Yes or No    ')
    
pie_Orders.sort()

 
def countX(lst, x): 
   count = 0
   for ele in lst: 
       if (ele == x): 
           count = count + 1
   return count 
    

        
allpie=int(len(pie_nos_list))
orderpies=int(len(pie_Orders)) 
i=1
index=0
while i<=allpie:
    x= pie_nos_list[i-1]
    if x in pie_Orders:
       y=countX(pie_Orders,x)
       ind_pie_name=pienames_list[i-1]
       
    if orderpies>=0 and pie_Orders.count(x)!=0:
       ind_pie_name=pienames_list[i-1]
       
    if x not in pie_Orders:
       ind_pie_name=pienames_list[i-1]
       
       y=0
    print(f'{ind_pie_name} [{y}]')
    i=i+1            
                
            
       
