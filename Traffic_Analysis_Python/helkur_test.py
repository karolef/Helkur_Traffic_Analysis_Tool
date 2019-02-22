from helkur_search import show_sum_for_protocol
from helkur_search import show_all_for_protocol
from helkur_search import show_chosen_column_for_protocol

# show_all_for_protocol("DNS")
# show_sum_for_protocol("TCP")

# optional columns: ip_source, ip_dest, port_tcp_source, port_tcp_dest, protocol, frame_length
show_chosen_column_for_protocol("ip_source", "TCP")
