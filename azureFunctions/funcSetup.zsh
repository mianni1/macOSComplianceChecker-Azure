#!/bin/zsh

# Create a new Azure Functions project
func init macOSComplianceEnforcerFunctions --python

# Navigate into the project directory
cd macOSComplianceEnforcerFunctions

# Create a new function for checking Defender status
func new --name CheckDefenderStatus --template "HTTP trigger" --authlevel "function"

# Create a new function for enforcement action
func new --name EnforceCompliance --template "HTTP trigger" --authlevel "function"

# Install necessary Python packages
echo "requests" >> requirements.txt
