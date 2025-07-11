# 🧪 Netmiko & Paramiko Practice Lab (GNS3 + Docker)

This repository contains a collection of scripts I wrote while learning **Python-based network automation** using **Netmiko** and **Paramiko**. I ran these in a custom **Network Automation Docker container** within a **GNS3 lab**, interacting with Cisco IOU L3 images configured with SSH and Telnet.

---

## 🔍 What this is

- My hands-on experiments while learning:
  - SSH/Telnet connections to Cisco routers.
  - Sending CLI commands via Netmiko and Paramiko.
  - Pushing configuration changes.
  - Fetching show command outputs.
- Scripts are tested against **Cisco IOU L3** images with both **Telnet** and **SSH** enabled.
- The environment was built using **GNS3** and a Dockerized automation container.

---

## 🛠 Tools & Tech Used

| Tool      | Purpose                     |
|-----------|-----------------------------|
| Python 3  | Scripting language          |
| Netmiko   | Simplified SSH/Telnet       |
| Paramiko  | Lower-level SSH automation  |
| GNS3      | Network emulation           |
| Docker    | Automation container        |
| Cisco IOU | L3 routers with SSH/Telnet  |

---

## 🔧 Cisco Router Setup for SSH & Telnet Access

R1# configure terminal
R1(config)# hostname R1
R1(config)# ip domain-name cisco.com
R1(config)# crypto key generate rsa
The name for the keys will be: R1.cisco.com
Choose the size of the key modulus in the range of 360 to 4096 for your
   General Purpose Keys. Choosing a key modulus greater than 512 may take
   a few minutes.

How many bits in the modulus [512]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...OK

R1(config)# ip ssh version 2
R1(config)# line vty 0 4
R1(config-line)# transport input ssh telnet
R1(config-line)# login local
R1(config-line)# end
R1# configure terminal
R1(config)# username cisco privilege 15 password cisco
R1(config)# end
R1# write memory        ! (optional) save running‑config to startup‑config
Building configuration...
[OK]
