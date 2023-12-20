# Pricing Details from Railway
cpu_cost_per_minute = 0.000463  # in dollars
memory_cost_per_minute = 0.000231  # in dollars
network_cost_per_kb = 0.000000095367432  # in dollars


# Assumed Resource Usage Per Execution
cpu_time_in_seconds = 14.28969693183899 # the CPU time you measured
cpu_usage_per_execution = cpu_time_in_seconds / 60  # vCPU minutes

peak_memory_usage_in_mib = 595.109375 # the peak memory usage you measured
memory_usage_per_execution = (peak_memory_usage_in_mib / 1024) * 1.074  # Convert MiB to GB

network_egress_per_execution = 6144  # KB


# Function to calculate costs based on number of executions
def calculate_costs(number_of_executions):
    # CPU Cost
    total_cpu_cost = cpu_usage_per_execution * number_of_executions * cpu_cost_per_minute

    # Memory Cost
    total_memory_cost = memory_usage_per_execution * number_of_executions * memory_cost_per_minute

    # Network Cost
    total_network_cost = network_egress_per_execution * number_of_executions * network_cost_per_kb

    # Total Cost
    total_cost = total_cpu_cost + total_memory_cost + total_network_cost

    return {
        "CPU Cost": total_cpu_cost,
        "Memory Cost": total_memory_cost,
        "Network Cost": total_network_cost,
        "Total Cost": total_cost
    }


# Example usage:
number_of_executions = 900000  # Change this number to calculate for different executions
costs = calculate_costs(number_of_executions)
print(f"Costs for {number_of_executions} executions:")
for cost_type, cost in costs.items():
    print(f"{cost_type}: ${cost:.4f}")


# ### Calculating Total Ingress
# video_size_mb = 6  # Size of one video in MB
# total_videos = 60000  # Total number of videos
#
# # Total network ingress in MB
# total_network_ingress_mb = video_size_mb * total_videos
#
# # Convert MB to GB for understanding (1 GB = 1024 MB)
# total_network_ingress_gb = total_network_ingress_mb / 1024
#
# print(f"Total Network Ingress: {total_network_ingress_gb} GB")