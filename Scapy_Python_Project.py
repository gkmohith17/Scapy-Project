#code to analyse a pcap file of packets and analyse the traffic to visualise different network parameters and plot a graph in the default web browser. 

from collections import Counter
from scapy.all import*
import plotly.graph_objects as go
import os
    
def user_choice(choice,packets):
    if choice == 1:
        plot_ip_src(packets)
    if choice == 2:
        plot_ip_dst(packets)
    if choice == 5:
        plot_ether_hwsrc(packets)
    if choice == 8:
        plot_dport_port(packets)
    if choice == 10:
        plot_arp_src(packets)   
    if choice == 12:
        plot_ether_type(packets)
    if choice == 9:
        plot_udp_len(packets)
    if choice == 11:
        plot_tcp_window(packets)
    if choice == 6:
        plot_ether_hwdst(packets)
    if choice == 3:
        plot_ip_len(packets)
    if choice == 4:
        plot_ip_ttl(packets)
    if choice == 7:
        plot_sport_port(packets)
    if choice == 13:
        plot_ip_version(packets)
    else:
        print("Wrong Choice")

def plot_ip_src(packets):
    srcIP=[]
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].src)
            except:
                pass
#collect the data and store in the most occured values in the dictonary
    cnt=Counter(srcIP)
    xData=list(cnt.keys())
    yData=list(cnt.values())
#take the two keys and values and store them in two list to plot
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
#if the option chosen in among the above six , plot the grpahy use plotly 
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='IP Source Occurence ',xaxis_title='IP Source Address',yaxis_title='Count',\
        paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
#show the figure in the website default in the user computer
        fig.show()
#the code is same but repeated by changing the values of the option chosen according to the parameter
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Line Chart of IP Source Occurence',xaxis_title='IP Source Address',yaxis_title='Count',\
        plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='IP Source Occurrence Pie Graph',paper_bgcolor='peachpuff')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='IP Source Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='IP Source Occurrence Sunburst Graph')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='IP Source Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()

def plot_ip_dst(packets):
    dstIP=[]
    for pkt in packets:
        if IP in pkt:
            try:
                dstIP.append(pkt[IP].dst)   
            except:
                pass
    cnt = Counter(dstIP)
    xData = list(cnt.keys())
    yData = list(cnt.values()) 
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='IP Destination Occurence ',xaxis_title='IP Destination',\
        yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Line Chart of IP Destination Occurence',xaxis_title='IP Destination',yaxis_title='Count',\
        paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='IP Destination Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='IP Destination Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='IP Destination Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='IP Destination Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()

def plot_ether_hwsrc(packets):
    s=[]
    for pkt in packets:
        if Ether in pkt:
            try:
                s.append(pkt[Ether].hwsrc)
            except:
                pass
    cnt=Counter(s)
    xData=list(cnt.keys())
    yData=list(cnt.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='Sender Hardware Address Occurence Bar Graph',xaxis_title='Sender Hardware Address',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Sender Hardware Address Occurence Line Graph',xaxis_title='Sender Hardware Address',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='IP Source Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Sender Hardware Address Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='Sender Hardware Address Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Sender Hardware Address 3-D Graph',paper_bgcolor='lightgray')
        fig.show()

def plot_dport_port(packets):
    counttt=0
    s=[]
    for pkt in packets:
        if TCP in pkt:
            try:
                s.append(pkt[TCP].dport)
                counttt +=1
            except:
                pass
    cnt= Counter(s) 
    xData = list(cnt.keys())
    yData = list(cnt.values()) 
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='Destination Port Occurence Bar Graph',xaxis_title='Destination Port',\
        yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title=' Destination Port Occurence',xaxis_title='Destination Port',yaxis_title='Count',\
        paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='Destination Port Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Destination Port Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='Destination Port Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Destination Port Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()

def plot_arp_src(packets):
    s=[]
    for pkt in packets:
        if ARP in pkt:
            try:
                s.append(pkt[ARP].psrc)
            except:
                pass
    col_count = Counter(s)
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='ARP Source Occurence Bar Graph',xaxis_title='ARP Source',\
        yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='ARP Source Occurence Line Graph',xaxis_title='ARP Source',yaxis_title='Count',\
        paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='ARP Source Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='ARP Source Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='ARP Source Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='ARP Source Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()

def plot_ether_type(packets):
    s=[]
    for pkt in packets:
        if Ether in pkt:
            try:
                s.append(pkt[Ether].type)
            except:
                pass
    col_count = Counter(s)
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='Ethernet Type Occurence Bar Graph',xaxis_title='Ethernet Type',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Ethernet Type Occurence Line Graph',xaxis_title='Ethernet Type',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='Ethernet Type Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Ethernet Type Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='Ethernet Type Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Ethernet Type Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
     
def plot_udp_len(packets):
    s=[]
    for pkt in packets:
        if UDP in pkt:
            try:
                s.append(pkt[UDP].len)
            except:
                pass
    col_count = Counter(s)
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='UDP Length Occurence Bar Graph',xaxis_title='UDP Length',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='UDP Length Occurence Line Graph',xaxis_title='UDP Length',yaxis_title='CountEther Type',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='UDP Length Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='UDP Length Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='UDP Length Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='UDP Length Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")

