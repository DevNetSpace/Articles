import paramiko
import time
import getpass



def main ():
    #provide credentials
    login = input("Username:")
    password = getpass.getpass("Password for " + login + ":")
    list_of_ips = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
    for ip in list_of_ips:
       try:
           remote_conn_pre = paramiko.SSHClient()
           remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           remote_conn_pre.connect(ip, username=login,
                                   password=password,
                                   look_for_keys=False, allow_agent=False)
           remote_conn = remote_conn_pre.invoke_shell()
           remote_conn.send('\n')
           remote_conn.send('terminal length 0')
           remote_conn.send('\n')
           time.sleep(2)
           remote_conn.send("sh ip int br")
           remote_conn.send('\n')
           remote_conn.recv(10000).decode("utf-8")
           time.sleep(10)
       except:
           print ("I cannot connect to device:" + ip)
           continue

if __name__ == "__main__":
    main()