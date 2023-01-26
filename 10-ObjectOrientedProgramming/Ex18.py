# The Contact class contains the 'name', 'email' and 'telephone' fields enabling the description of a single contact on a smartphone.
# The Contact_List class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:
#     a.	Adds a new contact
#     b.	Displays the contact list

# Write a program consisting of 3 files (smartphone.py -> Ex18.py, contact.py, contact_list.py).
# In the mail (?main) program (smartphone.py) create an object representing a contact list and add the following people data:
#     John Brown     brown@onet.pl       555234000
#     Anna May   	 am@o2.pl            232000199
#     George Small   smallg@google.pl    222999100
#     Paola Big      bigpaola@poczta.pl  100200300
# Then display the contact list available on the smartphone.

import contact
import contact_list

l = contact_list.Contact_List()
l.add(contact.Contact("John Brown", "brown@onet.pl", 555234000))
l.add(contact.Contact("Anna May", "am@o2.pl", 232000199))
l.add(contact.Contact("George Small", "smallg@google.pl", 222999100))
l.add(contact.Contact("Paola Big", "bigpaola@poczta.pl", 100200300))
l.display()