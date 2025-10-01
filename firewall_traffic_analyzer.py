# Name: Justin Coon
# Date: 09-30-2025
# Description: This program mimicks the analysis of firewall traffic.


print("=== Network Traffic Security Analyzer ===\n")


# Variable declaration for inputs containing port numbers and transfer size
port_num = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))



# If statement checking if the file size on port 22 is greater than 500MB 
# and prints a high risk statement of unauthorized remote access if it is
if port_num == 22 or port_num == 3389 and transfer_size >= 100:
    
    # Print statements showing the analyzed traffic and the risk assessment
    print("\nFIREWALL LOG:")
    print(f"Port: {port_num}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!")
    print("------------------------")

# elif clause checking if the file size being transfered on port 80 is greater than 100MB
# If it is, a medium risk flag of large unecrypted file data transfer detected    
elif port_num == 80 and transfer_size > 100:
    
    # Print statements showing the analyzed traffic and the risk assessment
    print("\nFIREWALL LOG:")
    print(f"Port: {port_num}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.")
    print("------------------------")
    
# elif clause checking port 443
elif port_num == 443:
    
    # Print statements showing the analyzed traffic and the risk assessment
    print("\nFIREWALL LOG:")
    print(f"Port: {port_num}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: LOW RISK: Secure encrypted transfer detected.")
    print("------------------------")
    

# else clause checking all other ports
else:
    
    # Print statements showing the analyzed traffic and the risk assessment
    print("\nFIREWALL LOG:")
    print(f"Port: {port_num}, Transfer Size: {transfer_size} MB")
    print("Risk Assessment: UNKNOWN: Unrecognized traffic pattern.")
    print("------------------------")