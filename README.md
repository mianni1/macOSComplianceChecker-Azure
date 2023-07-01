# macOSComplianceChecker-Azure

## Description

This will be an automated framework designed to empower macOS administrators who are using Microsofts Intune to enforce and monitor software based compliance issues their macOS fleet, when it comes to dealing with users wielding higher privilege and are able to uninstall and manipulate software such as MS Defender and other security tooling. 

This framework will allow you to check your macOS fleet for compliance with your organisation's security policies much more frequently than Intune's native eight [8] hour check-in window. This framework will also allow you to remediate and take enforcement action against any non-compliant endpoints automatically at custom intervals. However, I will go with the default of every fifteen [15] minutes.

This is a work in progress and I will be adding working on this project so you may notice a lot of incomplete sections. I will be adding to this project as I go along.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [Tests](#tests)
5. [License](#license)

## Installation

To get started with macOSComplianceEnforcer-Azure, you'll need to set up a few things on your local machine and on the target endpoints:

### Local Machine Setup

- **An Azure account**: You'll be using Azure Functions and you will obviously have one given that you are using Intune to manage your fleet. If you don't have one, well you are in the wrong place :D.

- **Azure CLI**: This is a command line tool for managing Azure resources. You can download it [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

- **VS Code**: This is the code editor I am using for this project. You can download it [here](https://code.visualstudio.com/download).

- **Terraform**: This is an open-source infrastructure as code software tool. You can download it [here](https://www.terraform.io/downloads.html).

- **Homebrew**: This is a package manager for macOS that you'll use for installing other tools. Install it from [here](https://brew.sh/). Worth noting most good enterprise environments will not let you install this so you may need to adapt and modify some of the steps in this repo. Maybe when I have more time I might look into completly removing this dependency.

### Endpoint Setup

- **Microsoft Intune**: You'll need to have all the target endpoints enrolled in Microsoft Intune.

- **Zsh script**: A script will need to be deployed to all endpoints using Intune. This script will check the status of an application (e.g., MS Defender) and call an Azure Function if the application is not running or installed.

## Usage

Instructions on how to use the tool. NOTE: WORK IN PROGRESS

## Contributing

Information for anyone who wants to contribute to the project. NOTE: WORK IN PROGRESS

## Tests

Information about the testing performed within the project and how to run them. NOTE: WORK IN PROGRESS

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for the full text