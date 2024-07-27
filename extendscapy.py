from scapy.all import *
from collections import Counter
import plotly.express as px
from plotly.subplots import make_subplots
# import plotly.graph_objects as go


def area_ipdst(packets):
    packets = rdpcap(packets)
    ip_destinations = [pkt[IP].dst for pkt in packets if IP in pkt]
    cnt = Counter(ip_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Destination Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.data[0].line.color = 'black'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_ipdst(packets):
    packets = rdpcap(packets)
    ip_destinations = [pkt[IP].dst for pkt in packets if IP in pkt]
    cnt = Counter(ip_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    # # Calculate latency
    # ip_requests = {pkt[IP].dst: pkt.time for pkt in packets if IP in pkt}
    # latency = []

    # for pkt in packets:
    #     if IP in pkt:
    #         response_time = pkt.time
    #         ip_destination = pkt[IP].dst
    #         if ip_destination in ip_requests:
    #             latency.append(response_time - ip_requests[ip_destination])


    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Destination Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = [  'red', 'darkred', 'firebrick', 'crimson',  'orange', 'darkorange',  'yellow', 'gold', 'lightyellow',  'green', 'darkgreen', 'lime', 'forestgreen',  'blue', 'darkblue', 'mediumblue', 'royalblue',  'purple', 'mediumpurple', 'rebeccapurple',  'pink', 'deeppink', 'hotpink', 'lightpink',  'brown', 'saddlebrown', 'maroon', 'sienna',  'gray', 'darkgray', 'lightgray', 'dimgray',  'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces( marker=dict(color=gradient_colors), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    # fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_ipdst(packets):
    packets = rdpcap(packets)
    ip_destinations = [pkt[IP].dst for pkt in packets if IP in pkt]
    cnt = Counter(ip_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Destination Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_ipsrc(packets):
    packets = rdpcap(packets)
    ip_sources = [pkt[IP].src for pkt in packets if IP in pkt]
    cnt = Counter(ip_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Source Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_ipsrc(packets):
    packets = rdpcap(packets)
    ip_sources = [pkt[IP].src for pkt in packets if IP in pkt]
    cnt = Counter(ip_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Source Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color='black'), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_ipsrc(packets):
    packets = rdpcap(packets)
    ip_sources = [pkt[IP].src for pkt in packets if IP in pkt]
    cnt = Counter(ip_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(pkt[IP].len for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['IP Source Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='IP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_arp_src(packets):
    packets = rdpcap(packets)
    arp_sources = [pkt[ARP].psrc for pkt in packets if ARP in pkt]
    cnt = Counter(arp_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Source Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_arp_src(packets):
    packets = rdpcap(packets)
    arp_sources = [pkt[ARP].psrc for pkt in packets if ARP in pkt]
    cnt = Counter(arp_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Source Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color='black'), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_arp_src(packets):
    packets = rdpcap(packets)
    arp_sources = [pkt[ARP].psrc for pkt in packets if ARP in pkt]
    cnt = Counter(arp_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Source Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.data[0].line.color = 'black'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_arp_dst(packets):
    packets = rdpcap(packets)
    arp_destinations = [pkt[ARP].pdst for pkt in packets if ARP in pkt]
    cnt = Counter(arp_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Destination Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_arp_dst(packets):
    packets = rdpcap(packets)
    arp_destinations = [pkt[ARP].pdst for pkt in packets if ARP in pkt]
    cnt = Counter(arp_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Destination Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color='black'), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_arp_dst(packets):
    packets = rdpcap(packets)
    arp_destinations = [pkt[ARP].pdst for pkt in packets if ARP in pkt]
    cnt = Counter(arp_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if ARP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[ARP]) for pkt in packets if ARP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['ARP Destination Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='ARP Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_sender_port(packets):
    packets = rdpcap(packets)
    sender_ports = [pkt[TCP].sport if TCP in pkt else pkt[UDP].sport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(sender_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Sender Port Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Sender Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.data[0].line.color = 'black'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_sender_port(packets):
    packets = rdpcap(packets)
    sender_ports = [pkt[TCP].sport if TCP in pkt else pkt[UDP].sport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(sender_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Sender Port Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color=gradient_colors), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Sender Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_sender_port(packets):
    packets = rdpcap(packets)
    sender_ports = [pkt[TCP].sport if TCP in pkt else pkt[UDP].sport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(sender_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Sender Port Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Sender Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_destination_port(packets):
    packets = rdpcap(packets)
    dest_ports = [pkt[TCP].dport if TCP in pkt else pkt[UDP].dport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(dest_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Destination Port Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Destination Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_destination_port(packets):
    packets = rdpcap(packets)
    dest_ports = [pkt[TCP].dport if TCP in pkt else pkt[UDP].dport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(dest_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Destination Port Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color=gradient_colors), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Destination Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_destination_port(packets):
    packets = rdpcap(packets)
    dest_ports = [pkt[TCP].dport if TCP in pkt else pkt[UDP].dport for pkt in packets if TCP in pkt or UDP in pkt]
    cnt = Counter(dest_ports)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt or UDP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) if TCP in pkt else len(pkt[UDP]) for pkt in packets if TCP in pkt or UDP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Destination Port Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Destination Port', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.data[0].line.color = 'black'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_window_size(packets):
    packets = rdpcap(packets)
    window_sizes = [pkt[TCP].window if TCP in pkt else None for pkt in packets if TCP in pkt]
    window_sizes = [size for size in window_sizes if size is not None]
    cnt = Counter(window_sizes)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) for pkt in packets if TCP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Window Size Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Window Size', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_window_size(packets):
    packets = rdpcap(packets)
    window_sizes = [pkt[TCP].window if TCP in pkt else None for pkt in packets if TCP in pkt]
    window_sizes = [size for size in window_sizes if size is not None]
    cnt = Counter(window_sizes)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) for pkt in packets if TCP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Window Size Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color=gradient_colors), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Window Size', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_window_size(packets):
    packets = rdpcap(packets)
    window_sizes = [pkt[TCP].window if TCP in pkt else None for pkt in packets if TCP in pkt]
    window_sizes = [size for size in window_sizes if size is not None]
    cnt = Counter(window_sizes)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if TCP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[TCP]) for pkt in packets if TCP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Window Size Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Window Size', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_ttl(packets):
    packets = rdpcap(packets)
    ttl_values = [pkt[IP].ttl if IP in pkt else None for pkt in packets if IP in pkt]
    ttl_values = [ttl for ttl in ttl_values if ttl is not None]
    cnt = Counter(ttl_values)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[IP]) for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes / second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Time to Live Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Time to Live', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.data[0].line.color = 'black'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_ttl(packets):
    packets = rdpcap(packets)
    ttl_values = [pkt[IP].ttl if IP in pkt else None for pkt in packets if IP in pkt]
    ttl_values = [ttl for ttl in ttl_values if ttl is not None]
    cnt = Counter(ttl_values)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[IP]) for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Time to Live Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color=gradient_colors), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Time to Live', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_ttl(packets):
    packets = rdpcap(packets)
    ttl_values = [pkt[IP].ttl if IP in pkt else None for pkt in packets if IP in pkt]
    ttl_values = [ttl for ttl in ttl_values if ttl is not None]
    cnt = Counter(ttl_values)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if IP in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[IP]) for pkt in packets if IP in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Time to Live Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Time to Live', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_ethernet_source(packets):
    packets = rdpcap(packets)
    eth_sources = [pkt[Ether].src for pkt in packets if Ether in pkt]
    cnt = Counter(eth_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes / second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Source Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_ethernet_source(packets):
    packets = rdpcap(packets)
    eth_sources = [pkt[Ether].src for pkt in packets if Ether in pkt]
    cnt = Counter(eth_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Source Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color='black'), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_ethernet_source(packets):
    packets = rdpcap(packets)
    eth_sources = [pkt[Ether].src for pkt in packets if Ether in pkt]
    cnt = Counter(eth_sources)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Source Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Source', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def area_ethernet_destination(packets):
    packets = rdpcap(packets)
    eth_destinations = [pkt[Ether].dst for pkt in packets if Ether in pkt]
    cnt = Counter(eth_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes / second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Destination Distribution', 'Jitter Distribution'])
    graph = px.area(x=xData, y=yData, title='Area Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'lightgreen'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def bar_ethernet_destination(packets):
    packets = rdpcap(packets)
    eth_destinations = [pkt[Ether].dst for pkt in packets if Ether in pkt]
    cnt = Counter(eth_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time

    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Destination Distribution', 'Jitter Distribution'])
    graph = px.bar(x=xData, y=yData, title='Bar Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    gradient_colors = ['red', 'darkred', 'firebrick', 'crimson', 'orange', 'darkorange', 'yellow', 'gold', 'lightyellow', 'green', 'darkgreen', 'lime', 'forestgreen', 'blue', 'darkblue', 'mediumblue', 'royalblue', 'purple', 'mediumpurple', 'rebeccapurple', 'pink', 'deeppink', 'hotpink', 'lightpink', 'brown', 'saddlebrown', 'maroon', 'sienna', 'gray', 'darkgray', 'lightgray', 'dimgray', 'white', 'black', 'snow', 'ivory', 'black']
    fig.update_traces(marker=dict(color='black'), selector=dict(type='bar'))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()

def line_ethernet_destination(packets):
    packets = rdpcap(packets)
    eth_destinations = [pkt[Ether].dst for pkt in packets if Ether in pkt]
    cnt = Counter(eth_destinations)
    xData = list(cnt.keys())
    yData = list(cnt.values())
    arrival_times = [pkt.time for pkt in packets if Ether in pkt]
    jitter = [arrival_times[i + 1] - arrival_times[i] for i in range(len(arrival_times) - 1)]
    total_bytes = sum(len(pkt[Ether]) for pkt in packets if Ether in pkt)
    total_time = arrival_times[-1] - arrival_times[0]
    throughput = total_bytes / total_time
    print(f"Throughput: {throughput} bytes  /second")
    fig = make_subplots(rows=1, cols=2, subplot_titles=['Ethernet Destination Distribution', 'Jitter Distribution'])
    graph = px.line(x=xData, y=yData, title='Line Chart')
    fig.add_trace(graph.data[0], row=1, col=1)
    fig.update_coloraxes(graph.layout.coloraxis, colorbar=dict(xanchor='left', thickness=15))
    fig.update_yaxes(title_text='Count', row=1, col=1)
    fig.update_xaxes(title_text='Ethernet Destination', row=1, col=1)
    fig.update_layout(plot_bgcolor='lavenderblush')
    fig.data[0].line.color = 'red'
    fig.update_layout(annotations=[dict(text=f'Throughput of the given network is - {throughput}', x=0.8, y=1.07, xref='paper', yref='paper', showarrow=False, font=dict(size=20, color='red'))])
    fig.add_trace(px.scatter(x=range(len(jitter)), y=jitter).data[0], row=1, col=2)
    fig.update_xaxes(title_text='Packet Index', row=1, col=2)
    fig.update_yaxes(title_text='Jitter', row=1, col=2)
    fig.update_layout(height=600, width=1000, showlegend=False)
    fig.show()


# packets = input("Enter the packets files to be analysed:  ")
packets = "TestRunFile.pcap" 

area_ipdst(packets)
# bar_ipdst(packets)
# line_ipdst(packets)

# area_ipsrc(packets)
bar_ipsrc(packets)
#line_ipsrc(packets)

# area_arp_src(packets)
# bar_arp_src(packets)
line_arp_src(packets)

# area_arp_dst(packets)
bar_arp_dst(packets)
# line_arp_dst(packets)

area_sender_port(packets)
# bar_sender_port(packets)
# line_sender_port(packets)

# area_destination_port(packets)
# bar_destination_port(packets)
line_destination_port(packets)

# area_window_size(packets)
# bar_window_size(packets)
# line_window_size(packets)

area_ttl(packets)
# bar_ttl(packets)
# line_ttl(packets)

# area_ethernet_source(packets)
bar_ethernet_source(packets)
# line_ethernet_source(packets)

# area_ethernet_destination(packets)
bar_ethernet_destination(packets)
# line_ethernet_destination(packets)