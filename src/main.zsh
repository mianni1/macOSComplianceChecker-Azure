#!/bin/bash

# This script checks if Microsoft Defender is installed and running every 15 minutes. 
# You can also your own custom checks to this and add more functions by following my example of MS Defender below.
# If Microsoft Defender is not running, it attempts to start it and calls an Azure Function to report the event.
# If Microsoft Defender is not installed, it calls a different Azure Function to trigger reinstallation, enforcement action and report the event

# The script is based on code from the Microsoft shell-intune-samples repository:
# https://github.com/microsoft/shell-intune-samples/blob/master/macOS/Custom%20Attributes/checkDefenderRunning/checkDefenderRunning.sh

# Function URLs and keys from Azure Functions
running_function_url="https://your-azure-function-url.azurewebsites.net/api/functionName"
running_function_key="your-azure-function-key"

enforcement_function_url="https://your-azure-function-url.azurewebsites.net/api/enforcmentActionFunctionName"
enforcement_function_key="your-azure-function-key"

# Check if Microsoft Defender is installed
defenderInstalled=$(ls /Applications/ | grep -x "Microsoft Defender.app")

if [ -z "$defenderInstalled" ]; then
    # Microsoft Defender is not installed
    # Call Azure Function to trigger enforcement action on the Endpoint
    curl -X POST "$enforcement_function_url" -H "x-functions-key:$enforcement_function_key"
else
    # Microsoft Defender is installed
    # Check if Microsoft Defender is running
    defenderStatus=$(pgrep -x "Microsoft Defender")

    # If Microsoft Defender is not running, then start it
    if [ -z "$defenderStatus" ]; then
        # Microsoft Defender is not running
        # Start Microsoft Defender
        open -a "Microsoft Defender"
        # Call Azure Function
        curl -X POST "$running_function_url" -H "x-functions-key:$running_function_key"
    fi
fi
