FasdUAS 1.101.10   ��   ��    k             l     ��������  ��  ��        l      �� 	 
��   	$
set tid to AppleScript's text item delimiters

set t to the clipboard
set l to paragraphs of t

repeat with i from 1 to count of l
	if item i of l = "" then
		set item i of l to return
	else
		set item i of l to (item i of l) & " "
	end if
end repeat

set the clipboard to l as string
    
 �  < 
 s e t   t i d   t o   A p p l e S c r i p t ' s   t e x t   i t e m   d e l i m i t e r s 
 
 s e t   t   t o   t h e   c l i p b o a r d 
 s e t   l   t o   p a r a g r a p h s   o f   t 
 
 r e p e a t   w i t h   i   f r o m   1   t o   c o u n t   o f   l 
 	 i f   i t e m   i   o f   l   =   " "   t h e n 
 	 	 s e t   i t e m   i   o f   l   t o   r e t u r n 
 	 e l s e 
 	 	 s e t   i t e m   i   o f   l   t o   ( i t e m   i   o f   l )   &   "   " 
 	 e n d   i f 
 e n d   r e p e a t 
 
 s e t   t h e   c l i p b o a r d   t o   l   a s   s t r i n g 
      l     ��������  ��  ��        l     ����  O         k           r    
    4    �� 
