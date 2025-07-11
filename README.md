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

[Cisco Router Config](https://github.com/dubeysatyam15/netmiko-paramiko-lab/blob/main/cisco_ssh_setup.txt)
