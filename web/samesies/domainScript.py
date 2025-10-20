#!/usr/bin/exec-suid -- /usr/bin/python3
import sys
sys.path.append('/challenge')

if __name__ == '__main__':
    with open("/etc/hosts", "a+") as f:
        text = f.read()
        if "minnetonka" not in text:
            f.write("127.0.0.1:5000\tminnetonkatriplets.ctf")
        