�� 
cfol  m       �   � M a c i n t o s h   H D : U s e r s : s m a r g h e i m : D o c u m e n t s : C L A S S I C S : S t u d y   M a t e r i a l s :  o      ���� 0 
folderpath 
folderPath   ��  r        c        n       !   4    �� "
�� 
file " m    ����  ! o    ���� 0 
folderpath 
folderPath  m    ��
�� 
alis  o      ���� 0 x  ��    m      # #�                                                                                  MACS  alis    t  Macintosh HD               ����H+  ҍK
Finder.app                                                     ԲY�`�        ����  	                CoreServices    ���*      �`D    ҍKҍHҍG  6Macintosh HD:System: Library: CoreServices: Finder.app   
 F i n d e r . a p p    M a c i n t o s h   H D  &System/Library/CoreServices/Finder.app  / ��  ��  ��     $ % $ l     ��������  ��  ��   %  & ' & l     ��������  ��  ��   '  ( ) ( l      �� * +��   *.(
set theSubject to fileName
set theBody to "Hello sir. Here is my " & fileName
set theAddress to "Some Email"
set theAttachment to theFile
set theSender to "Some Sender"

tell application "Mail"
	set theNewMessage to make new outgoing message with properties {subject:theSubject, content:theBody & return & return, visible:true}
	tell theNewMessage
		set visibile to true
		set sender to theSender
		make new to recipient at end of to recipients with properties {address:theAddress}
		try
			make new attachment with properties {file name:theAttachment} at after the last word of the last paragraph
			set message_attachment to 0
		on error errmess -- oops
			log errmess -- log the error
			set message_attachment to 1
		end try
		log "message_attachment = " & message_attachment
		#send
	end tell
end tell
    + � , ,P 
 s e t   t h e S u b j e c t   t o   f i l e N a m e 
 s e t   t h e B o d y   t o   " H e l l o   s i r .   H e r e   i s   m y   "   &   f i l e N a m e 
 s e t   t h e A d d r e s s   t o   " S o m e   E m a i l " 
 s e t   t h e A t t a c h m e n t   t o   t h e F i l e 
 s e t   t h e S e n d e r   t o   " S o m e   S e n d e r " 
 
 t e l l   a p p l i c a t i o n   " M a i l " 
 	 s e t   t h e N e w M e s s a g e   t o   m a k e   n e w   o u t g o i n g   m e s s a g e   w i t h   p r o p e r t i e s   { s u b j e c t : t h e S u b j e c t ,   c o n t e n t : t h e B o d y   &   r e t u r n   &   r e t u r n ,   v i s i b l e : t r u e } 
 	 t e l l   t h e N e w M e s s a g e 
 	 	 s e t   v i s i b i l e   t o   t r u e 
 	 	 s e t   s e n d e r   t o   t h e S e n d e r 
 	 	 m a k e   n e w   t o   r e c i p i e n t   a t   e n d   o f   t o   r e c i p i e n t s   w i t h   p r o p e r t i e s   { a d d r e s s : t h e A d d r e s s } 
 	 	 t r y 
 	 	 	 m a k e   n e w   a t t a c h m e n t   w i t h   p r o p e r t i e s   { f i l e   n a m e : t h e A t t a c h m e n t }   a t   a f t e r   t h e   l a s t   w o r d   o f   t h e   l a s t   p a r a g r a p h 
 	 	 	 s e t   m e s s a g e _ a t t a c h m e n t   t o   0 
 	 	 o n   e r r o r   e r r m e s s   - -   o o p s 
 	 	 	 l o g   e r r m e s s   - -   l o g   t h e   e r r o r 
 	 	 	 s e t   m e s s a g e _ a t t a c h m e n t   t o   1 
 	 	 e n d   t r y 
 	 	 l o g   " m e s s a g e _ a t t a c h m e n t   =   "   &   m e s s a g e _ a t t a c h m e n t 
 	 	 # s e n d 
 	 e n d   t e l l 
 e n d   t e l l 
 )  - . - l     ��������  ��  ��   .  / 0 / l     ��������  ��  ��   0  1 2 1 l    3���� 3 r     4 5 4 I   �� 6��
�� .rdwropenshor       file 6 4    �� 7
�� 
alis 7 m     8 8 � 9 9 ( H F S : P a t h : T o : F i l e . t x t��   5 o      ���� 0 y  ��  ��   2  : ; : l    ' <���� < r     ' = > = I    %�� ?��
�� .rdwrread****        **** ? o     !���� 0 y  ��   > o      ���� 0 x  ��  ��   ;  @ A @ l  ( - B���� B I  ( -�� C��
�� .rdwrclosnull���     **** C o   ( )���� 0 y  ��  ��  ��   A  D E D l     ��������  ��  ��   E  F G F l     ��������  ��  ��   G  H I H l     ��������  ��  ��   I  J K J l     ��������  ��  ��   K  L M L l     ��������  ��  ��   M  N�� N l  . � O���� O O   . � P Q P k   2 � R R  S T S r   2 5 U V U m   2 3 W W � X X ( r i c h h a @ s a s . u p e n n . e d u V o      ���� 
0 hannah   T  Y Z Y r   6 ; [ \ [ m   6 7 ] ] � ^ ^ * n i t i . b a g c h i @ g m a i l . c o m \ o      ���� 0 niti   Z  _ ` _ r   < C a b a m   < ? c c � d d 4 s t e p h e n . m a r g h e i m @ g m a i l . c o m b o      ���� 0 stephen   `  e f e r   D j g h g I  D f���� i
�� .corecrel****      � null��   i �� j k
�� 
kocl j m   H K��
�� 
bcke k �� l��
�� 
prdt l K   N ` m m �� n o
�� 
subj n m   Q T p p � q q  T e s t   S u b j e c t o �� r s
�� 
ctnt r o   W X���� 0 x   s �� t��
�� 
pvis t m   [ \��
�� boovfals��  ��   h o      ���� 0 thenewmessage theNewMessage f  u�� u O   k � v w v k   q � x x  y z y I  q ����� {
�� .corecrel****      � null��   { �� | }
�� 
kocl | m   u x��
�� 
trcp } �� ~ 
�� 
insh ~ n   { � � � �  ;   � � � 2  { ���
�� 
trcp  �� ���
�� 
prdt � K   � � � � �� ���
�� 
radd � o   � ����� 0 stephen  ��  ��   z  ��� � I  � �������
�� .emsgsendnull���     bcke��  ��  ��   w o   k n���� 0 thenewmessage theNewMessage��   Q m   . / � ��                                                                                  emal  alis    F  Macintosh HD               ����H+  ҍmMail.app                                                       �JE΄��        ����  	                Applications    ���*      ΄��    ҍm  #Macintosh HD:Applications: Mail.app     M a i l . a p p    M a c i n t o s h   H D  Applications/Mail.app   / ��  ��  ��  ��       �� � ���   � ��
�� .aevtoappnull  �   � **** � �� ����� � ���
�� .aevtoappnull  �   � **** � k     � � �   � �  1 � �  : � �  @ � �  N����  ��  ��   �   � " #�� �������� 8�������� � W�� ]�� c���������� p��������������~�}�|
�� 
cfol�� 0 
folderpath 
folderPath
�� 
file
�� 
alis�� 0 x  
�� .rdwropenshor       file�� 0 y  
�� .rdwrread****        ****
�� .rdwrclosnull���     ****�� 
0 hannah  �� 0 niti  �� 0 stephen  
�� 
kocl
�� 
bcke
�� 
prdt
�� 
subj
�� 
ctnt
�� 
pvis�� �� 
�� .corecrel****      � null�� 0 thenewmessage theNewMessage
� 
trcp
�~ 
insh
�} 
radd
�| .emsgsendnull���     bcke�� �� *��/E�O��k/�&E�UO*��/j E�O�j 
E�O�j O� i�E�O�E` Oa E` O*a a a a a a �a fa a  E` O_  )*a a a *a -6a a  _ la  O*j !UUascr  ��ޭ