## Overview

The `firewall_project` is a Python-based firewall tool that leverages the `scapy` library. This project aims to provide basic firewall functionalities, including packet filtering and logging.

## Installation

To install the `firewall_project`, follow these steps:

1. **Clone the Repository**

   First, clone the repository from GitHub (or your preferred version control system):

   ```bash
    git clone https://github.com/mesopotamico/basic_Firewall.git
    cd firewall_project```

2. Set Up a Virtual Environment (Recommended)
It is highly recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the Project
Install the project along with its dependencies using pip:
```bash
    pip install -e .
```

This command will install the firewall_project along with the scapy dependency specified in the setup.py file.
Usage

Once installed, you can use the command-line tool provided by the firewall_project:

```bash
    firewall
```

This command will execute the main function from the firewall module. Customize the tool's behavior by editing the firewall.py file in the src directory.

**Note:** You have to be a root user to run the program.


### Environment Variables

To configure the application, you need to set the following environment variables:

- **`ALLOWED_IPS`**: Specifies the IP addresses that are permitted to access the application. You can list multiple IP addresses separated by commas. Example:
  ```
  ALLOWED_IPS=192.168.1.10,10.0.0.5
  ```

- **`ALLOWED_PORTS`**: Defines the network ports that the application will accept. List multiple ports separated by commas. Example:
  ```
  ALLOWED_PORTS=80,443,3478
  ```

- **`ALLOWED_PROTOCOLS`**: Specifies the network protocols allowed by the application. List multiple protocols separated by commas. Example:
  ```
  ALLOWED_PROTOCOLS=TCP,UDP,Ethernet,IP,Raw,DNS
  ```

To set these environment variables, you can add them to your `.env` file or configure them directly in your server or development environment.

