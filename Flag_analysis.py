#analysing and visualising the throughput and the occurences of flags in a abnormal and normal traffic of packets

from scapy.all import rdpcap, IP, TCP
import plotly.graph_objects as go


def generate(packets,x):
    packet_count = x
#packet count to be varied    
    TCP_packets = [packet for packet in packets if TCP in packet]
    TCP_packets = TCP_packets[:packet_count]
    syn_count = 0
    ack_count = 0
    fin_count = 0
#count the number of the flags in the packet sent and recevied    
    for packet in TCP_packets:
        if packet[TCP].flags & 0x02:
            syn_count += 1
        if packet[TCP].flags & 0x010:
            ack_count += 1
        if packet[TCP].flags & 0x01:
            fin_count += 1
#throughput calculation for the packet count
    throughput = packet_count / len(TCP_packets)
    print(f"Number of SYN packets: {syn_count}")
    print(f"Number of ACK packets: {ack_count}")
    print(f"Number of FIN packets: {fin_count}")
    print(f"Throughput: {throughput:.2f} packets per packet analyzed")
    xdata = ['SYN', 'ACK', 'FIN']
    ydata = [syn_count, ack_count, fin_count]
    return xdata, ydata,throughput

def choice(option,xData, yData,throughput):
    if option == 1:
#defining the colours for the graph
        gradient_colors = ['red', 'green', 'yellow', 'blue']
        fig=go.Figure(data=[go.Bar(x=xData, y=yData,marker=dict(color=gradient_colors))])
#write the graph name and the text - throughput in it
        fig.update_layout(title='Flag Occurances Bar Graph',xaxis_title='Packets Flags',yaxis_title='Count',yaxis=dict(range=[0,500]),paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
#display the graph in the local web browser        
        fig.show()
    if option == 2:
        fig=go.Figure(data=[go.Line(x=xData,y=yData,line=dict(color='black'))])
        fig.update_layout(title='Flag Occurances Line Graph',xaxis_title='Packets Flags',yaxis_title='CountEther Type',paper_bgcolor='lightgray',plot_bgcolor='lavenderblush')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
        fig.show()
    if option == 3:
        fig = go.Figure(data=[go.Pie(labels=xData,values=yData)])
        fig.update_layout(title='Flag Occurances Pie Chart',paper_bgcolor='lightgray')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
        fig.show()
    if option == 4:
        fig=go.Figure(data=[go.Pie(labels=xData,values=yData,hole=0.5)])
        fig.update_layout(title='Flag Occurances Doughnut Graph',paper_bgcolor='lightgray')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
        fig.show()
    if option == 5:
        fig = go.Figure(data=[go.Sunburst(labels=xData,parents=['']*len(xData),values=yData)])
        fig.update_layout(title='Flag Occurances Sunburst Graph',paper_bgcolor='lightgray')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
        fig.show()
    if option == 6:
        fig = go.Figure(data=go.Scatter3d(x=xData, y=yData, z=yData, mode='lines+markers', marker=dict(size=10)))
        fig.update_layout(title='Flag Occurances Scatter 3D',paper_bgcolor='lightgray')
        fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}',x=1,y=1.07,xref='paper',yref='paper',showarrow=False,font=dict(size=10,color='red'))])
        fig.show()

pcap_file = input("Enter the file and with its extensions : ")
pcap_file1 = input("Enter the file with abnormality: ")

x = int(input("Enter the packet count to be analysed: "))

packets = rdpcap(pcap_file)
packets1 = rdpcap(pcap_file1)

xdata1, ydata1 ,throughput1 = generate(packets,x)
xdata2, ydata2, throughput2 = generate(packets1,x)


option = int(input("Enter the option\n1: Bar\n2: Line\n3: Pie\n4: Doughnut\n5: Sunburst\n6: Scatter 3D\n"))
choice(option,xdata1, ydata1,throughput1)
choice(option,xdata2, ydata2, throughput2)
