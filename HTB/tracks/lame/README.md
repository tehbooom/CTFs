# LAME

## Too ez 4 me

nmap -sV -sC -p- 10.10.10.3 -oA nmap/lame

show thats port 21 is open but when i login with anonymous i get nothing. I use the vsftpd 2.3.4 exploit aginast it with no success

port 3632 is also open with a vulnerale distccd v1 however i also had no success with the exploit on this port since it prompted me for a user and i dont have any usernames. I could brute force this but i dont feel like it

samba is running 3.0.20 with an exploit called "username map script"  and requires no authentication!

Exploit was successful and got a root shell. Box was too easy.