def plot_tcp_window(packets):
    s=[]
    for pkt in packets:
        if TCP in pkt:
            try:
                s.append(pkt[TCP].window)
            except:
                pass
    col_count = Counter(s)
    yData = list(col_count.keys())
    xData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='TCP Window Occurence Bar Graph',xaxis_title='TCP Window',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='TCP Window Occurence Line Graph',xaxis_title='TCP Window',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='TCP Window Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='TCP Window Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='TCP Window Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='TCP Window Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")

def plot_ether_hwdst(packets):
    s=[]
    for pkt in packets:
        if Ether in pkt:
            try:
                s.append(pkt[Ether].hwdst)
            except:
                pass
    cnt=Counter(s)
    xData=list(cnt.keys())
    yData=list(cnt.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='Ethernet Target Hardware Address Occurence Bar Graph',xaxis_title='Ethernet Target Hardware Address',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Ethernet Target Hardware Address Occurence Line Graph',xaxis_title='Ethernet Target Hardware Address',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='Ethernet Target Hardware Address Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Ethernet Target Hardware Address Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='IP Source Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Ethernet Target Hardware Address Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")

def plot_ip_len(packets):
    s=[]
    for pkt in packets:
        if IP in pkt:
            try:
                s.append(pkt[IP].len)
            except:
                pass
    col_count = Counter(s)
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='IP Length Occurence Bar Graph',xaxis_title='IP Length',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='IP Length Occurence Line Graph',xaxis_title='IP Length',yaxis_title='Count',)
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='IP Length Occurrence Pie Graph')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='IP Length Occurrence Doughtnut Graph')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='IP Length Occurrence Sunburst Graph')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='IP Lenght Occurrence 3-D Graph')
        fig.show()
    else:
        print("Type either of those")

def plot_ip_ttl(packets):
    s=[]
    for pkt in packets:
        if IP in pkt:
            try:
                s.append(pkt[IP].ttl)
            except:
                pass
    col_count = Counter(s)
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='Packet Time to Live Occurence Bar Graph',xaxis_title='Packet Time to Live',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Packet Time to Live Occurence Line Graph',xaxis_title='Packet Time to Live',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='Packet Time to Live Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Packet Time to Live Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='Packet Time to Live Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Packet Time to Live Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")


def plot_sport_port(packets):
    counttt=0
    s=[]
    for pkt in packets:
        if TCP in pkt:
            try:
                s.append(pkt[TCP].sport)
                counttt +=1
            except:
                pass
    col_count = Counter(s) 
    xData = list(col_count.keys())
    yData = list(col_count.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='TCP Source Port Occurence Bar Graph',xaxis_title='TCP Source Port',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='TCP Source Port Occurence Line Graph',xaxis_title='TCP Source Port',yaxis_title='Count',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='TCP Source Port Occurrence Pie Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='TCP Source Port Occurrence Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='TCP Source Port Occurrence Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='TCP Source Port Occurrence 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")

def plot_ip_version(packets):
    srcIP=[]
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].version)
            except:
                pass
    cnt=Counter(srcIP)
    xData=list(cnt.keys())
    yData=list(cnt.values())
    option = int(input("\nWhat kinda graph you want ?\n1.Bar\n2.Line\n3.Pie\n4.Doughtnut Graph\
    \n5.SunBurst Graph\n6.3-D Graph\n"))
    if option == 1:
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=yData,colorscale='Viridis'))])
        fig.update_layout(title='IP Version Occurence ',xaxis_title='IP Source Address',yaxis_title='Count')
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Line Chart of IP Version Occurence',xaxis_title='IP Source Address',yaxis_title='Count',\
        paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='IP Source Version Pie Graph',paper_bgcolor='peachpuff')
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='IP Source Version Doughtnut Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='IP Source Version Sunburst Graph',paper_bgcolor='lightgray')
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='IP Source Version 3-D Graph',paper_bgcolor='lightgray')
        fig.show()
    else:
        print("Type either of those")

address = input("Enter the file name stored in the folder with the extension: ")
if os.path.exists(address):
    packets = rdpcap(address)
#read the pcap file    
    print("\nChoose your Network Parameter for the Occurance Plot: ")
#choose the parameter given below to plot the graph    
    print("\n1.IP Source Address\t\t2.IP Destination Address\n3.IP Length\
    \t\t\t4.Packet's Time To Live\n5.Sender Hardware Address   \t6.Target Hardware Address\
    \n7.Sender Ports\t\t\t8.Destination Ports\n9.UDP Length\
    \t\t10.ARP Source\n11.TCP Window\t\t\t12.Ethernet Type\
    \n13.IP Version")
    while True:
        ch = int(input("\nEnter you choice to count the occurence: \n\t**Enter 0 to exit**\n"))
        if(ch!=0):
            user_choice(ch,packets)
        else:
            print("\t---- Thank you ----")
            break
else:
    print("\n\t\t**The file doesn't exist in this directory, please change the file location or check the file name**") 
    print("\n(File Name to be given like user_file_name.pcap and in the same folder)\n")