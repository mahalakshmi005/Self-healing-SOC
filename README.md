# 🛡️ Self-Healing SOC
### AI-Assisted Automated Threat Detection and Response System

## 1. Project Overview

Self-Healing SOC is an AI-assisted Security Operations Center automation project designed to detect suspicious file activity, analyze security alerts, and automate incident response.

The project integrates Wazuh, n8n, VirusTotal, Groq AI, REST APIs, and Python to build an automated threat detection and response pipeline.

It reduces manual intervention by automating security alert processing, threat intelligence analysis, conditional evaluation, and file quarantine in a controlled lab environment.

## 2. Project Objectives

- Monitor Windows endpoint file activity.
- Detect suspicious file events using Wazuh.
- Automate security alert processing using n8n.
- Analyze file hashes using VirusTotal.
- Integrate Groq AI through an n8n AI Agent.
- Use REST APIs for communication with security services.
- Trigger automated responses through Wazuh Active Response.
- Quarantine eligible test files using a custom Python script.
- Maintain execution logs and notifications.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Wazuh | Security monitoring and threat detection |
| n8n | Security workflow automation |
| VirusTotal | File hash reputation analysis |
| Groq AI | AI-powered alert processing through AI Agent |
| Python | Custom file quarantine script |
| REST APIs | Communication with Wazuh and VirusTotal |
| HTTP Request | API integration through n8n |
| JSON | API request and response data handling |
| Kali Linux | Wazuh Manager and n8n environment |
| Windows 11 | Wazuh Agent endpoint |

## 4. System Architecture

```text
              WINDOWS 11 ENDPOINT
                  (Wazuh Agent)
                       |
                       v
                 WAZUH MANAGER
              (Security Monitoring)
                       |
                       v
                 n8n WORKFLOW
                       |
            +----------+----------+
            |                     |
            v                     v
        VIRUSTOTAL              GROQ AI
      (Hash Analysis)         (AI Agent)
            |                     |
            v                     v
       Threat Data           AI Output Parser
            |                     |
            +----------+----------+
                       |
                       v
                     MERGE
                       |
                       v
               CONDITIONAL CHECK
                       |
             +---------+---------+
             |                   |
             v                   v
         MALICIOUS           NOT MATCHED
             |                   |
             v                   v
     WAZUH ACTIVE RESPONSE    LOG RESULT
             |
             v
      PYTHON QUARANTINE
           SCRIPT
             |
             v
       QUARANTINE FOLDER
             |
             v
       LOGGING AND EMAIL
        NOTIFICATION
```

## 5. Workflow Explanation

### Step 1: Endpoint Monitoring

Wazuh Agent is installed on the Windows 11 endpoint to monitor configured file activity.

### Step 2: Threat Detection

Wazuh Manager receives endpoint events and generates security alerts based on configured detection rules.

### Step 3: Workflow Automation

n8n receives the security alert and processes relevant event information.

### Step 4: VirusTotal Analysis

The workflow extracts the file hash and uses the VirusTotal API to retrieve file reputation information.

### Step 5: Groq AI Integration

The Groq Chat Model is connected to an n8n AI Agent.

The AI Agent processes the supplied alert information, and its output is passed through an AI Output Parser.

### Step 6: Result Merging

The workflow combines the relevant results using a Merge node.

### Step 7: Conditional Evaluation

The IF node evaluates the configured condition to determine whether the workflow should trigger the automated response or follow the alternative logging branch.

### Step 8: Automated Response

When the configured malicious-verdict condition is met, n8n communicates with the Wazuh REST API to trigger Wazuh Active Response.

### Step 9: File Quarantine

A custom Python Active Response script executes on the Windows endpoint.

It moves eligible test files from the monitored directory into the quarantine directory.

### Step 10: Logging and Notification

The workflow includes logging and email notification nodes to support execution tracking and alert communication.

## 6. REST API Integration

The project uses REST APIs through n8n HTTP Request nodes to communicate with security services.

### Wazuh REST API

- Used for API authentication.
- Uses token-based authentication.
- Used to retrieve relevant API information.
- Used to trigger Wazuh Active Response.

### VirusTotal API

- Used to submit file hash information for reputation lookup.
- Retrieves threat intelligence information.
- Provides malicious, suspicious, harmless, and undetected detection statistics when available.

### HTTP Request and JSON

- HTTP Request nodes handle API communication.
- JSON is used to process API request and response data.
- API responses are passed between workflow nodes.

## 7. Python Quarantine Script

A custom Python script was developed for automated file quarantine through Wazuh Active Response.

### Key Features

- Accepts a file path and confirmation argument.
- Restricts file processing to the configured test directory.
- Moves eligible files to the quarantine directory.
- Handles filename conflicts.
- Records quarantine operations in a log file.

### Test Directories

| Directory | Purpose |
|---|---|
| `C:\SOC-Test` | Monitored test directory |
| `C:\SOC-Quarantine` | Quarantine destination |

## 8. Project Directory Structure

```text
Self-Healing-SOC/
│
├── active-response/
│   └── wazuh_quarantine_ar.py
│
├── docs/
│   └── project-overview.txt
│
├── n8n-workflow/
│   └── Self-Healing-SOC-workflow-sanitized.json
│
├── wazuh-config/
│   └── ossec-config-notes.txt
│
├── screenshots/
│   ├── 01-soc-test-files.png
│   ├── 02-n8n-successful-execution.png
│   ├── 03-quarantine-results.png
│   ├── 04-complete-n8n-workflow.png
│   └── 05-wazuh-file-deletion-alert.png
│
└── README.md
```

## 9. Testing and Validation

The project was tested in a controlled virtual lab environment.

Testing included:

- Wazuh endpoint file activity detection.
- Security alert generation.
- n8n workflow execution.
- VirusTotal file hash reputation lookup.
- Groq AI Agent integration.
- REST API communication.
- Wazuh Active Response execution.
- Python quarantine script execution.
- Quarantine log verification.

### EICAR Testing

The EICAR antivirus test file was used to validate antivirus detection and testing workflows.

**Note:** EICAR is a harmless antivirus test signature, not actual malware.

## 10. Security Considerations

- The quarantine script restricts file processing to the configured test directory.
- A confirmation argument is required before quarantine execution.
- API credentials and sensitive configuration values must not be published.
- Testing should be performed using harmless files in a controlled environment.
- AI-generated analysis should be validated before being relied upon for security decisions.

## 11. Limitations

- Tested in a controlled virtual lab environment.
- VirusTotal analysis depends on available threat intelligence data.
- AI-generated output may require human verification.
- Quarantine is restricted to the configured test directory.
- The project is an educational prototype and is not production-ready.

## 12. Future Enhancements

- Integrate additional threat intelligence sources.
- Improve AI-assisted alert prioritization.
- Develop a centralized security monitoring dashboard.
- Extend automated incident response capabilities.
- Improve incident reporting and analytics.
- Add more endpoint monitoring and response scenarios.

## 13. Disclaimer

This project is developed for educational and defensive cybersecurity purposes only.

All testing is performed in a controlled lab environment.
