
'''
Q7. EC2 Recommendation
Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
Input:
Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

The output will be a recommendation for a new EC2 instance based on the following logic:

Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
 
Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:

nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge..

If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one step.
If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one step.
If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended.
If the instance is the largest (32xlarge), it cannot be upgraded further.

Input 1: 
Current EC2 : t2.large
CPU : 20%

Output 1:
Table showing columns and its value (use Que 6 function to make table with following columns)
Columns are : serial no., current ec2, current CPU, status, recommended ec2

'''
import csv


instance_sizes = ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]

def get_instance_recommendation(current_instance, cpu_utilization):
    instance_type, instance_size = current_instance.split('.')
    size_index = instance_sizes.index(instance_size)
    
    if cpu_utilization < 20:
        if size_index > 0:
            recommended_size = instance_sizes[size_index - 1]
        else:
            recommended_size = instance_size
        status = "Underutilized"
    elif 20 <= cpu_utilization <= 80:
        recommended_size = instance_size
        status = "Optimized"
    else:
        if size_index < len(instance_sizes) - 1:
            recommended_size = instance_sizes[size_index + 1]
        else:
            recommended_size = instance_size
        status = "Overutilized"
    
    recommended_instance = f"{instance_type}.{recommended_size}"
    return status, recommended_instance

def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    
    for row in data:
        row_str = " | ".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
        print(f"| {row_str} |")
        if row == data[0]:  
            print("|" + "|".join("-" * (col_width + 2) for col_width in col_widths) + "|")

def print_recommendation_table(current_instance, cpu_utilization):
    status, recommended_instance = get_instance_recommendation(current_instance, cpu_utilization)
    data = [
        ["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"],
        ["1", current_instance, f"{cpu_utilization}%", status, recommended_instance]
    ]
    print_table(data)

# Example usage
current_instance = "t2.large"
cpu_utilization = 20
print_recommendation_table(current_instance, cpu_utilization)