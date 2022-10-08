class array(): 
2 def init_(self): 
3 self.l=[i 
4 def insert_at_end ( self, list, value): 
5 1=list 
6 1.append(value) 
7 return 1 
8 def insert_at_beginning (self, 1ist, value) : 
9 1=list 
10 1.insert(0, value) 
11 return 1 
12 def insert_atmidd le (self , list, value, inde 
13 1=list 
14 1.insert(index, value) 
15 return l 
16 def to_count (self, list) :
17 1-list 
18 1.count(list) 
19 return 1 
20 def to_pop(self, list): 
21 1=list 
22 11=1.popPO 
23 return 11 
24 def to_sort(self, list) : 
25 1-list 
26 1.sort() 
27 return 1 
28 def to_find_length ( self, list) : 
29 1=list 
30 11=len(1) 
31 return 11 
32 def to_reverse(self, list): 
33 1=list 
34 1.reverse() 
35 return 1 
36 def to_display_thelist (self, list): 
37 1=list 
38 return 1 
39 def _to_clear( self , list) : 
40 1=list 
41 1.clear( 
42 return 1 
43 obj=array() 
44 list=[21,32,45,65,99,72, 33] 
45 while(list): 
46 print("1.insert at end") 
47 print("2.insert at beginning") 
48 print("3.insert at middle") 
49 print("4.to count the list") 
50 print("5.to pop the list") 
51 print("6.to sort the list") 
52 print("7.to find the length of the lis 
53 print("8.to reverse the list") 
54 print("9.display the list") 
55 print("10.clear the list")
56 print("11.PROGRAM EXIT") 
57 print("-----------------------------") 
58 choice= int(input("enter the choice"))
59 if choice==1:
60 value=int (""enter the value : ") 
61 result=obj. insert_at_end (1ist, valu 61 
62 print(result) 
63 elif choice==2: 
64 value=input ( "enter the value: ")
65 result=obj.insertat_beginning(list)
66 print(result) 
67 elif choice==3 : 
68 value=input ( "enter the value: ")
69 pos=int (input ( "enter the position : 
70 result=obj.insert_at_middle(list, 
71 print(result) 
72 elif choice==4: 
73 result=obj._to_count (list) 
74 print(result) 
75 elif choice==5 : 
76 result=obj._to_pop(list) 
77 print(result) 
78 elif choice==6: 
79 result=obj._to_sort(list) 
80 print(result) 
81 elif choice==7: 
82 result=obj.to_find_length (list) 
83 print(result) 
84 elif choice==8 : 
85 result-obj._to_reverse(list) 
86 print(result) 
87 elif choice==9: 
88 result-obj._to_display_thelist (lis 
89 print(result) 
90 elif choice==10: 
91 result=obj._to_clear (list) 
92 print(result) 
93 elif choice==11 : 
94 print("program exit")
95 break



1.insert at end 
2.insert at beginning 
3.insert at middle 
4.to count the list 
5.to pop the list 
6.to sort the list 
7.to find the length of the list 
8.to reverse the list 
9.display the list 
10.clear the list 
11.PROGRAM EXIT 
-------_----------------------------
enter the choice: 1 
enter the value: 4 
(21, 32, 45, 65, 99, 72, 33, '4'] 
1.insert at end 
2.insert at beginning 
3.insert at middle 
4.to count the list 
5.to pop the list 
6.to sort the list 
7.to find the length of the list 
8.to reverse the list 
9.display the list 
10.clear the list 
11.PROGRAM EXIT 
-===-=========-=====-=--===

enter the choice: 3 
enter the value: 2 
enter the position: 3 
[21, 32, 45, '2, 65, 99, 72, 33, '4'] 
1.insert at end 
2.insert at beginning 
3.insert at middle 
4.to count the list 
5.to pop the list 
6.to sort the list 
7.to find the length of the list 
8.to reverse the list 
9.display the list 
10.clear the list 
11.PROGRAM EXIT 
-----=--=---==--===--=-=-
enter the choice: 5 
4 
1.insert at end 
2.insert at beginning 
3.insert at middle 
4.to count the list 
5.to pop the list 
6.to sort the list 
7.to find the length of the list 
8.to reverse the list 
9.display the list 
10.clear the list 
11.PROGRAM EXIT 
=====--========


enter the choice: 8 
[33, 72, 99, 65, '2', 45, 32, 21] 
1.insert at end 
2.insert at beginning 
3.insert at middle 
4.to count the list 
5.to pop the list 
6.to sort the list 
7.to find the length of the list 
8.to reverse the list 
9.display the list 
10.clear the list 
11.PROGRAM EXIT 
-=== 
enter the choice: 11
