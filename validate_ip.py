class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(IP) <= 15 and "." in IP:
            l= []
            l = IP.split(".")
            c=0
            l2=['1','2','3','4','5','6','7','8','9','0']
            for i in l:
                if i.isdigit() and int(i) <=255 :
                    if len(i) > 1 and i[0] == "0":
                        c = 0
                    else:
                        c+=1
                    
                else:
                    c=0 
            if c==4 and IP.count(".")==3:
                return "IPv4"
            else:
                return "Neither"
                    
        elif ":" in IP :
            l1 = []
            l1= IP.split(":")
            c= 0
            for i in l1:
                try:
                    k =int(i,16)
                except:
                    k = "adasd"
                k1 = str(k)
                if k1.isdigit() and len(i)<=4 and i[0]!="-":
                    c+=1
                else:
                    c=0
            if c == 8 :
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
